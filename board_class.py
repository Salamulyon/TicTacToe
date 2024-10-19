"""
initializing the TicTacToe Board. making the length of the board variable 
so that the board space can always be increased
"""
from constants import BOARD_LENGTH

class Board:
    def __init__(self) -> None:
        self.board_space: int = BOARD_LENGTH * BOARD_LENGTH
        self.placeholder = " "
        self.board_array: list[str] = [self.placeholder for _ in range(self.board_space)]

    def write_to_board(self,character: str,
                       position: int):
        if self.board_array[position] == self.placeholder:
            self.board_array[position] = character
        else:
            print('Location Already taken')
        
    def return_dynamic_board(self):
        disp_board = ''
        horizontal_lines = '--' * BOARD_LENGTH
        #disp_board += '|'
        disp_board += self.board_array[0]
        for n in range(1,self.board_space):
            disp_board += '|'
            if n % BOARD_LENGTH != 0:
                disp_board += self.board_array[n]
            else:
                disp_board += '\n'
                disp_board += horizontal_lines
                disp_board += '\n'
                disp_board += self.board_array[n]
        disp_board += '|'
        return disp_board


    def print_board(self):
        disp = self.return_dynamic_board()
        print(disp)
        