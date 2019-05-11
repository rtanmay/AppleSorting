rom PIL import Image

filename="./tempr.jpg"
im=Image.open(filename)

pix=im.load()

imtuple=im.size

l=imtuple[0]
b=imtuple[1]

print("Length of Image=",l,"\nBreadth of Image=",b)

# Introduced error margin to reduce the computations.
# Can it be used here
errormargin=5

countsize=0
for i in range(l):
	for j in range(b):
		if(insideapple())
			countsize=countsize+1

val=234
if(countsize>=val):
	return True # True means apple is big
else:
	return False # False means apple is small