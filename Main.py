from ChessPLib import *
from math import *

debugRotation=0
bnw = 0

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

debugDictionairy = {
    0 : None,
    1 : "knight",
    2 : "bishop",
    3 : "queen",
    4 : "checker",
    5 : "rook",
    6 : "pawn",
    "rook" : rookMoves,
    "knight" : knightMoves,
    "bishop" : bishopMoves,
    "queen" : rookMoves + bishopMoves,
    "checker" : checkerMoves,
    "pawn" : pawnMoves,
    "blank" : "I have a skill issue"
}

quickGen("d", board)

turn = True
running = True

py.display.set_caption('Goofy Chess')
py.display.set_icon(py.image.load("Assets/blackpawn.png"))

notation = []

while running:         
    mouseCellx = floor(py.mouse.get_pos()[0]/screen.square_size) if floor(py.mouse.get_pos()[0]/screen.square_size) < (board.w-1) else board.w-1
    mouseCelly = floor(py.mouse.get_pos()[1]/screen.square_size) if floor(py.mouse.get_pos()[1]/screen.square_size) < (board.h-1) else board.h-1 # Finds which cell the mouse is in

    currentCell = board.get_cell(mouseCellx, mouseCelly)
    
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1: #Left Click
            if currentCell.validMove == True: #Uses the painted tiles as the valid moves, each cell has an attribute called "Valid Move"
                lastCell.piece.move(currentCell)
                print(genChessNotation(lastCell.piece.pieceType, currentCell, False if currentCell.piece == None else True, board))

                # Notation Generation
                notation.append(genChessNotation(lastCell.piece.pieceType, currentCell, False if currentCell.piece == None else True, board))
                print(notation)

                # Moves the piece
                currentCell.piece = lastCell.piece
                lastCell.piece = None
                print("I moved!")
                
                if currentCell.NBT != None: #NBT Data Actions
                    if currentCell.NBT[0] == "killMyPiece": #Kill piece action
                        board.get_cell(currentCell.NBT[1], currentCell.NBT[2]).piece = None

                    if currentCell.NBT[0] == "Swapsies": #Move a piece somewhere else
                        board.get_cell(currentCell.NBT[1], currentCell.NBT[2]).piece.cell = board.get_cell(currentCell.NBT[3], currentCell.NBT[4])
                        board.get_cell(currentCell.NBT[3], currentCell.NBT[4]).piece = board.get_cell(currentCell.NBT[1], currentCell.NBT[2]).piece
                        board.get_cell(currentCell.NBT[1], currentCell.NBT[2]).piece = None

                    currentCell.NBT = None # Remove the NBT after its used
                
                Cell.reset_all_NBT()

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
                
        if event.type == py.MOUSEBUTTONDOWN and event.button == 3: #Right Click
            print(debugRotation)
            print(debugRotation%(len(debugDictionairy)/2))
            if debugDictionairy[debugRotation%(len(debugDictionairy)/2)] != None:
                currentCell.piece = Piece(debugDictionairy[debugRotation%(len(debugDictionairy)/2)], board, (currentCell.x, currentCell.y), debugDictionairy[debugDictionairy[debugRotation%(len(debugDictionairy)/2)]], True if bnw%2 == 0 else False)
            else:
                currentCell.piece = None
            if bnw%2 == 0:
                debugRotation += 1 
            bnw += 1
            if debugRotation == 11:
                debugRotation = 0
    
    clickedThisFrame = False
    screen.run(board)
    
print(notation)

screen.quit()