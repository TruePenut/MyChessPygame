import pygame as py

# TEST

# Color Palletes:
cGreen = (0, 92, 50)
cWhite = (247, 234, 173)
cRed = (191, 103, 144)
cBlue = (86, 118, 150)
cOrange = (255, 230, 105)

# Move IDS
# 0: Can't Capture, only move
# 1: Can capture and move
# 2: Can only move if capturing (Eg. Pawn capture)
# 3: Can only be used on the first turn AND does not capture
# 4: Move an extra tile after capturing
# 5: Castling (Must include more data, new format [x displacement, y displacement, distance, ID, [Global Pos of second piece, its new position relative to the first piece]])

# Format [x displacement, y displacement, distance, ID]

bishopMoves = [[1, 1, 8, 1],[1, -1, 8, 1],[-1, -1, 8, 1],[-1, 1, 8, 1]]
rookMoves = [[0, 1, 8, 1],[0, -1, 8, 1],[-1, 0, 8, 1],[1, 0, 8, 1]]
knightMoves = [[2, 1, 1, 1],[2, -1, 1, 1],[-2, -1, 1, 1],[-2, 1, 1, 1],[1, 2, 1, 1],[1, -2, 1, 1],[-1, -2, 1, 1],[-1, 2, 1, 1]]
kingMoves = [[1, 0, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1], [-1, 1, 1, 1], [-1, 0, 1, 1], [-1, -1, 1, 1], [0, -1, 1, 1], [1, -1, 1, 1], [1, -1, 1, 1], [-2, 0, 1, 5, [[-4, 0], [-1, 0]]], [2, 0, 1, 5, [[3, 0], [1, 0]]]]
pawnMoves = [[0, -1, 1, 0], [-1, -1, 1, 2], [1, -1, 1, 2], [0, -1, 2, 3]]
checkerMoves = [[1, 1, 2, 4],[1, -1, 2, 4],[-1, -1, 2, 4],[-1, 1, 2, 4],[0, 1, 1, 1],[0, -1, 1, 1],[-1, 0, 1, 1],[1, 0, 1, 1]]
pawn2Moves = [[1, -1, 1, 0],[-1, -1, 1, 0],[0, 1, 1, 2],[0, -1, 1, 2],[1, -2, 1, 3],[-1, -2, 1, 3]]

notationDict = {
    "rook" : "R",
    "knight" : "N",
    "bishop" : "B",
    "queen" : "Q",
    "king" : "K",
    "checker" : "C",
    "pawn" : ""

}

def genChessNotation(name, cell, killed, board):
    if killed:
        return f"{notationDict[name]}x{chr(65 + cell.x).lower()}{str(board.h - cell.y)}"
    else:
        return f"{notationDict[name]}{chr(65 + cell.x).lower()}{str(board.h - cell.y)}"
    
def quickGen(name, board):#Premade boards with set moves and pieces
    print(board)
    # Classic Starting Board
    if name == "s":
        for x in range(board.w):
            pawn = Piece("pawn", board, (x-1, 1), pawnMoves, False)
            
            pawn = Piece("pawn", board, (x-1, board.h-2), pawnMoves, True)

        brook1 = Piece("rook", board, (0, 0), rookMoves, False)
        brook2 = Piece("rook", board, (board.w-1, 0), rookMoves, False)
        knight = Piece("knight", board, (board.w-7, 0), knightMoves, False)
        knight = Piece("knight", board, (board.w-2, 0), knightMoves, False)
        bishop = Piece("bishop", board, (board.w-6, 0), bishopMoves, False)
        bishop = Piece("bishop", board, (board.w-3, 0), bishopMoves, False)
        queen = Piece("queen", board, (board.w-5,0), bishopMoves+rookMoves, False)
        king = Piece("king", board, (board.w-4,0), kingMoves, False, True)

        wrook1 = Piece("rook", board, (0, 7), rookMoves, True)
        wrook2 = Piece("rook", board, (board.w-1, board.h-1), rookMoves, True)
        knight = Piece("knight", board, (board.w-7, board.h-1), knightMoves, True)
        knight = Piece("knight", board, (board.w-2, board.h-1), knightMoves, True)
        bishop = Piece("bishop", board, (board.w-6, board.h-1), bishopMoves, True)
        bishop = Piece("bishop", board, (board.w-3, board.h-1), bishopMoves, True)
        queen = Piece("queen", board, (board.w-5,board.h-1), bishopMoves+rookMoves, True)
        king = Piece("king", board, (board.w-4,board.h-1), kingMoves, True, True)
    elif name == "d":
        for x in range(board.w):
            pawn = Piece("pawn", board, (x-1, 1), pawn2Moves, False)
            
            pawn = Piece("pawn", board, (x-1, board.h-2), pawn2Moves, True)

        brook1 = Piece("rook", board, (0, 0), rookMoves, False)
        brook2 = Piece("rook", board, (board.w-1, 0), rookMoves, False)
        knight = Piece("knight", board, (board.w-7, 0), knightMoves, False)
        knight = Piece("knight", board, (board.w-2, 0), knightMoves, False)
        princess = Piece("checker", board, (board.w-6, 0), checkerMoves, False)
        princess = Piece("checker", board, (board.w-3, 0), checkerMoves, False)
        queen = Piece("queen", board, (board.w-5,0), bishopMoves+rookMoves, False)
        king = Piece("king", board, (board.w-4,0), kingMoves, False, True)

        wrook1 = Piece("rook", board, (0, board.h-1), rookMoves, True)
        wrook2 = Piece("rook", board, (board.w-1, board.h-1), rookMoves, True)
        knight = Piece("knight", board, (board.w-7, board.h-1), knightMoves, True)
        knight = Piece("knight", board, (board.w-2, board.h-1), knightMoves, True)
        princess = Piece("checker", board, (board.w-6, board.h-1), checkerMoves, True)
        princess = Piece("checker", board, (board.w-3, board.h-1), checkerMoves, True)
        queen = Piece("queen", board, (board.w-5,board.h-1), bishopMoves+rookMoves, True)
        king = Piece("king", board, (board.w-4,board.h-1), kingMoves, True, True)

