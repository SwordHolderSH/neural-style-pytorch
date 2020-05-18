# neural-style-pytorch
A simple PyTorch implementation of "A Neural Algorithm of Artistic Style"

## introduction

I try some other codes for neural-style-pytorch, but their outputs may become noise in some epochs, such as epoch 45, 170 and 230 in Figure 1. I don't know why. Therefore, I simply implement the method of "A Neural Algorithm of Artistic Style (http://arxiv.org/abs/1508.06576). 

<div align=center>  <img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/output.png" width="900" /> </div>      
<p align="center">**Figure 1**</p>

## Results
<p align="left"> The output as shown in Table 1. </p>


 <table>
 <tr>
   <td>Style</td><td>Content</td><td>Output</td>
 </tr>
 <tr>
   <td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/style/s.jpg" width="200" /></td>
   <td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/content/dog_cat.jpg" width="200" />      </td>
   <td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/out_27000.jpg" width="200" /></td>
 </tr>
  
   <tr>
   <td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/style/picasso.jpg" width="200" /></td>
   <td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/out_0.jpg" width="200" />      </td>
   <td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/out_73000.jpg" width="200" /></td>
 </tr>
<tr>
   <td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/style/s.jpg" width="200" /></td>
   <td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/test/out_0.jpg" width="200" />      </td>
   <td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/test/out_300000.jpg" width="200" /></td>
 </tr>
 </table>
  <p align="center"> **Table 1**</p>



<p align="left">
Outputs of some epochs as shown in Figure 2 and Table 2, the outputs may be more stable, and will not become noise suddenly.
</p>

<div align=center>  <img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/my_output.jpg" width="900" /></div>
                                                          <p align="center">  **Figure 2**</p>


 <table>
 <tr>
   <td>epoch 0</td><td>epoch 1000</td><td>epoch 5000</td><td>epoch 10000</td>
 </tr>
  
  <tr>
   <td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/test/out_0.jpg" width="200" /></td><td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/test/out_1000.jpg" width="200" /></td><td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/test/out_5000.jpg" width="200" /></td><td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/test/out_10000.jpg" width="200" /></td>
 </tr>

 <tr>
   <td>epoch 50000</td><td>epoch 100000</td><td>epoch 200000</td><td>epoch 300000</td>
 </tr>
   <tr>
 <td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/test/out_50000.jpg" width="200" /></td>
   <td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/test/out_100000.jpg" width="200" /></td><td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/test/out_200000.jpg" width="200" /></td><td>.<div align=center><img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/test/out_300000.jpg" width="200" /></td>
 </tr> 
 </table>
 <p align="center">**Table 2**</p>     
 <p align="left"></p>
 
## Acknowledge

Thanks for the reference codes as following:

[1] fast_neural_style https://github.com/pytorch/examples/tree/master/fast_neural_style   
[2] neural-style-pytorch https://github.com/Zhenye-Na/neural-style-pytorch   
[3] neural-style-pytorch https://github.com/L1aoXingyu/neural-transfer     

The main program is neural_style.py. Inspired by [1], I calculate the losses in iterations directly, instead of modeling them in network. I also remove the normalization, and use Adam optimizer. The optimization speed of this code may slower than other PyTorch codes, which needs more epochs, but I don't know why.

