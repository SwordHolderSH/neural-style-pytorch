# neural-style-pytorch
A fast PyTorch implementation of "A Neural Algorithm of Artistic Style"

## introduction
I try some other codes for neural-style-pytorch, but their outputs may become noise in some epochs, such as epoch 45, 170 and 230 in Figure1. I don't know why.  
.<div align=center>  <img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/output.png" width="900" />
                                                          Figure 1 
Therefore, I simply implement the method of "A Neural Algorithm of Artistic Style" (http://arxiv.org/abs/1508.06576).
 
## Results
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
 Our output as shown in Figure 2, the outputs may be more stable, and will not become noise suddenly.
 .<div align=center>  <img src="https://github.com/SwordHolderSH/neural-style-pytorch/blob/master/demos/my_output.jpg" width="900" />
                                                          Figure 2
 

