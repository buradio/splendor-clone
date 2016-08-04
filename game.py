#! python2
import pygame

"""
    game.py is the main file to create pygame window

    classes:
        Game: main Game object
"""


class Game():

    #constants
    DISPLAY_SIZE = DISPLAY_WIDTH,DISPLAY_HEIGHT = 800,600
    TITLE = "SPLENDOR"
    
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(self.DISPLAY_SIZE)
        pygame.display.set_caption(self.TITLE)

        self.clock = pygame.time.Clock()
        self.running = True
        

    def loop(self):
        self.clock.tick(60)

        self.screen.fill(0)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

    def quit(self):
        self.running = False
        pygame.quit()


#initialize game
game = Game()

#call gameloop
while game.running:
    game.loop()
