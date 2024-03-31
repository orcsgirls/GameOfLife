import pygame, random
import tkinter
import tkinter.filedialog
from PIL import Image
from numpy import asarray

class Grid:
    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.gen_alive = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        
        self.dead_color = pygame.Color((55,55,55))
        self.life_color = pygame.Color((0,255,0))
        self.life_color_hstart = 180
        self.life_color_saturation = 100
        self.life_color_luminescence  = 80   
        
        self.generation_view = False
        
    def draw(self, window):
        for row in range(self.rows):
            for column in range(self.columns):
                hue = self.life_color_hstart+self.gen_alive[row][column]*10 if self.generation_view else self.life_color_hstart
                self.life_color.hsla=(hue, self.life_color_saturation, self.life_color_luminescence, 100)
                color = self.life_color if self.cells[row][column] else self.dead_color 
                pygame.draw.rect(window, color, (column * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))

    def fill_random(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = random.choice([1, 0, 0, 0])

    def fill_image(self, file=''):
        if file == "":
            file = self._prompt_file()
        print(f"Reading image from {file} ..")
        image = Image.open(file).resize((self.columns, self.rows))
        fn = lambda x : 1 if x > 128 else 0
        data = asarray(image.convert("L").point(fn, mode='1'))
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = data[row][column]
        
    def clear(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = 0
                self.gen_alive[row][column] = 0

    def toggle_cell(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.cells[row][column] = not self.cells[row][column]
            self.gen_alive[row][column] = 0
            
    def toggle_generation_view(self):
        self.generation_view =  not self.generation_view
        
    def increase_luminescence(self):
        if(self.life_color_luminescence < 95):
            self.life_color_luminescence += 5

    def decrease_luminescence(self):
        if(self.life_color_luminescence > 5):
            self.life_color_luminescence -= 5
            
    # Private methods
    
    def _prompt_file(self):
        top = tkinter.Tk()
        top.withdraw()  # hide window
        file_name = tkinter.filedialog.askopenfilename(parent=top)
        top.destroy()
        return file_name