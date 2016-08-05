#! python2
import pygame
import render

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
        pygame.display.set_icon(render.loadImg('icon.png'))
        self.phase = 'StartMenu'
        self.clock = pygame.time.Clock()
        self.running = True
        

    def loop(self):
        self.clock.tick(60)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250,250,250))

        #---------Render Here---------
        self.background = render.renderAll(self)
        #-----------------------------

        #Draw Everything
        self.screen.blit(self.background,(0,0))
        pygame.display.flip()

        #Input Somethings
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