def averageColor(color1, color2,l = 0.750):
    return (color1[0]*l + color2[0]*(1-l), color1[1]*l + color2[1]*(1-l), color1[2]*l + color2[2]*(1-l))

class Signal:
    def __init__(self):
        self._subscribers = []

    def connect(self, callback):
        self._subscribers.append(callback)

    def emit(self, *args, **kwargs):
        for subscriber in self._subscribers:
            subscriber(*args, **kwargs)

class Piece: #Holds all the piece logic
    def __init__(self, pieceType, board, position, basicMoves, color, important = False): # Format [x displacement, y displacement, distance, ID] eg. Rook [[0,1,1,1],[1,0,1,1],[0,-1,1,1],[-1,0,1,1]]; Color is a bool
        #Initialised along with the pieces
        self.cell = board.get_cell(position[0], position[1])
        self.basicMoves = basicMoves
        self.board = board
        self.color = color
        self.pieceType = pieceType
        self.moveCounter = 0
        self.important = important

        #Variables that shift over time
        self.lastPosition = None
        self.listOfMoves = []

        board.livingPieces.append(self)
        
        #Sprites
        self.sprite_name = f"{'white' if self.color else 'black'}{self.pieceType}.png"
        self.sprite = py.image.load("Assets/"+self.sprite_name)
        
        print(f"{self.sprite_name} Initialised")
        
        self.cell.piece = self #Assigns a cell this piece
                
    def genMoves(self, dangerousCells): #Generate all the valid moves
        inDanger = False
        if self.cell.color == cRed: inDanger == True

        self.listOfMoves = []
        bOw = 1 if self.color else -1
        for move in self.basicMoves: 
            for x in range(move[2]): #How many tiles should the movement go
                if -1 < self.cell.x + move[0]*(x+1) < self.board.w and -1 < self.cell.y + move[1]*(x+1)*bOw < self.board.h: #Check if it is domain
                    theCellIAmMovingTo = self.board.get_cell(self.cell.x + move[0]*(x+1), self.cell.y + move[1]*(x+1)*bOw) #This is the cell this move will direct the piece towards
                    if self.important == False or theCellIAmMovingTo not in dangerousCells:
                        if move[3] < 3 and move[3] != 2: #IDs 0, 1, and 2
                            if theCellIAmMovingTo.piece == None:  
                                self.listOfMoves.append([move[0]*(x+1), move[1]*(x+1)*bOw, move[3]])
                            else:
                                self.listOfMoves.append([move[0]*(x+1), move[1]*(x+1)*bOw, move[3]])
                                print("Someones fat ass is in the way")
                                break

                        elif move[3] == 3: #ID 3 first turn
                            if self.moveCounter < 1 and (theCellIAmMovingTo.piece == None):
                                self.listOfMoves.append([move[0]*(x+1), move[1]*bOw*(x+1), 0])
                            else:
                                print("Someones fat ass is in the way")
                                break

                        elif move[3] == 4: # ID 4, the checkers piece uses this
                            if theCellIAmMovingTo.piece != None: # If there is a piece on the cell I am moving to
                                if -1 < self.cell.x + move[0]*(x+2) < self.board.w and -1 < self.cell.y + move[1]*(x+2)*bOw < self.board.h: # Doing a second check the the move is in domain
                                    self.listOfMoves.append([move[0]*(x+2), move[1]*(x+2)*bOw, move[3], move[0]*(x+1), move[1]*(x+1)*bOw]) #If so, add this move and the kill move as a valid move
                                    if theCellIAmMovingTo.piece.color != self.color: #If piece on this moves tile is on the opposite color, add an NBT to the cell to KILL this piece
                                        self.board.get_cell(self.cell.x + move[0]*(x+2), self.cell.y + move[1]*(x+2)*bOw).NBT = ["killMyPiece", self.cell.x + move[0]*(x+1), self.cell.y + move[1]*(x+1)*bOw]
                                        print("Someones fat ass is in the way")
                                    break
                                print("Too far")
                            
                    elif move[3] == 5 and inDanger == False: #ID 5: Castling [x, y, distance, ID, [[Rel x, Rel y of the pieces], [New rel x and rel y]]]
                        swappingCell = self.board.get_cell(self.cell.x + move[4][0][0], self.cell.y + move[4][0][1])
                        if swappingCell != None and swappingCell.piece != None: #If I and the piece I am moving are on the first move
                            if self.moveCounter == 0 and swappingCell.piece.moveCounter == 0: #If I and the piece I am moving are on the first move
                                if theCellIAmMovingTo.piece == None and self.board.get_cell(self.cell.x + move[4][1][0], self.cell.y + move[4][1][1]).piece == None:
                                    self.listOfMoves.append([move[0]*(x+1), move[1]*bOw*(x+1), 0])
                                    theCellIAmMovingTo.NBT = ["Swapsies", self.cell.x + move[4][0][0], self.cell.y + move[4][0][1], self.cell.x + move[4][1][0], self.cell.y + move[4][1][1]]
                else:
                    print("Out of domain")
                    break
    
    def transition(self): #Promotion, will add a selection screen soon. Should probably add a thing for initialisation
        self.pieceType = "queen"
        self.basicMoves = [[1, 1, 8, 1],[1, -1, 8, 1],[-1, -1, 8, 1],[-1, 1, 8, 1], [0, 1, 8, 1],[0, -1, 8, 1],[-1, 0, 8, 1],[1, 0, 8, 1]]
        self.sprite_name = f"{'white' if self.color else 'black'}{self.pieceType}.png"
        self.sprite = py.image.load("Assets/"+self.sprite_name)          
        print("Estrogen Unlocked")

    def validateMoves(self):
        validCells = [] #[Cell, Dangerous NOW, piece, Dangerous FUTURE]
        for move in self.listOfMoves:
            
            currentCell = self.board.get_cell(self.cell.x + move[0], self.cell.y + move[1])
            
            if currentCell.piece == None and (move[2] == 0 or move[2] == 1 or move[2] == 3 or move[2] == 5):
                if move[2] == 1: validCells.append([currentCell, False, self, True]) #No kill move
                else: validCells.append([currentCell, False, self, False])
            
            elif move[2] == 4:
                if currentCell.piece == None:
                    validCells.append([currentCell, False, self, False]) #No kill move
                    if self.board.get_cell(self.cell.x + move[3], self.cell.y + move[4]).piece.color != self.color:
                        validCells.append([currentCell, True, self, False]) #Kill move
                
            elif currentCell.piece == None and move[2] == 2:
                validCells.append([currentCell, False, self, True])
                print(f"{move} Nothing to capture No move")
                
            elif currentCell.piece.color != self.color and move[2] != 0:
                print(f"{move} Kill Move")
                validCells.append([currentCell, True, self, False])
            else:
                print(f"{move} No Kill No move")
        return validCells
    
    def colorInMoves(self):
        for cell in self.validateMoves():
            if cell[1] == True and cell[2] == self:
                cell[0].validMove = True 
                cell[0].color = cRed
            elif cell[2] == self:
                cell[0].validMove = True 
                cell[0].color = cBlue
        
    def move(self, newCell):
        self.lastPosition = [self.cell.x, self.cell.y]

        self.moveCounter += 1
        self.cell = newCell
        
        if self.pieceType == "pawn" and self.color == False and self.cell.y == 7:
            self.transition()
        
        if self.pieceType == "pawn" and self.color == True and self.cell.y == 0:
            self.transition()           

