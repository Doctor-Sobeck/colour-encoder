import math

def encodeColour(r,g,b):
	# colour = (0 - 255)
	return (r+g*256+b*65536)

def unencodeColour(colour):
	# Set each colour value 
	r = math.floor(colour%256)
	g = math.floor((colour-r)%65536/256)
	b = math.floor((colour-g-r)/65536)
	
	return (r,g,b)
