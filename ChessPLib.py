import pygame as py

# Color Palletes:
cGreen = "#005c32"
cWhite = "#f7eaad"
cRed = "#bf6790"
cBlue = "#567696"

class Piece:
    def __init__(self, pieceType, board, position, basicMoves, color): # Format [x displacement, y displacement, distance, capture] eg. Rook [[0,1,1,1],[1,0,1,1],[0,-1,1,1],[-1,0,1,1]]; Color is a bool
        self.cell = board.get_cell(position[0], position[1])
        self.basicMoves = basicMoves
        self.board = board
        self.listOfMoves = []
        self.color = color
        self.pieceType = pieceType
        self.moveCounter = 0
        
        self.sprite_name = f"{'white' if self.color else 'black'}{self.pieceType}.png"
        self.sprite = py.image.load("Assets/"+self.sprite_name)
        
        print(f"{self.sprite_name} Initialised")
        
        self.cell.piece = self
                
    def genMoves(self):
        self.listOfMoves = []
        bOw = 1 if self.color else -1
        for move in self.basicMoves:

            for x in range(move[2]): #How many tiles should the movement go
                if -1 < self.cell.x + move[0]*(x+1) < self.board.w and -1 < self.cell.y + move[1]*(x+1)*bOw < self.board.h:
                    if move[3] != 3:
                        if self.board.get_cell(self.cell.x + move[0]*(x+1), self.cell.y + move[1]*(x+1)*bOw).piece == None:  
                            self.listOfMoves.append([move[0]*(x+1), move[1]*(x+1)*bOw, move[3]])

                        else:
                            self.listOfMoves.append([move[0]*(x+1), move[1]*(x+1)*bOw, move[3]])
                            print("Someones fat ass is in the way")
                            break
                    else:
                        if self.moveCounter < 1 and (self.board.get_cell(self.cell.x + move[0]*(x+1), self.cell.y + move[1]*(x+1)*bOw).piece == None):
                            self.listOfMoves.append([move[0]*(x+1), move[1]*bOw*(x+1), 0])
                        else:
                            print("Someones fat ass is in the way")
                            break
                    
                else:
                    print("Out of domain")
                    break
    
    def transition(self):
        self.pieceType = "queen"
        self.basicMoves = [[1, 1, 8, 1],[1, -1, 8, 1],[-1, -1, 8, 1],[-1, 1, 8, 1], [0, 1, 8, 1],[0, -1, 8, 1],[-1, 0, 8, 1],[1, 0, 8, 1]]
        self.sprite_name = f"{'white' if self.color else 'black'}{self.pieceType}.png"
        self.sprite = py.image.load("Assets/"+self.sprite_name)          
        print("Estrogen Unlocked")

    def colorInMoves(self):
        for move in self.listOfMoves:
            print(move)
            if self.board.get_cell(self.cell.x + move[0], self.cell.y + move[1]).piece == None and move[2] != 2:
                self.board.get_cell(self.cell.x + move[0], self.cell.y + move[1]).color = cBlue
                self.board.get_cell(self.cell.x + move[0], self.cell.y + move[1]).validMove = True
                
            elif self.board.get_cell(self.cell.x + move[0], self.cell.y + move[1]).piece == None and move[2] == 2:
                self.board.get_cell(self.cell.x + move[0], self.cell.y + move[1]).color = self.board.get_cell(self.cell.x + move[0], self.cell.y + move[1]).primaryColor
                
            elif self.board.get_cell(self.cell.x + move[0], self.cell.y + move[1]).piece.color != self.color and move[2] != 0:
                self.board.get_cell(self.cell.x + move[0], self.cell.y + move[1]).color = cRed
                self.board.get_cell(self.cell.x + move[0], self.cell.y + move[1]).validMove = True
                
            else:
                self.board.get_cell(self.cell.x + move[0], self.cell.y + move[1]).color = self.board.get_cell(self.cell.x + move[0], self.cell.y + move[1]).primaryColor
    
    def move(self, newCell):
        self.moveCounter += 1
        self.cell = newCell
        
        if self.pieceType == "pawn" and self.color == False and self.cell.y == 7:
            self.transition()
        
        if self.pieceType == "pawn" and self.color == True and self.cell.y == 0:
            self.transition()
            
        
            

class Cell: #Class to hold basic info about the board (color, piece id, pos). Each cell is just a square on the board
    def __init__(self, x, y, piece):
        self.x = x
        self.y = y
        self.primaryColor = "#000000"
        self.color = "#000000"
        self.piece = piece
        self.validMove = False
        
        if (x + y)%2:
            self.primaryColor = cGreen
            self.color = cGreen
        else:
            self.primaryColor = cWhite
            self.color = cWhite
            
    def changeColor(self, color):
        self.color = color
    
    def reset(self):
        self.color = self.primaryColor
        self.validMove = False
        
    
    def get_position(self):
        return self.x, self.y

class Table: #Class of the data part of the game, hold all the positions
    def __init__(self, height, width):
        self.h = height
        self.w = width

        self.table = []

        for y in range(height):
            widthList = []
            for x in range(width):
                widthList.append(Cell(x, y, None))
            self.table.append(widthList)
            
    def print(self):
        for row in self.table:
            print([f"({cell.x},{cell.y})" for cell in row])
            
    def getPieceID(self, x, y):
        print(self.table[y][x].piece)
        
    def get_cell(self, x, y): # Get the cell at a specified position
        return self.table[y][x]
    
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
        self.screen = py.display.set_mode((self.screen_width + 40, self.screen_height + 40))  # Add extra space for labels
        self.font = py.font.SysFont('Arial', 20)  # Set the font and size for labels

    def draw_board(self):
        for y, row in enumerate(self.board.table):
            for x, cell in enumerate(row):
                # Adjust the rect position to account for the label space (40 pixels)
                rect = py.Rect(x * self.square_size , y * self.square_size, self.square_size, self.square_size)
                py.draw.rect(self.screen, self.board.get_cell(x, y).color, rect)
                
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
            self.screen.blit(label, (x * self.square_size + self.square_size // 2 - 10, self.board.h * self.square_size + 5))

        # Draw the numbers (1-8 or more) along the left side
        for y in range(self.board.h):
            number = str(self.board.h - y)  # Reverse order, top = 8, bottom = 1 for standard boards
            label = self.font.render(number, True, (255, 255, 255))  # White text for labels
            # Position the label centered on the left of the respective row
            self.screen.blit(label, (x * self.square_size + 60 + self.square_size // 2 - 10, y * self.square_size + self.square_size // 2 - 10))

    def run(self, board):
        self.screen.fill((0, 0, 0))  # Fill the screen with a black background
        self.draw_board()  # Draw the board with pieces
        self.draw_labels()  # Draw the row and column labels
        py.display.flip()  # Update the screen

    def quit(self):
        py.quit()


        