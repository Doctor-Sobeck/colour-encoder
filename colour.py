import math
def encodeColour(r,g,b):
	# colour = (0 - 255)
	return (r+g*256+b*65536)

def unencodeColour(colour):
	r = colour%256
	g = (colour-r)%65536/256
	b = ((colour-g)-r)/65536
	return (math.floor(r),math.floor(g),math.floor(b))