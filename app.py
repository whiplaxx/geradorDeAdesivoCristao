#!/bin/env python3.7

import editImage
from os import listdir
from PIL import Image, ImageDraw, ImageFont
from random import choice, randint
from sys import exit

# PATHS
IMAGES_PATH = 'images/'
FIGURES_PATH = IMAGES_PATH+'figures/'
FRAMES_PATH = IMAGES_PATH+'frames/'
FONTS_PATH = 'fonts/'
PHRASES_PATH = 'phrases.txt'

# VARIABLES
BORDER_SIZE_DEFAULT = (40,20,40,20)
ADESIVO_WIDTH = 300
STROKE_WIDTH = 5
STROKE_FILL = (0,0,0)

class Adesivo():

	def __init__(self):
		# Loading elements
		self.figuresNames = listdir(FIGURES_PATH)
		self.framesNames = listdir(FRAMES_PATH)
		self.fontsNames = listdir(FONTS_PATH)
		self.phrases = []
		with open(PHRASES_PATH, 'r', encoding='utf-8') as phrasesFile:
			for line in phrasesFile:
				if line != '':
					self.phrases.append( line.replace('\\n', '\n'))
		self.figure = ''
		self.frame = ''
		self.font = ''
		self.phrase = ''
		self.borderColor = ''
		self.fontColor = ''

	def buildRandomAdesivo(self, fileName='adesivo'):

		self.randomizeElements()

		# Adding border
		self.adesivo = editImage.createBorder( self.figure, BORDER_SIZE_DEFAULT, self.borderColor)
		# Resizing frame
		self.frame = editImage.resizeProp_width( self.frame, self.adesivo.size[0] )
		# Adding the frames
		self.adesivo = editImage.pasteBottom( self.adesivo, self.frame, 'l')
		self.frame = self.frame.rotate(180)
		self.adesivo = editImage.pasteTop( self.adesivo, self.frame, 'r')

		# Resizing adesivo
		self.adesivo = editImage.resizeProp_width( self.adesivo, ADESIVO_WIDTH)

		# Adding text
		draw = ImageDraw.Draw(self.adesivo)
		self.phrase = editImage.fitText( (self.adesivo.size[0]*0.8), self.phrase, self.font)
		textSize = draw.multiline_textsize(self.phrase, font=self.font, stroke_width=STROKE_WIDTH)
		textPositionTuple = ( int((self.adesivo.size[0]-textSize[0])/2), self.adesivo.size[1]-textSize[1])
		draw.multiline_text( textPositionTuple, self.phrase, font=self.font, fill=self.fontColor, align='center', stroke_width=STROKE_WIDTH, stroke_fill=STROKE_FILL)

		self.adesivo.save( fileName + '.png')

	def randomizeElements(self):
		self.randomizeElement('figure')
		self.randomizeElement('frame')
		self.randomizeElement('font')
		self.randomizeElement('phrase')
		self.borderColor = self.randomizeColor()
		self.fontColor = self.randomizeColor()

	# elements = 'figure', 'frame', 'font', 'phrase'
	def randomizeElement(self, element):
		
		if element == 'figure':
			self.figure = Image.open( FIGURES_PATH + choice(self.figuresNames) )
		elif element == 'frame':
			self.frame = Image.open( FRAMES_PATH + choice(self.framesNames) )
		elif element == 'font':
			self.font = ImageFont.truetype( FONTS_PATH + choice(self.fontsNames), int(ADESIVO_WIDTH/8))
		elif element == 'phrase':
			self.phrase = choice(self.phrases)
		else:
			exit( "The passed element ('" + str(element) + "') to 'randomizeElement' doesn't match any of the options (figure, frame, font or phrase)." )
	
	def randomizeColor(self):
		templates = [
			(0, 255, randint(0,255)),
			(0, randint(0,255), 255),
			(255, 0, randint(0,255)),
			(255, randint(0, 255), 0),
			(randint(0,255), 255, 0),
			(randint(0,255), 0, 255)
		]
		return choice(templates)


if __name__ == "__main__":
	
	a = Adesivo()
	a.buildRandomAdesivo()
