#!/usr/bin/env python3
import json
import re
from pdb import set_trace
from os import system
from sys import argv

# feed me an partially constructed crossword puzzle in a 2d array, in ipuz notation (board)
# and a word (alexicon) you want to place on the board, and findthenextword will return a list of valid places
# in the format: [[xCoord_of_First_Letter,yCoord_of_First_Letter]] which is the first letter placement of the accross clue
# zip* the board to do down!!

with open("xwordspine.json") as readio: board =json.loads(readio.read())

alexicon = argv[1]


def findnextwordspace (board, alexicon):
	lines = []
	for space in enumerate(board[0]):
		if  board[0][space[0]] == ' ' and board[1][space[0]] == ' ':
			board[0][space[0]] = '.'
	for space in enumerate(board[-1]):
		if  board[-1][space[0]] == ' ' and board[-2][space[0]] == ' ':
			board[-1][space[0]] = '.'
	for eachline in enumerate(board):
		for space in enumerate(board[0]):
			if board[eachline[0]][space[0]] == ' ':
				if board[eachline[0]-1][space[0]] == '.' or board[eachline[0]-1][space[0]] == ' ':
					if board[eachline[0]+1][space[0]] == '.' or board[eachline[0]+1][space[0]] == ' ':
							board[eachline[0]][space[0]] = '.'
	for each in board:
		lines.append(''.join(each))
	obstacle = re.compile('\.?[a-z][a-z]+\.?')
	legalplace = []
	for line in enumerate(lines):
		validstart = len(line[1])-len(alexicon)
		for validplace in range(validstart):
			if re.match(line[1][validplace:len(alexicon)+validplace], alexicon) is not None:
				#print("maybe! "+line[1][validplace:validplace+len(alexicon)])
				if re.search('[a-z| ]',line[1][validplace:len(alexicon)+validplace],) is not None:
					#print("found one at [" + str(line[0]) + "," + str(validplace) + "]:" + line[1][validplace:len(alexicon)+validplace], alexicon)
					if re.search('[a-z| ]',line[1][validplace-1],) is None:
						if re.search('[a-z| ]',line[1][validplace+len(alexicon)+1],) is None:
							#print(line[1][validplace-1])
							#print("found one at [" + str(line[0]) + "," + str(validplace) + "]:")
							legalplace.append((line[0],validplace))
	print('legalplaces for ' + alexicon + ':') 
	return legalplace
	#pdb.set_trace()


def sanitize(alexicon):
	if len(alexicon) > len(board[0]):
		print("too long, submit shorter word")
		exit()
	if re.search("[^a-zA-Z ]", alexicon,) is None:
		alexicon = ''.join(alexicon.lower().split(' '))
		return alexicon
	else: 
		print("remove offending characters, submit l8ter")
		exit()



findnextwordspace(board, sanitize(alexicon))


