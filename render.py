import os,pygame

def loadImg(fileName):
    return pygame.image.load(os.path.join('asset',fileName))

#create start menu
def startMenu(background):
    Img = loadImg('BgMenu.jpg')
    Img = pygame.transform.scale(Img,(860,600))
    background.blit(Img,(-60,0))

#render everthing (main of render.py)
def renderAll(game):
    startMenu(game.background)
    return game.background
