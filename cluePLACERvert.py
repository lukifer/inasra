#!/usr/bin/env python3
import json
import re
from pdb import set_trace
from os import system
from sys import argv

# feed me an partially constructed crossword puzzle in a 2d array, in ipuz notation (board)
# and a word (alexicon) you want to place on the board, the valid location for the first letter of the word x,y,
# and clueinsert will return the puzzle with the clue inserted
# zip* the board to do down!!


with open("xwordspine.json") as readio: board =json.loads(readio.read())
alexicon = argv[1]
position = [int(argv[2]),int(argv[3])]


def sanitize(alexicon):
	if len(alexicon) > len(board[0]) - position[1]:
		print("too long, submit shorter word")
		exit()
	if re.search("[^a-zA-Z ]", alexicon,) is None:
		alexicon = ''.join(alexicon.lower().split(' '))
		#set_trace()
		return alexicon
	else: 
		print("remove offending characters, submit l8ter")
		exit()

def insert(alexicon, position):
	regexalexicon = re.compile(''.join(board[position[0]][position[1]:position[1]+len(alexicon)]).replace(' ','.'))
	#set_trace()
	if regexalexicon.match(alexicon) is None:
		print('this word does not fit the position you have specified')
		exit()
	for letter in alexicon:
		board[position[0]][position[1]] = letter
		position[1] = position[1]+1
	#for e in board: print(e)

#for e in board: print(' '.join(e))
board = [list(row) for row in list(zip(*board))] 
#for e in board: print(' '.join(e))

insert(sanitize(alexicon), position)
board = [list(row) for row in list(zip(*board))] 
with open('.NextMoves/'+alexicon+".PlacedClue.VERT."+str(position[0])+'.'+str(position[1]), 'w') as writio:
	writio.write(json.dumps(board))
