import pygame as pg


class Item:

    def __init__(self, pos, image, equipable, slot='null', stats=[0, 0, 0]):

        self.slot = slot
        self.image = image
        self.last_grid = [None, (pos[0], pos[1])]
        self.equipable = False
        self.rect = pg.Rect((pos[0], pos[1]), (40, 40))

        # Stats of the item
        self.armor = stats[0]
        self.health = stats[1]
        self.attack = stats[2]

    def drag(self):

        # Move items position to mouse position
        self.rect.x, self.rect.y = pg.mouse.get_pos()
    
    def drop(self, tilemaps):

        # Lock to the grid under the mouse
        for tilemap in tilemaps:
            for grid in tilemap.grids:
                if grid.rect.x < self.rect.x < grid.rect.x + grid.rect.width:
                    if grid.rect.y < self.rect.y < grid.rect.y + grid.rect.height and not grid.occupied:
                        if grid.slot == self.slot or grid.slot == 'null':

                            # Set the items position to fit the grid
                            self.rect.x, self.rect.y = grid.rect.x, grid.rect.y

                            # Set the last occupied grid to non-occupied
                            if self.last_grid[0] is not None: 
                                self.last_grid[0].set_unoccupied()

                            # Set the current grid to occupied grid
                            self.last_grid = [grid, (grid.rect.x, grid.rect.y)]

                            # Set the current occupied grids status to occupied
                            grid.set_occupied_object(self)

                            return
                    elif grid.rect.y < self.rect.y < grid.rect.y + grid.rect.height and grid.occupied and self.last_grid[0] is not None and not self.last_grid[0].spawner and  not grid.spawner:
                        if (grid.occupied_object.slot == self.slot) or (grid.slot == 'null' and self.last_grid[0].slot == 'null'):

                            # Temporary variables
                            self.past_var = self.last_grid

                            # Set the items position to fit the grid
                            self.rect.x, self.rect.y = grid.rect.x, grid.rect.y
                            self.last_grid = [grid, (grid.rect.x, grid.rect.y)]

                            # Set the switched items position and last_grid variables
                            grid.occupied_object.last_grid[0] = self.past_var[0]
                            grid.occupied_object.rect.x, grid.occupied_object.rect.y = self.past_var[1][0], self.past_var[1][1]
                            # Set the the pas occcupied grids status to be occupied by the switched item
                            self.past_var[0].switch_occupied_object(grid.occupied_object)

                            # Set the current occupied grids status to occupied
                            grid.switch_occupied_object(self)

                            return
        
        # If didn't place above a grid
        self.rect.x, self.rect.y = self.last_grid[1]
            

    def draw(self, surface):
        surface.blit(self.image, self.rect)

