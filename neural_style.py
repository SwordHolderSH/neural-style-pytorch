from vgg import Vgg16
import utils
from torchvision import transforms
import torch.nn as nn
import torch.optim as optim
import numpy as np
from matplotlib import pyplot as plt
import torch


# Set args.
# You can use argparse.ArgumentParser() to instead

EPOCHS = 1000000
STYLE_IMG_PATH = './style/s.jpg'
# CONTENT_IMG_PATH = './content/code0.8.jpg'
CONTENT_IMG_PATH = './content/boy.bmp'
OUTPUT_DIR = './output/'
IMAGE_SIZE = 512
BATCH_SIZE = 1
LEARNING_RATE = 0.01
CONTENT_WEIGHT = 1
STYLE_WEIGHT = 1e10
TV_WEIGHT = 0.0001

transform = transforms.Compose([
    transforms.Resize(IMAGE_SIZE),
    transforms.ToTensor(),
])

style_transform = transforms.Compose([
    transforms.Resize(IMAGE_SIZE),
    transforms.ToTensor(),
])

vgg = Vgg16(requires_grad=False).cuda()  # vgg16 model

I = utils.scale_image(filename=STYLE_IMG_PATH, size=128, scale=512)

I = np.array(I)
plt.imshow(I)
plt.show()

style_img = utils.load_image(filename=STYLE_IMG_PATH, size=IMAGE_SIZE)
# style_img = utils.image_compose(IMG=style_img, IMAGE_ROW=4, IMAGE_COLUMN=4, IMAGE_SIZE=128)
content_img = utils.load_image(filename=CONTENT_IMG_PATH, size=IMAGE_SIZE)

style_img = style_transform(style_img)
content_img = transform(content_img)

style_img = style_img.repeat(BATCH_SIZE, 1, 1, 1).cuda()  # make fake batch
content_img = content_img.repeat(BATCH_SIZE, 1, 1, 1).cuda()

features_style = vgg(style_img)  # feature maps extracted from VGG
features_content = vgg(content_img)

gram_style = [utils.gram_matrix(y) for y in features_style]  # gram matrix of style feature

mse_loss = nn.MSELoss()

y = content_img.detach()  # y is the target output. Optimized start from the content image.
y = y.requires_grad_()  # let y required the grad

optimizer = optim.Adam([y], lr=LEARNING_RATE)  # let optimizer optimize the tensor y

print(" Start training ========================================")
for epoch in range(EPOCHS):

    def closure():
        optimizer.zero_grad()
        y.data.clamp_(0, 1)
        features_y = vgg(y)  # feature maps of y extracted from VGG
        gram_style_y = [utils.gram_matrix(i) for i in features_y]  # gram matrixs of feature_y in relu1_2,2_2,3_3,4_3

        fc = features_content.relu4_3  # content target in relu4_3
        fy = features_y.relu4_3  # y in relu4_3

        style_loss = 0  # add style_losses in relu1_2,2_2,3_3,4_3
        for fy_gm, fs_gm in zip(gram_style_y, gram_style):
            style_loss += mse_loss(fy_gm, fs_gm)
        style_loss = STYLE_WEIGHT * style_loss

        # fy_gm = gram_style_y[3]
        # fs_gm = gram_style[3]
        # style_loss = STYLE_WEIGHT * mse_loss(fy_gm, fs_gm)

        content_loss = CONTENT_WEIGHT * mse_loss(fc, fy)  # content loss

        tv_loss = TV_WEIGHT * (torch.sum(torch.abs(y[:, :, :, :-1] - y[:, :, :, 1:])) +
                               torch.sum(torch.abs(y[:, :, :-1, :] - y[:, :, 1:, :])))

        total_loss = content_loss + style_loss + tv_loss
        total_loss.backward(retain_graph=True)

        if epoch % 100 == 0:
            print("Epoch {}: Style Loss : {:4f} Content Loss: {:4f} TV Loss: {:4f}".format(epoch, style_loss,
                                                                                           content_loss, tv_loss))
        if epoch % 1000 == 0:
            utils.save_image_epoch(y, './outputs/', epoch)
        return total_loss


    optimizer.step(closure)
