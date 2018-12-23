import numpy as np
import pandas as p
import secrets

#intialize board
board_starting_white = np.array([[22,23,24,25,26,24,23,22],
				[21,21,21,21,21,21,21,21],
				[0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0],
				[11,11,11,11,11,11,11,11],
				[12,13,14,15,16,14,13,12]])

board = board_starting_white

#initalize column and row labels
r_labels = ['1', '2', '3', '4', '5', '6', '7', '8']
c_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

#pretty up the board
pretty_board = p.DataFrame(data=board, index=r_labels, columns=c_labels, dtype='int8')

#global vars
kings_alive = 1
wking_alive = 1
bking_alive = 1
piece = 'sdf'
move = 'dfd'

#def kings_check():

def coor_convert_piece():
	#A column
	if piece == A1:
		piece = board[0,0]
	elif piece == A2:
		piece = board[1,0]
	elif piece == A3:
		piece = board[2,0]
	elif piece == A4:
		piece = board[3,0]
	elif piece == A5:
		piece = board[4,0]
	elif piece == A6:
		piece = board[5,0]
	elif piece == A7:
		piece = board[6,0]
	elif piece == A8:
		piece = board[7,0]
	#B column
	elif piece == B1:
		piece = board[0,1]
	elif piece == B2:
		piece = board[1,1]
	elif piece == B3:
		piece = board[2,1]
	elif piece == B4:
		piece = board[3,1]
	elif piece == B5:
		piece = board[4,1]
	elif piece == B6:
		piece = board[5,1]
	elif piece == B7:
		piece = board[6,1]
	elif piece == B8:
		piece = board[8,1]
	#C column
	elif piece == C1:
		piece = board[0,2]
	elif piece == C2:
		piece = board[1,2]
	elif piece == C3:
		piece = board[2,2]
	elif piece == C4:
		piece = board[3,2]
	elif piece == C6:
		piece = board[5,2]
	elif piece == C7:
		piece = board[6,2]
	elif piece == C8:
		piece = board[7,2]
	#D column
	elif piece == D1:
		piece = board[0,3]
	elif piece == D2:
		piece = board[1,3]
	elif piece == D4:
		piece = board[2,3]
	elif piece == D4:
		piece = board[3,3]
	elif piece == D5:
		piece = board[4,3]
	elif piece == D6:
		piece = board[5,3]
	elif piece == D7:
		piece = board[6,3]
	elif piece == D8:
		piece = board[7,3]
	#E Column
	elif piece == E1:
		piece = board[0,4]
	elif piece == E2:
		piece = board[1,4]
	elif piece == E3:
		piece = board[2,4]
	elif piece == E4:
		piece = board[3,4]
	elif piece == E5:
		piece = board[4,4]
	elif piece == E6:
		piece = board[5,4]
	elif piece == E7:
		piece = board[6,4]
	elif piece == E8:
		piece = board[7,4]
	#F column
	elif piece == F1:
		piece = board[0,5]
	elif piece == F2:
		piece = board[1,5]
	elif piece == F3:
		piece = board[2,5]
	elif piece == F4:
		piece = board[3,5]
	elif piece == F5:
		piece = board[4,5]
	elif piece == F6:
		piece = board[5,5]
	elif piece == F7:
		piece = board[6,5]
	elif piece == F8:
		piece = board[7,5]
	#G column 
	elif piece == G1:
		piece = board[0,6]
	elif piece == G2:
		piece = board[1,6]
	elif piece == G3:
		piece = board[2,6]
	elif piece == G4:
		piece = board[3,6]
	elif piece == G5:
		piece = board[4,6]
	elif piece == G6:
		piece = board[5,6]
	elif piece == G7:
		piece = board[6,6]
	elif piece == G8:
		piece = board[7,6]
	#H column 
	elif piece == H1:
		piece = board[0,7]
	elif piece == H2:
		piece = board[1,7]
	elif piece == H3:
		piece = board[2,7]
	elif piece == H4:
		piece = board[3,7]
	elif piece == H5:
		piece = board[4,7]
	elif piece == H6:
		piece = board[5,7]
	elif piece == H7:
		piece = board[6,7]
	elif piece == H8:
		piece = board[7,7]
	return piece


#def pawn():

#def rook():

#def knight():

#def bishop():

#def queen():

def game():
	#nice prompt 
	print("Welcome to Terminal Chess.")
	print("First digit of a number corresonds to the color of the piece, the second to the type.")
	print("White = 1, Black = 2.")
	print("Pawn = 1, Rook = 2, Knight = 3, Bishop = 4, Queen = 5, King = 6.")
	print("Yes, numbers, I know.... It's faster computationally.")
	
	kings_alive = 1
	#game logic	
	while kings_alive == 1:
		print(pretty_board)
		piece = input("Enter the piece's position that you would like to move.")
		move = input("Enter the position that you would like to move too. Enter The letter as capital.")
		print(piece, move)
		coor_convert_piece()
		print(piece, move)


		if wking_alive == 1 and bking_alive == 1:
			kings_alive = 1
			
		else:
			kings_alive = 0  
		
		

	#end condition logic
	if wking_alive == 1:
		print("White Won")

	elif bking_alive == 1:
		print("Black Won")

	else:
		print("You have quit the game.")


game()

	
