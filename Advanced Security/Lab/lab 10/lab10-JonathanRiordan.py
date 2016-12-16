''' 
Part 1 
Student Name: Jonathan Riordan
Student Id: C13432152
'''
from PIL import Image
from PIL import ImageColor
import base64

from pylab import *
import numpy as np

print "*********** Part 1 ************"
inputImage='grayscale.jpg'

pilImage=Image.open(inputImage)
rgb_im = pilImage.convert('RGB')
pix = pilImage.load()

#pilImage.show()
imageSize = pilImage.size
im = Image.new('RGB',imageSize, "white")

pixels = im.load()

#im.show()
print imageSize

width = int(imageSize[0])
height = int(imageSize[1])
i = 0
j = 0

colourPixel = []
print width
print height
for i in range(0,width):
	for j in range(0, height):
		r, g, b = rgb_im.getpixel((i,j))
		print r, g, b
		pixels[i, j] = (r, g, b, 255)
		
im.show()
pilImage.show()


# Part 2 

def pad_message(text):
	missing = 8 - len(text)
	return ( '0' * missing ) + text

def encryptMessage(message):
	binaryMessage = []
	# iterate through the massge to get the bits.
	i=0
	
	# Get lenfth of the key and concert each character to a bit.
#	while i < len(message):
#		print message[i]
#		print(bin(ord(message[i])))
#		binaryMessage.append(bin(ord(message[i])))
#		i += 1
#	print ("Length of binary message array: " + str(len(binaryMessage)))
	# iterate through the image.
	
	b = ''
	# convert message to binary string
	for char in message: b += pad_message( bin(ord(char))[2:])
	print "message in binary: " + b
	inputImage='grayscale.jpg'

	pilImage=Image.open(inputImage)
	rgb_im = pilImage.convert('RGB')
	pix = pilImage.load()

	#pilImage.show()
	imageSize = pilImage.size
	im = Image.new('RGB',imageSize, "white")

	pixels = im.load()

	#im.show()
	print imageSize

	width = int(imageSize[0])
	height = int(imageSize[1])
	i = 0
	j = 0

	colourPixel = []
	counter = 0

	for i in range(0,width):
		for j in range(0, height):
			pixel = rgb_im.getpixel((i,j))[0]
			if counter < len(b):
				bin_pixel = bin(pixel)[2:-1]
				new_pix_bin = bin_pixel + b[ counter % len(b)]
				pixel = int(new_pix_bin, 2)
			counter += 1
		
			pixels[i, j] = ( int(pixel), int(pixel), int(pixel) )
			
	im.save('encrypted_img.jpg')
	im.show()
	pilImage.show()

	
	
	
	
	
print "*********** Part 2 ************"
print "Encrypting plaintext into the image"

plaintext = "hello, my name is jonathan riordan"

encryptMessage(plaintext)
		