import red_green
import size_sorting
import cv2
from PIL import Image
import numpy as np
# import CNNtest1

filename="./try.jpg"

im = cv2.imread(filename)
im = cv2.resize(im, (500,500))
im=Image.fromarray((im).astype(np.uint8))
# im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
im.save("try.jpg")

is_red=False
is_big=False
# is_good=False
Angle=-1


# COLOR
color_of_apple = red_green.getcolor(filename)
if(color_of_apple == "RED"):
	is_red=True

# SIZE
size_of_apple = size_sorting.getsize(filename)
if(size_of_apple == "BIG"):
	is_big=True

# QUALITY
# quality_of_apple = CNNtest1.quality(filename)
# if(quality_of_apple=="GOOD"):
# 	is_good=True

# print("QUALITY=", is_good)

# WRITE 8 combinations and angle accordingly

if(is_red and is_big==False):
	Angle = 0

if(is_red and is_big):
	Angle = 25

if(is_red==False and is_big==False):
	Angle = 50

if(is_red==False and is_big):
	Angle = 75

print(Angle)