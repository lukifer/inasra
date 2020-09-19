#!/usr/bin/env python3

from wand.color import Color
from wand.image import Image
from wand.drawing import Drawing
from wand.compat import nested
from sys import argv
import subprocess
from pdb import set_trace
import json

FontSize = 22
with open(argv[1]) as readio: board =json.loads(readio.read())
#set_trace()
Width = int(len(board[0]) * FontSize * .8)
Height = int(len(board) * FontSize)

with Drawing() as draw:
	with Image(width=Width, height=Height) as img:
		draw.font_family = 'Letter Gothic'
		#draw.font_style = "Outline"
		draw.font_size = FontSize
		draw.push()
		for row in enumerate(board):
			draw.text(int(Width/8),int(.7*FontSize*(row[0]+14)),' '.join(row[1]))	
	
		draw.pop()
		draw(img)
		img.save(filename='image.png')

subprocess.call(['feh','image.png'])
