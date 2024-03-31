#-----------------------------------------------------------------------------------
# CONTROLLER: The class for event handling
#-----------------------------------------------------------------------------------
import pygame, sys

class Controller:
    def __init__(self, model, view, fps):
        self.model = model
        self.view = view
        self.fps = fps

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                self.view.resize(event.dict["size"])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row = pos[1] // self.view.cell_size
                column = pos[0] // self.view.cell_size
                self.model.toggle_cell(row, column)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.model.start()
                elif event.key == pygame.K_SPACE:
                    self.model.stop()
                elif event.key == pygame.K_f:
                    self.fps += 2
                elif event.key == pygame.K_s:
                    if self.fps > 5:
                        self.fps -= 2
                elif event.key == pygame.K_r:
                    self.model.create_random_state()
                elif event.key == pygame.K_c:
                    self.model.clear()
                elif event.key == pygame.K_u:
                    self.model.step()
                elif event.key == pygame.K_i:
                    self.model.create_from_image()
                elif event.key == pygame.K_g:
                    self.view.toggle_generation_view()
                elif event.key == pygame.K_b:
                    self.view.increase_luminescence()
                elif event.key == pygame.K_d:
                    self.view.decrease_luminescence()
