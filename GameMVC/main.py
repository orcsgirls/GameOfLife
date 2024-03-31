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
    
    
    
pygame.init()

GREY = (29, 29, 29)
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 750
CELL_SIZE = 10
FPS = 12

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

# Simulation Loop
while True:

    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[1] // CELL_SIZE
            column = pos[0] // CELL_SIZE
            simulation.toggle_cell(row, column)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                simulation.start()
            elif event.key == pygame.K_SPACE:
                simulation.stop()
            elif event.key == pygame.K_f:
                FPS += 2
            elif event.key == pygame.K_s:
                if FPS > 5:
                    FPS -= 2
            elif event.key == pygame.K_r:
                simulation.create_random_state()
            elif event.key == pygame.K_c:
                simulation.clear()
            elif event.key == pygame.K_u:
                simulation.step()
            elif event.key == pygame.K_i:
                simulation.create_from_image()
            elif event.key == pygame.K_g:
                simulation.toggle_generation_view()
            elif event.key == pygame.K_b:
                simulation.increase_luminescence()
            elif event.key == pygame.K_d:
                simulation.decrease_luminescence()

    # 2. Updating State
    simulation.update()
    pygame.display.set_caption(f"Game of Life - Generation {simulation.generation} - Cells alive {simulation.get_alive_cells()}")

    # 3. Drawing
    window.fill(GREY)
    simulation.draw(window)

    pygame.display.update()
    clock.tick(FPS)