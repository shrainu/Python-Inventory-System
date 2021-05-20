import pygame as pg


class Grid:

    def __init__(self, pos, size, slot='null'):

        self.rect = pg.Rect((pos[0], pos[1]), (size, size))
        self.slot = slot
        self.occupied = False
        self.occupied_object = None
        self.spawner = False
    
    def draw(self, surface):

        pg.draw.rect(surface, (123, 50, 250), self.rect, 1)

    def set_occupied_object(self, object_given):

        if not self.occupied:
            self.occupied = True
            self.occupied_object = object_given
    
    def switch_occupied_object(self, object_given):
        self.occupied = True
        self.occupied_object = object_given
    
    def set_unoccupied(self):

        self.occupied = False
        self.occupied_object = None

