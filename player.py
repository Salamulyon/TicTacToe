from baseplayer import BasePlayer
from constants import BOARD_LENGTH

class Player(BasePlayer):
    
    def pick_board_space(self):
        loc = input("Please enter a location to place your marker :")
        try:
            loc = int(loc)
            if 0 <= loc <= (BOARD_LENGTH*BOARD_LENGTH) :
                return loc - 1
            else:
                print("Invalid Location. Value is out of range")
                self.pick_board_space()
        except ValueError:
            print("Invalid selection") 
            self.pick_board_space() 
    