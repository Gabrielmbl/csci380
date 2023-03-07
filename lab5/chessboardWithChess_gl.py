# •	Given the chessboard, draw a red chess and place it at the first cell of the chessboard.


import cv2 
import numpy as np
print(cv2.__version__)

board_size = int(input('Desired width: '))
num_squares = int(input('Desired number of squares per row: '))
square_size = int(board_size/num_squares)

board = np.zeros([board_size, board_size, 3], dtype = np.uint8)

print_chessboard = True
y = 0


frame = np.zeros((250, 250, 3), dtype = np.uint8)
frame = cv2.resize(frame, (board_size, board_size))

for row in range(0, num_squares):
    if num_squares % 2 == 0:
        print_chessboard = not print_chessboard
    x = 0
    for col in range(0, num_squares):
        if print_chessboard == True:
            board[y : y+square_size, x : x+square_size, :] = 255
            x += square_size
            print_chessboard = False
        else:
            x += square_size
            print_chessboard = True
    
    y += square_size

chess_coordinates = (int(square_size/2), int(square_size/2))
radius = (int(square_size/2))

image = cv2.circle(board, chess_coordinates, radius, (0,0,255), -1)

cv2.imshow('chessboard', board)
cv2.waitKey(0)

cv2.destroyAllWindows()
