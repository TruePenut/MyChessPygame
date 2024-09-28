from ChessPLib import *
from math import *

inputSize = input("What size board do you want? (s or y/x): ") #Get size of the board from player

if str(inputSize) == "s":
    print("Standard Board Size")
    board = Table(8,8)
else:
    height, width = map(int, inputSize.split("/"))
    board = Table(height, width)

screen = Display(board, 64, cWhite, cGreen)
    
board.print()

lastCell = None

# Move IDS
# 0: Can't Capture, only move
# 1: Can capture and move
# 2: Can only move if capturing (Eg. Pawn capture)
# 3: Can only be used on the first turn AND does not capture
# 4: Castling 1
# 5: Castling 2

bishopMoves = [[1, 1, 8, 1],[1, -1, 8, 1],[-1, -1, 8, 1],[-1, 1, 8, 1]]
rookMoves = [[0, 1, 8, 1],[0, -1, 8, 1],[-1, 0, 8, 1],[1, 0, 8, 1]]
knightMoves = [[2, 1, 1, 1],[2, -1, 1, 1],[-2, -1, 1, 1],[-2, 1, 1, 1],[1, 2, 1, 1],[1, -2, 1, 1],[-1, -2, 1, 1],[-1, 2, 1, 1]]
kingMoves = [[1, 0, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1], [-1, 1, 1, 1], [-1, 0, 1, 1], [-1, -1, 1, 1], [0, -1, 1, 1], [1, -1, 1, 1]]
pawnMoves = [[0, -1, 1, 0], [-1, -1, 1, 2], [1, -1, 1, 2], [0, -1, 2, 3]]

#Starting Board

for x in range(8):
    pawn = Piece("pawn", board, (x-1, 1), pawnMoves, False)
    
    pawn = Piece("pawn", board, (x-1, 6), pawnMoves, True)

brook1 = Piece("rook", board, (0, 0), rookMoves, False)
brook2 = Piece("rook", board, (7, 0), rookMoves, False)
knight = Piece("knight", board, (1, 0), knightMoves, False)
knight = Piece("knight", board, (6, 0), knightMoves, False)
bishop = Piece("bishop", board, (2, 0), bishopMoves, False)
bishop = Piece("bishop", board, (5, 0), bishopMoves, False)
queen = Piece("queen", board, (3,0), bishopMoves+rookMoves, False)
king = Piece("king", board, (4,0), kingMoves, False)

wrook1 = Piece("rook", board, (0, 7), rookMoves, True)
wrook2 = Piece("rook", board, (7, 7), rookMoves, True)
knight = Piece("knight", board, (1, 7), knightMoves, True)
knight = Piece("knight", board, (6, 7), knightMoves, True)
bishop = Piece("bishop", board, (2, 7), bishopMoves, True)
bishop = Piece("bishop", board, (5, 7), bishopMoves, True)
queen = Piece("queen", board, (3,7), bishopMoves+rookMoves, True)
king = Piece("king", board, (4,7), kingMoves, True)

turn = True

running = True
while running:         
    mouseCellx = floor(py.mouse.get_pos()[0]/screen.square_size) if floor(py.mouse.get_pos()[0]/screen.square_size) < (board.w-1) else board.w-1
    mouseCelly = floor(py.mouse.get_pos()[1]/screen.square_size) if floor(py.mouse.get_pos()[1]/screen.square_size) < (board.h-1) else board.h-1 # Finds which cell the mouse is in

    currentCell = board.get_cell(mouseCellx, mouseCelly)
    
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        
        if event.type == py.MOUSEBUTTONDOWN:
            if currentCell.validMove == True:
                lastCell.piece.move(currentCell)
                currentCell.piece = lastCell.piece
                lastCell.piece = None
                print("I moved!")
                
                if turn:
                    turn = False
                else:
                    turn = True
                
                board.resetBoard()
            else:
                board.resetBoard()
            if currentCell.piece != None and currentCell.piece.color == turn:
                board.resetBoard()
                currentCell.piece.genMoves()
                currentCell.piece.colorInMoves()
                lastCell = currentCell
    
    clickedThisFrame = False
    screen.run(board)
    
    

    
screen.quit()
