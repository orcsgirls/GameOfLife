#-------------------------------------------------------------------------
# MODEL: The model is the simulation itself
#-------------------------------------------------------------------------

import tkinter
import tkinter.filedialog
import random
from PIL import Image
from numpy import asarray

class Model:

    def __init__(self, simulation_size):
        self.rows = simulation_size[1]
        self.columns = simulation_size[0]
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.cells_temp = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.gen_alive = [[0 for _ in range(self.columns)] for _ in range(self.rows)]   
        self.run = False
        self.generation = 0
        self.alive_cells = 0

    def count_live_neighbors(self, row, column):
        live_neighbors = 0

        neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for offset in neighbor_offsets:
            new_row = (row + offset[0]) % self.rows
            new_column = (column + offset[1]) % self.columns
            if self.cells[new_row][new_column] == 1:
                live_neighbors += 1

        return live_neighbors

    def update(self):
        if self.is_running():
            for row in range(self.rows):
                for column in range(self.columns):
                    live_neighbors = self.count_live_neighbors(row, column)
                    cell_value = self.cells[row][column]

                    if cell_value == 1:
                        if live_neighbors > 3 or live_neighbors < 2:
                            self.cells_temp[row][column] = 0
                            self.gen_alive[row][column] = 0
                        else:
                            self.cells_temp[row][column] = 1
                            self.gen_alive[row][column] += 1
                    else:
                        if live_neighbors == 3:
                            self.cells_temp[row][column] = 1
                        else:
                            self.cells_temp[row][column] = 0

            for row in range(self.rows):
                for column in range(self.columns):
                    self.cells[row][column] = self.cells_temp[row][column]
                    
            self.generation += 1
            self.alive_cells = self.get_alive_cells()
            
    def get_alive_cells(self):
        alive = 0
        for row in range(self.rows):
                for column in range(self.columns):
                    alive += self.cells[row][column]     
        return alive
    
    def is_running(self):
        return self.run

    def start(self):
        self.run = True

    def stop(self):
        self.run = False
        
    def step(self):
        if self.is_running() == False:
            self.run = True
            self.update()
            self.run = False
            
    def clear(self):
        if self.is_running() == False:
            self._clear()
            self.generation = 0

    def create_random_state(self):
        if self.is_running() == False:
            self._clear()
            self.generation = 0
            for row in range(self.rows):
                for column in range(self.columns):
                    self.cells[row][column] = random.choice([1, 0, 0, 0])

    def create_from_image(self, file=''):
        if self.is_running() == False:
            self._clear()
            self.generation = 0
            self._fill_image(file)
            
    def toggle_cell(self, row, column):
        if self.is_running() == False:
            if 0 <= row < self.rows and 0 <= column < self.columns:
                self.cells[row][column] = not self.cells[row][column]
                self.gen_alive[row][column] = 0   
                
    # Private methods
    
    def _fill_image(self, file=None):
        filename = self._prompt_file() if not file else file
        if filename:
            image = Image.open(filename).resize((self.columns, self.rows))
            fn = lambda x : 1 if x > 128 else 0
            data = asarray(image.convert("L").point(fn, mode='1'))
            for row in range(self.rows):
                for column in range(self.columns):
                    self.cells[row][column] = data[row][column]
                
    def _prompt_file(self):
        top = tkinter.Tk()
        top.withdraw()
        file_name = tkinter.filedialog.askopenfilename(parent=top)
        top.destroy()
        return file_name
        
    def _clear(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = 0
                self.gen_alive[row][column] = 0
