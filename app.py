#!/bin/env python3.7

import editImage
from os import listdir
from PIL import Image, ImageDraw, ImageFont
from random import choice, randint

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

if __name__ == "__main__":
	
	# Getting images names
	ls_figuresNames = listdir(FIGURES_PATH)
	ls_framesNames = listdir(FRAMES_PATH)
	ls_fontsNames = listdir(FONTS_PATH)
	ls_phrases = []
	with open(PHRASES_PATH, 'r', encoding='utf-8') as phrasesFile:
		for line in phrasesFile:
			if line != '':
				ls_phrases.append( line.replace('\\n', '\n'))
	
	# List of RGB colors for borders and fonts
	ls_bordersColors = [ (255,255,255), (52,180,235), (237,128,170) ]
	ls_fontsColors = [ (38,41,212), (242,5,52), (219,175,42)]

	# Randomizing elements
	figure = Image.open( FIGURES_PATH + choice(ls_figuresNames) )
	frame = Image.open( FRAMES_PATH + choice(ls_framesNames) )
	font = ImageFont.truetype( FONTS_PATH + choice(ls_fontsNames), int(ADESIVO_WIDTH/8))
	fontColor = (randint(150, 255), randint(150, 255), randint(150, 255))
	phrase = choice(ls_phrases)

	# Adding border
	adesivo = editImage.createBorder( figure, BORDER_SIZE_DEFAULT, choice(ls_bordersColors))
	# Resizing frame
	frame = editImage.resizeProp_width( frame, adesivo.size[0] )
	# Adding the frames
	adesivo = editImage.pasteBottom( adesivo, frame, 'l')
	frame = frame.rotate(180)
	adesivo = editImage.pasteTop( adesivo, frame, 'r')

	# Resizing adesivo
	adesivo = editImage.resizeProp_width(adesivo, ADESIVO_WIDTH)

	# Adding text
	draw = ImageDraw.Draw(adesivo)
	phrase = editImage.fitText( (adesivo.size[0]*0.8), phrase, font)
	textSize = draw.multiline_textsize(phrase, font=font, stroke_width=STROKE_WIDTH)
	textPositionTuple = ( int((adesivo.size[0]-textSize[0])/2), adesivo.size[1]-textSize[1])
	draw.multiline_text( textPositionTuple, phrase, font=font, fill=fontColor, align='center', stroke_width=STROKE_WIDTH, stroke_fill=STROKE_FILL)

	adesivo.save('adesivo.png')

