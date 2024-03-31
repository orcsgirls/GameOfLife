#-----------------------------------------------------------------------------------
# FINAL: The Game of Life - Model, View, Controller coding pattern
#-----------------------------------------------------------------------------------
import pygame

from model import Model
from view import View
from controller import Controller

FPS = 12
MODEL_SIZE = (75, 50)
CELL_SIZE = 10

def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    model = Model(MODEL_SIZE)
    view = View(model, CELL_SIZE)
    controller = Controller(model, view, FPS)

    while True:
        
        controller.handle_events()
        model.update()
        view.draw()
        
        pygame.display.update()
        clock.tick(controller.fps)

if __name__ == "__main__":
    main()
