#-------------------------------------------------------------------------
# VIEW: The class to visualize the model
#-------------------------------------------------------------------------

import pygame
from pygame.locals import *

class View:
    def __init__(self, model, cell_size):
        self.model = model
        self.cell_size = cell_size     
        
        self.background_color = pygame.Color((29,29,29))
        self.dead_color = pygame.Color((55,55,55))
        self.life_color = pygame.Color((0,255,0))
        self.life_color_hstart = 180
        self.life_color_saturation = 100
        self.life_color_luminescence  = 70    
        self.generation_view = False
        self.set_display() 
        
    def draw(self):
        self.window.fill(self.background_color) 
        for row in range(self.model.rows):
            for column in range(self.model.columns):
                hue = self.life_color_hstart+self.model.gen_alive[row][column]*10 if self.generation_view else self.life_color_hstart
                self.life_color.hsla=(hue, self.life_color_saturation, self.life_color_luminescence, 100)
                color = self.life_color if self.model.cells[row][column] else self.dead_color 
                pygame.draw.rect(self.window, color, (column * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))

        pygame.display.set_caption(f"Game of Life - Generation {self.model.generation} - Alive cells {self.model.alive_cells}")
        pygame.display.update()
    
    def set_display(self):
        window_width = self.model.columns * self.cell_size
        window_height = self.model.rows * self.cell_size      
        self.window = pygame.display.set_mode((window_width, window_height),RESIZABLE)
        pygame.display.set_caption("Game of Life")
    
    def resize(self, window_size):
        self.cell_size=min(window_size[1] // self.model.rows, 
                           window_size[0] // self.model.columns)
        self.set_display()
        
    def toggle_generation_view(self):
        self.generation_view =  not self.generation_view
        
    def increase_luminescence(self):
        if(self.life_color_luminescence < 95):
            self.life_color_luminescence += 5

    def decrease_luminescence(self):
        if(self.life_color_luminescence > 5):
            self.life_color_luminescence -= 5
            