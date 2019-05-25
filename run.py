import red_green
import size_sorting
import cv2
from PIL import Image
import numpy as np
import CNNtest

filename="./try.jpg"

im = cv2.imread(filename)
im = cv2.resize(im, (500,500))
# back = cv2.imread("./background.jpg")
# im = im - back
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
im=Image.fromarray((im).astype(np.uint8))
im.save("try.jpg")

# Initialise the variables
is_red=False
is_big=False
is_good=False
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
quality_of_apple = CNNtest.quality(filename)
if(quality_of_apple=="GOOD"):
	is_good=True

# WRITE 5 combinations for 5 boxes and angle accordingly

if(is_good==False):
	# print("BAD")
	Angle =0

else:
	# print("GOOD")
	if(is_red==False and is_big==False):
		Angle = 79

	if(is_red and is_big==False):
		Angle = 28

	if(is_red==False and is_big):
		Angle = 103

	if(is_red and is_big):
		Angle = 56


print(Angle)