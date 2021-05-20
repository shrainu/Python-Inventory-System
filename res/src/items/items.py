import pygame as pg
from res.src.item import Item


class Sword(Item):

    SWORD_IMAGE = pg.image.load('res/assets/sword.png')

    def __init__(self, pos):
        Item.__init__(self, pos, Sword.SWORD_IMAGE, True, "weapon", [0, 0, 15])


class Gloves(Item):

    GLOVES_IMAGE = pg.image.load('res/assets/gloves.png')

    def __init__(self, pos):
        Item.__init__(self, pos, Gloves.GLOVES_IMAGE, True, "weapon", [5, 5, 5])


class Helmet(Item):

    HELMET_IMAGE = pg.image.load('res/assets/helmet.png')

    def __init__(self, pos):
        Item.__init__(self, pos, Helmet.HELMET_IMAGE, True, "head", [15, 15, 0])


class Chestplate(Item):

    CHESTPLATE_IMAGE = pg.image.load('res/assets/chestplate.png')

    def __init__(self, pos):
        Item.__init__(self, pos, Chestplate.CHESTPLATE_IMAGE, True, "body", [10, 25, 0])
    

class Leggings(Item):

    LEGGINGS_IMAGE = pg.image.load('res/assets/leggings.png')

    def __init__(self, pos):
        Item.__init__(self, pos, Leggings.LEGGINGS_IMAGE, True, "leggings", [10, 10, 0])


class Boots(Item):

    BOOTS_IMAGE = pg.image.load('res/assets/boots.png')

    def __init__(self, pos):
        Item.__init__(self, pos, Boots.BOOTS_IMAGE, True, "boots", [5, 10, 0])

