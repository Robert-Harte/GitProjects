#!/usr/bin/env python3

import random

class TicTakToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]     # a single list to rep a 3x3 square. The _ just indicates there's no condition to meet in the for loop

    # Method to print the board
    def print_board(self):
        # uses splicing to split the list up.
        # [i*3:(i+1)*3] is which group of 3 are we choosing. Uses splicing to split into chunks. e.g. 0*3 = 0, (0+1)*3 = 3. So becomes [0:3], which are indexes 0,1,2.
        # then i = 1, e.g. 1*3 = 3, (1+1)*3 = 6. So becomes [3:6], which are indexes 3,4,5.
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:    
            print("| " + " | ".join(row) + " |")
    
    @staticmethod       # static method as it does not require any information from the class instance.
    def print_board_nums():
        # uses splicing to split the list up.
        # Assign number variables to each square. Similar to the above logic, but has an additional. This is because this only printing a generic static board each time.
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def moves(self, square, letter):
        # Apply move to board
        # First: check if that move is valid
        # Second: Update board to include new move.
        # Third: check if winning move. 
        if self.board[square] == " ":
            self.board[square] = letter
            return True
        else:
            print("Invalid move! Select another square.")
        return False
    
    # Return true if there are moves available.
    def available_moves(self):
        if " " in self.board:
            return True
        return False
        
    # Check if the last move was the winning move.
    def winning_move(self, square, letter):
        # Row:
        row_num = square // 3   # how many times does 3 go into square. e.g. if square = 4, then it is row 1 (middle row) 
        row = self.board[row_num * 3: (row_num + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        col_num = square % 3    # divide by 3 and take left over
        col = [self.board[col_num + i * 3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True
        
        # check diagonals
        # only need to check (0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # left to right diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False

  
def main():
    game = TicTakToe()
    game.print_board_nums()
    turn = random.choice(["x", "o"])
    
    # Keep looping until the game ends
    while True:
        try:
            square = int(input(f"It is player {turn} turns. Please enter a square number: "))
            if game.moves(square,turn): # Make a move
                game.print_board()
                if game.winning_move(square, turn): # Check if the game has been won after the move.
                    print(f"Congratz! Player {turn} has won!")
                    break
                # switch player        
                if turn == "x":
                    turn = "o"
                else:
                    turn = "x"
                
                if not game.available_moves():
                    print("Game over, no one wins.")
                    break   
                
        except (ValueError, IndexError):
            print("Invalid position! Please choose a number between 0-8 which has not yet been selected.")
            
    
if __name__ == "__main__":
    main()