class Cell: #Class to hold basic info about the board (color, piece id, pos). Each cell is just a square on the board
    signal = Signal()
    def __init__(self, x, y, piece):
        self.x = x
        self.y = y
        self.primaryColor = "#000000"
        self.color = "#000000"
        self.piece = piece
        self.validMove = False
        self.NBT = None
        
        if (x + y)%2:
            self.primaryColor = cGreen
            self.color = cGreen
        else:
            self.primaryColor = cWhite
            self.color = cWhite

        Cell.signal.connect(self.reset_NBT)
            
    def changeColor(self, color):
        self.color = color
    
    def reset(self):
        self.color = self.primaryColor
        self.validMove = False
        
    def get_position(self):
        return self.x, self.y
    
    def reset_NBT(self):
        self.NBT = None    
    
    @staticmethod
    def reset_all_NBT():
        # Emit the signal to reset NBT for all subscribed Cell objects
        Cell.signal.emit()

class Table: #Class of the data part of the game, hold all the positions
    def __init__(self, height, width):
        self.h = height
        self.w = width
        
        self.lastMoveCell1 = None
        self.lastMoveCell2 = None

        self.livingPieces = []

        self.dangerousCells = []

        self.table = []

        for y in range(height):
            widthList = []
            for x in range(width):
                widthList.append(Cell(x, y, None))
            self.table.append(widthList)
            
    def updateCellColor(self):
        if self.lastMoveCell1 != None and self.lastMoveCell2 != None:
            if self.lastMoveCell2.color != cRed:
                self.lastMoveCell2.color = cOrange
            if self.lastMoveCell1.color != cRed:
                self.lastMoveCell1.color = cOrange
        for cell in self.dangerousCells:
            if cell.piece.important:
                cell.color = cRed


    def print(self):
        for row in self.table:
            print([f"({cell.x},{cell.y})" for cell in row])
            
    def getPieceID(self, x, y):
        print(self.table[y][x].piece)
        
    def get_cell(self, x, y): # Get the cell at a specified position
        if x <= self.w-1 and  y <= self.h-1:
            return self.table[y][x]
        else:
            return None
    
    def genDangerousCells(self, dangerousCells):
        for piece in self.livingPieces:
            piece.genMoves(dangerousCells)
            for move in piece.validateMoves():
                if move[1] == True or move[3] == True: #If the cell is deadly
                    dangerousCells.append(move[0])
    
    def resetBoard(self):
        for row in self.table:
            for cell in row:
                cell.reset()
        
