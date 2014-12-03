import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Scene:

    def __init__(self, window_size=[500, 500]):
        self.window = pygame.display.set_mode(
            window_size, HWSURFACE | OPENGL | DOUBLEBUF
            )
        glViewport(0, 0, window_size[0], window_size[1])
        glShadeModel(GL_SMOOTH)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        viewport = glGetIntegerv(GL_VIEWPORT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(
            60.0,
            float(viewport[2]) / float(viewport[3]),
            0.1,
            1000.0
            )
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def Get_Window(self):
        return self.window


def init():
    global scene
    scene = Scene()


def Get():
    try:
        return scene
    except:
        init()
        return scene


def Draw(points):
    for p in points:
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_POINTS)
        glVertex2i(int(p[0]), int(p[1]), int(p[2]))
        glEnd()
