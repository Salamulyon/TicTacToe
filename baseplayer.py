from dataclasses import dataclass


class BasePlayer:
    id: int = 0
    character: str = ''

    def pick_board_space():
        raise NotImplementedError('This function needs to be overwritten')
