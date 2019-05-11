import red_green
import small_big

#HOW TO GET THE FILENAME FROM CAMERA?
filename=""

is_red=False
is_big=False
Angle=-1

color_of_apple = getcolor(filename)
if(color_of_apple == "RED"):
	is_red=True
else:
	is_red=False

size_of_apple = getsize(filename)
if(size_of_apple == "BIG")
	is_big=True
else:
	is_big=False

if(is_red and is_small):
	Angle = 0

if(is_red and is_big):
	Angle = 25

if(is_green and is_small):
	Angle = 50

if(is_green and is_big):
	Angle = 75

# How to Send the angle information to motor?