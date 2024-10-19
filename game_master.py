from random import choice
from constants import BOARD_LENGTH
from baseplayer import BasePlayer
from board_class import Board



class GameMaster():

    def __init__(self,
                 player1: BasePlayer,
                 player2: BasePlayer,
                 board: Board) -> None:
        self.player_1 = player1
        self.player_2 = player2
        self.board = board


    def alloc_char_to_player(self):
        characters = ['X','O']
        self.first_player = choice([self.player_1,self.player_2])
        self.first_player.character = choice(characters)
        self.first_player.id = 0
        self.first_player.name = 'First Player'

        if self.first_player == self.player_1:
            self.second_player = self.player_2 
            self.second_player.name = 'Second Player'    
        else:
            self.second_player = self.player_1
            self.second_player.name = 'Second Player'

        self.second_player.id = 1
        if self.first_player.character == 'X':
            self.second_player.character = 'O'
        else:
            self.second_player.character = 'X'


        return self.first_player
    
    def switch_curr_player(self,
                         curr_player: BasePlayer):
        if curr_player == self.first_player:
            curr_player = self.second_player
            return curr_player
        else:
            curr_player = self.first_player
            return curr_player

    def _check_diagonally(self,
                          symbol: str):
            """
            since it's only checking diagonally,the only way to win is to have
            a diagonal running the full length of the board so it only checks diagonally
            from the first position and the last position on the first row
            """
            if self.board.board_array[0] == symbol:
                spaces = [num for num in range(BOARD_LENGTH + 1,
                                               BOARD_LENGTH*BOARD_LENGTH,
                                               BOARD_LENGTH + 1)] #this makes it so that the values in the list are diagonal from this position
                for space in spaces:
                    if self.board.board_array[space] != symbol:
                        return False
                return True
            if self.board.board_array[BOARD_LENGTH - 1] == symbol:
                spaces = [num for num in range(BOARD_LENGTH - 1,
                                               (BOARD_LENGTH*(BOARD_LENGTH - 1) + 1),
                                               BOARD_LENGTH - 1)]#this makes it so that the values in the list are diagonal from this position
                for space in spaces:
                    if self.board.board_array[space] != symbol:
                        return False
                return True
            
            return False

    def _check_lengthwise(self,
                          symbol: str):
        """
        checks lengthwise for matching symbols i.e left to right
        """
        spaces = [num for num in range(0,
                                       (BOARD_LENGTH*(BOARD_LENGTH-1) + 1),
                                       BOARD_LENGTH)] #spaces to check to see if there's a match horizontally
        for space in spaces:
            if self.board.board_array[space] == symbol:
                for count in range(0,
                                (BOARD_LENGTH),
                                1):
                    if self.board.board_array[count + space] != symbol:
                        return False
                    continue
                return True

        

    def _check_up_down(self,
                       symbol: str):
        """
        checks vertically to see if there are matching symbols.
        checks from only the top row down each column
        """
        spaces = [num for num in range(0,
                                       BOARD_LENGTH,
                                       1)]
        for space in spaces:
            if self.board.board_array[space] == symbol:
                for count in range(0,
                                    (BOARD_LENGTH*(BOARD_LENGTH-1) + 1),
                                    BOARD_LENGTH):
                    if self.board.board_array[space + count] !=  symbol:
                        return False
                    continue
                return True


    def check_if_player_wins(self,
                             curr_player:BasePlayer):
        diagonal = self._check_diagonally(curr_player.character)
        up_down = self._check_up_down(curr_player.character)
        length_wise = self._check_lengthwise(curr_player.character)

        winner = diagonal or up_down or length_wise

        if winner:
            print(f'{curr_player.name} {curr_player.character} wins!!')
            return winner
            

        