class Display:  # Displays the game
    def __init__(self, board, square_size, color1, color2):
        self.board = board
        self.square_size = square_size
        self.color1 = color1
        self.color2 = color2
        self.screen_width = board.w * square_size
        self.screen_height = board.h * square_size
        py.init()
        self.screen = py.display.set_mode((self.screen_width + self.square_size/2, self.screen_height + self.square_size/2))  # Add extra space for labels
        self.font = py.font.SysFont('Arial', 20)  # Set the font and size for labels

    def draw_board(self):
        for y, row in enumerate(self.board.table):
            for x, cell in enumerate(row):
                # Adjust the rect position to account for the label space (40 pixels)
                rect = py.Rect(x * self.square_size , y * self.square_size, self.square_size, self.square_size)
                py.draw.rect(self.screen, averageColor(self.board.get_cell(x, y).color, self.board.get_cell(x, y).primaryColor), rect)
                
                if cell.piece is not None:
                    piece = cell.piece
                    piece_sprite = py.transform.scale(piece.sprite, (self.square_size, self.square_size))  # Scale sprite
                    self.screen.blit(piece_sprite, (x * self.square_size, y * self.square_size))  # Adjust position for labels

    def draw_labels(self):
        # Draw the letters (A-H or wider) at the bottom
        for x in range(self.board.w):
            letter = chr(65 + x)  # Convert 0 -> 'A', 1 -> 'B', etc.
            label = self.font.render(letter, True, (255, 255, 255))  # White text for labels
            # Position the label centered below the respective column
            self.screen.blit(label, (x * self.square_size + self.square_size // 2 - 10, self.board.h * self.square_size))

        # Draw the numbers (1-8 or more) along the left side
        for y in range(self.board.h):
            number = str(self.board.h - y)  # Reverse order, top = 8, bottom = 1 for standard boards
            label = self.font.render(number, True, (255, 255, 255))  # White text for labels
            # Position the label centered on the left of the respective row
            self.screen.blit(label, (x * self.square_size + self.square_size // 2 - 10 + self.square_size*0.9, y * self.square_size + self.square_size // 2 - 10))

    def run(self, board):
        self.screen.fill((0, 0, 0))  # Fill the screen with a black background
        self.draw_board()  # Draw the board with pieces
        self.draw_labels()  # Draw the row and column labels
        py.display.flip()  # Update the screen

    def quit(self):
        py.quit()
