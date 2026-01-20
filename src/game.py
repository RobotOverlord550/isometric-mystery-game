

import pygame


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((720, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.back_ground_color = "purple"
        self.frame_rate = 60


    def _handle_events(self):
        """process game events
        """        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def _update_screen(self):
        """refresh the screen preferrably every frame
        """        
        self.screen.fill(self.back_ground_color)
        pygame.display.flip()
        self.clock.tick(self.frame_rate)

          
    def loop(self, update_function):
        """core game loop

        Args:
            update_function (function which has no parameters): function to run every game loop (frame)
        """        
        while self.running:
            self._handle_events()
            self._update_screen()
            update_function()


