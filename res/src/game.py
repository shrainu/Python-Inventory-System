import sys
import pygame as pg
# Initialize Scripts
from res.src.tilemap import Tilemap
from res.src.items import items
from res.src.ui_handler import UIHandler
from res.src.player import Player
from res.src.item_spawner import ItemSpawner


class Game:

    def __init__(self, screen, clock):

        # Pygame components
        self.clock = clock
        self.screen = screen
        self.event_list = None
        self.WIDTH, self.HEIGHT = self.screen.get_size()

        # Set tilemap
        self.tilemaps = []
        self.inventory_tilemap = Tilemap((40, 40), (10, 10), 40, (5, 5))
        self.armor_tilemap = Tilemap((560, 40), (1, 4), 40, (0, 20), 'armor')
        self.weapon_tilemap = Tilemap((640, 40), (1, 2), 40, (0, 20), 'weapon')
        self.spawner_tilemap = Tilemap((40, 560), (5, 1), 40, (61, 0))
        # Append tilemaps to tilemaps list
        self.tilemaps.append(self.inventory_tilemap)
        self.tilemaps.append(self.armor_tilemap)
        self.tilemaps.append(self.weapon_tilemap)
        self.tilemaps.append(self.spawner_tilemap)

        # Items
        self.items = []

        # Item spawners
        self.item_spawners = []
        self._spawner_types = ['weapon', 'head', 'body', 'leggings', 'boots']
        # Set the Item spawners
        for i in range(len(self.spawner_tilemap.grids)):
            self.temp = ItemSpawner(self.spawner_tilemap.grids[i].rect.center, self.tilemaps, self._spawner_types[i])
            self.item_spawners.append(self.temp)

        # Player
        self.player = Player()

        # UI Handler
        self.ui_handler = UIHandler(self.items, self.player)

    def run(self):

        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):

        # Update the eventlist
        self.event_list = pg.event.get()

        # Check events
        for event in self.event_list:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def update(self):
        
        # UI Handler
        self.ui_handler.update(self.event_list, self.tilemaps)

        # Item Spawners
        for item_spawner in self.item_spawners:
            item_spawner.spawn_items(self.items)

    def draw(self):

        self.screen.fill((0, 0, 0))

        # Draw tilemaps
        for tilemap in self.tilemaps:
            tilemap.draw_tilemap(self.screen)
            tilemap.draw_borders(self.screen, 5)

        # Draw items
        for item in self.items:
            item.draw(self.screen)
        
        # Draw player stats
        self.player.draw_stats(self.screen)

        pg.display.flip()

