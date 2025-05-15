#import section
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import math
import cv2
from math import * 
import numpy as np
original_image = Image.open("lena.png") # Name of the image
original_image_grayscale = ImageOps.grayscale(original_image)
plt.imshow(original_image_grayscale)
# Obtain the number of rows and columns
# of the image
width, height  = original_image_grayscale.size
Filtered = np.zeros((height,width, 3), np.uint8)
imagev= original_image_grayscale.load()
for i in range(1, width-1):
  for j in range(1,height-1 ):
     Filtered[j,i]= 255-imagev[i,j]
filtered_image = Filtered #Image.fromarray(Filtered)
#filtered_image.save("image_without_noise.jpg")
plt.imshow(filtered_image)

