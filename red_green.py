from PIL import Image

def getcolor(filename):
	im=Image.open(filename)
	pix=im.load()
	imtuple=im.size
	l=imtuple[0]
	b=imtuple[1]
	countred=0
	countgreen=0
	# Introduced error margin to reduce the error.
	errormargin=5
	for i in range(l):
		for j in range(b):
			temptuple=pix[i,j]
			if(temptuple[0]>temptuple[1]+errormargin):
				countred=countred+1
			if(errormargin+temptuple[0]<temptuple[1]):
				countgreen=countgreen+1
	if(countred>=countgreen):
		return "RED"
	else:
		return "GREEN"
