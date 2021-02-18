#!/bin/env python3.7

from PIL import Image, ImageDraw

def resizeProp_width( image, newWidth ):
	width = image.size[0]
	height = image.size[1]
	
	newHeight = int( height * (newWidth / width) )
	
	newImage = image.resize( (newWidth, newHeight) )
	return newImage

def resizeProp_height( image, newHeight ):
	width = image.size[0]
	height = image.size[1]

	newWidth = int( width * (newHeight / height) )
	
	newImage = image.resize( (newWidth, newHeight) )
	return newImage

def pasteTop( imageBase, imageFore, verticalAlignment='l'):
	
	if verticalAlignment=='r' or verticalAlignment=='right':
		leftPosition = imageBase.size[0] - imageFore.size[0]
	elif verticalAlignment=='c' or verticalAlignment=='center':
		leftPosition = int( (imageBase.size[0] - imageFore.size[0])/ 2)
	else:
		leftPosition = 0
	positionTuple = (leftPosition, 0)

	imageBase.paste( imageFore, positionTuple, mask=imageFore)
	return imageBase

def pasteBottom( imageBase, imageFore, verticalAlignment='l'):
	
	if verticalAlignment=='r' or verticalAlignment=='right':
		leftPosition = imageBase.size[0] - imageFore.size[0]
	elif verticalAlignment=='c' or verticalAlignment=='center':
		leftPosition = int( (imageBase.size[0] - imageFore.size[0])/ 2)
	else:
		leftPosition = 0
	positionTuple = (leftPosition, imageBase.size[1]-imageFore.size[1])

	imageBase.paste( imageFore, positionTuple, mask=imageFore)
	return imageBase


def createBorder( image, bordersSize, colorRgb=(255,255,255)):

	newImageWidth = image.size[0]+bordersSize[0]+bordersSize[2]
	newImageHeight = image.size[1]+bordersSize[1]+bordersSize[3]
	newImageSize = ( newImageWidth, newImageHeight )

	newImage = Image.new('RGB', newImageSize, colorRgb )
	newImage.paste( image, ( bordersSize[0], bordersSize[1] ) )
	return newImage


def fitText(width, text, font):
	
	draw = ImageDraw.Draw( Image.new('RGB', (1,1)) )
	
	textWords = text.replace('\n','').split(' ')
	
	text = ""
	for word in textWords:
		textSize = draw.multiline_textsize( text+word, font=font)
		if textSize[0] < width:
			text += word + ' '
		else:
			text += '\n' + word + ' '
	
	return text

