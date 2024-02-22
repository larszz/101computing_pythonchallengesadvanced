from Game import Game
from Coordinate import Coordinate
from Pieces import *



if __name__ == '__main__':
    game = Game()
    coor = game.grid.get_field_coordinates()
    print(game.fancy_output())
