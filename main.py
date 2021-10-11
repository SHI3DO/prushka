import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pg.init()

Color = (255, 255, 255)  # 하얀색
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN, pg.OPENGL)

mainLoop = True
while mainLoop:
    screen.fill(Color)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            mainLoop = False
    pg.display.update()

pg.quit()
