# -*- coding: utf-8 -*-
import random

class MapGenerator():
    def __init__(self):
        self.length = 0
        self.width = 0
        self.grid = []
        # Need to add island, continents, ocean, etc., tiles in the symbols
        self.symbols = {0:{'name':'tree', 'icon': '^'},
                        1: {'name': 'water', 'icon': '~'},
                        2: {'name':'land', 'icon': '_'},
                        3: {'name':'houses', 'icon': '#'},
                        4: {'name':'snow', 'icon': '*'}}
    
    def map_initialize(self, length, width):
        ''' Generates a list of lists, that represents a grid, that 
        will act as a base map.
        
        length is the number of nested lists (rows).
        Width is the number of tiles in every nested list (columns).
        '''
        self.length = length
        self.width = width
        icon_random = random.randint(0,len(self.symbols)-1)
        for number in range(self.width):
            self.grid.append([self.symbols[icon_random]['icon'] for num in range(self.length)])
          
    def alive_dead_tiles(self):
        for row_index, row in enumerate(self.grid):
            for tile_index, tile in enumerate(row):
                rando = random.randint(0,2)
                if rando == 2:
                    self.grid[row_index][tile_index] = random.randint(0,1)
                else:
                    pass

    def tile_conversion(self):
        for row_index, row in enumerate(self.grid):
            for col_index, tile in enumerate(row):
                if tile == 1:
                    symbol_access = random.randint(0, len(self.symbols)-1)
                    tile_replacement = self.symbols[symbol_access]['icon']
                    self.grid[row_index][col_index] = tile_replacement
                          
              
    def print_map(self):
        for row in self.grid:
            x = ''
            for tile in row:
                x += str(tile)
            print(x)
        
    def br(self):
        '''
        This is a biased run. It counts the total number of neighbors that a dead
        tile from a grid has, and then uses percentages to turn it into a live
        tile. Neighbors that are more numerous have a greater influence than 
        less numerous tiles.
        '''
        for row_index, row in enumerate(self.grid):
            # row_index is the index of the sublist, and row is the list itself.
            for tile_index, tile in enumerate(row):
                if tile == 0:
                    # tile_index is the index of each tile.
                    min_value = max(0, tile_index - 1)
                    max_value = tile_index + 1
                    if row_index != 0:
                        top_row = self.grid[row_index - 1][min_value:max_value + 1]
                    else:
                        # Top row tiles do not have a top row.
                        top_row = []
                    
                    sides = self.grid[row_index][min_value:max_value + 1]
        
                    if row_index == len(self.grid) -1:
                        # bottom row tiles do not have a bottom row.
                        bot_row = []
                    else:
                        bot_row = self.grid[row_index + 1][min_value:max_value + 1]
                        
        
                    neighbors = top_row+bot_row+sides
                    # a combination of all of the neighbors into one list.
                    
                    symbol_count = {'^': 0,
                            '*': 0,
                            '~':  0,
                            '#': 0,
                            '_': 0,
                            '@': 0}

                    for neighbor in neighbors:
                        if neighbor == 0:
                            pass
                        else:
                            symbol_count[neighbor] += 1    

                    bucket = ['_'] # Starts off with land to keep from having an error with an empty bucket.
                    unused_tiles = ['_']
                    # The bucket is used to turn the a dead tile into a map tile based off
                    # of its neighbors. A random integer will be generated to index 
                    # the bucket. The more a tile appears in the bucket, the more
                    # likely it will be chosen.
                    for icon, count in symbol_count.items():
                        if count != 0:
                            for num in range(0, count):
                                bucket.append(icon)
                        else:
                            unused_tiles.append(icon)
                    
                    # alive tile will have a 1 in 500 chance of being an unused tile
                    decider = random.randint(0,500)
                    if decider == 1:
                        alive_tile = unused_tiles[random.randint(0,len(unused_tiles)-1)]
                    else:
                        alive_tile = bucket[random.randint(0,len(bucket)-1)]
                    self.grid[row_index][tile_index] = alive_tile
    
                else:
                    pass
    
    def build_biome(self, b_length, b_height):
        icon_random = random.randint(0,len(self.symbols)-1)
        biome = [[self.symbols[icon_random]['icon'] for number in range(b_length)] for number in range(b_height)]
        return biome
        
        
    def biome_injector(self):
        grid_xsize = len(self.grid[0])
        grid_ysize = len(self.grid)
        
        bio_col = random.randint(1,grid_xsize)
        bio_row = random.randint(1,grid_ysize)
        biome = self.build_biome(bio_col, bio_row)
        
        
        biome_xsize = len(biome[0])
        #biome_ysize = len(biome)
        
        x_limit = len(self.grid[0]) - len(biome[0])
        y_limit = len(self.grid) - len(biome)
       
        # The top left corner is where the biome injection will start.
        # start by generating random starting points and see if they ever go
        # out of target:
        
        x_insert = random.randint(0,x_limit)
        y_insert = random.randint(0,y_limit)
    
        
        #insert_coordinate = (x_insert, y_insert)
        last_row_index = y_insert + len(biome) - 1
        last_col_index = x_insert + biome_xsize
        
    
        # insert the biome randomly in the grid (which will be the entire map.)
        count = 0
        for row_index, row in enumerate(self.grid):
            if row_index in range(y_insert,last_row_index + 1):
                self.grid[row_index][x_insert:last_col_index] = biome[count][:]
                count += 1


    # also tricky. the river will run a cardinal direction, and when inserting into the grid, will only insert the water tiles '~'.
    pass

x = MapGenerator()
x.map_initialize(100,100)
x.print_map()
print('\n')
x.alive_dead_tiles()
x.tile_conversion()
x.br()
x.print_map()
x.biome_injector()
print('\n')
x.print_map()
print('End')
