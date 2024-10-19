from board_class import Board
from game_master import GameMaster
from comp_player import CompPlayer
from player import Player


def main():
    p1 = Player()
    p2 = Player()
    game_board = Board()
    gm = GameMaster(p1,p2,game_board)
    curr_player = gm.alloc_char_to_player()
    game_board.print_board()
    
    is_winner = False
    while not is_winner:
        print(f"{curr_player.name}'s turn. Your character is {curr_player.character}")
        loc = curr_player.pick_board_space()
        game_board.write_to_board(curr_player.character,loc)
        game_board.print_board()
        is_winner = gm.check_if_player_wins(curr_player)
        curr_player = gm.switch_curr_player(curr_player)


if __name__ == "__main__":
    main()
