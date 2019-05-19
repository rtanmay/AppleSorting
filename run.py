import red_green
import size_sorting

filename="./tempr.jpg"

is_red=False
is_big=False
Angle=-1


color_of_apple = red_green.getcolor(filename)
if(color_of_apple == "RED"):
	is_red=True
else:
	is_red=False

# if(is_red):
# 	print(0)
# else:
# 	print(45)

# Working

size_of_apple = size_sorting.getsize(filename)

if(size_of_apple == "BIG"):
	is_big=True
else:
	is_big=False

if(is_red and is_big==False):
	Angle = 0

if(is_red and is_big):
	Angle = 25

if(is_red==False and is_big==False):
	Angle = 50

if(is_red==False and is_big):
	Angle = 75

print(Angle)
# # How to Send the angle information to motor?