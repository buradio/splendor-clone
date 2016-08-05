import os,pygame

def loadImg(fileName,colorkey=False):
    file = os.path.join('asset',fileName)
    _image = pygame.image.load(file)
    if colorkey:
        if colorkey == -1: 
        # If the color key is -1, set it to color of upper left corner
            colorkey = _image.get_at((0, 0))
        _image.set_colorkey(colorkey)
        _image = _image.convert()
    else: # If there is no colorkey, preserve the image's alpha per pixel.
        _image = _image.convert_alpha()
    return _image

#create start menu
def startMenu(background):
    Img = loadImg('BgMenu.jpg')
    Img = pygame.transform.scale(Img,(860,600))
    background.blit(Img,(-60,0))

#render everthing (main of render.py)
def renderAll(game):
    startMenu(game.background)
    return game.background
