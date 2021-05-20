import os
import json
import pygame as pg
# Import scripts
from res.src.game import Game


def main():

    running = True

    pg.init()
    WIDTH, HEIGHT = 960, 720
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Inventory System")
    clock = pg.time.Clock()

    game = Game(screen, clock)

    while running:
        
        game.run()


if __name__ == "__main__":
    main()

