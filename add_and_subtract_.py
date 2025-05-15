#import section
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import math
import cv2
from math import * 
import numpy as np
original_image1 = Image.open("S(2).jpeg") # Name of the image
original_image2 = Image.open("S(4).jpeg") # Name of the image
original_image_grayscale1 = ImageOps.grayscale(original_image1)
original_image_grayscale2 = ImageOps.grayscale(original_image2)
plt.imshow(original_image_grayscale1)
#plt.imshow(original_image_grayscale2)
# Obtain the number of rows and columns
# of the image
width, height  = original_image_grayscale1.size
Filtered = np.zeros((height,width, 3), np.uint8)
imagev1= original_image_grayscale1.load()
imagev2= original_image_grayscale2.load()
for i in range(1, width-1):
  for j in range(1,height-1 ):
     Filtered[j,i]= imagev2[i,j]-imagev1[i,j]
filtered_imager = Filtered 
#plt.imshow(filtered_image)
plt.imsave('Filtered_imagea-b.jpg', filtered_imager, cmap='gray')
Filtereds = np.zeros((height,width, 3), np.uint8)
for i in range(1, width-1):
  for j in range(1,height-1 ):
     Filtereds[j,i]= imagev2[i,j]+imagev1[i,j]
filtered_images = Filtereds 
#plt.imshow(filtered_image)
plt.imsave('Filtered_imagea+b.jpg', filtered_images, cmap='gray')
#logaritmic 
#width, height  = filtered_image.size
filtered_image1 = Image.open("Filtered_image.jpg") # Name of the image
Filtered1 = np.zeros((height,width, 3), np.uint8)
C=20
original_image_grayscalex = ImageOps.grayscale(filtered_image1)
imagev= original_image_grayscalex.load()
for i in range(1, width-1):
  for j in range(1,height-1 ):
     pixel=(np.log10(1+imagev[i,j]))*C
     Filtered1[j,i]=pixel
filtered_imagex = Filtered1 #Image.fromarray(Filtered)
plt.imsave('Filtered_logaritmic.jpg', filtered_imagex, cmap='gray')
plt.imshow(filtered_imagex)
#original_image1=original_image1_grayscale
#original_image2=original_image2_grayscale
filtered = filtered_imagex
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4 ,figsize=(10 , 10))
ax1.title.set_text("Image1")
ax1.axis("off")
ax1.imshow(original_image_grayscale1,cmap='gray')
ax2.title.set_text("Image2")
ax2.axis("off")
ax2.imshow(original_image_grayscale2, cmap='gray')
ax3.title.set_text("Filtered substract")
ax3.axis("off")
ax3.imshow(filtered_imager, cmap='gray')
ax4.title.set_text("Filtered add")
ax4.axis("off")
ax4.imshow(filtered_images, cmap='gray')