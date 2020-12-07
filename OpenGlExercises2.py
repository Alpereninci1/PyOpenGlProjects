# Alperen İnci
# 18120205016

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import random

#degiskenler
mouse_click = False

viewportSelected = 2

viewportSelected2 = 2

viewportSelected3 = 2
deltax = 0.0
deltay = 0.0

dx = 0.4
boyut = 0.3


def InitGL(Width, Height):  # init fonksiyonu
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)


def mouse(button, state, x, y):  # mouse fonksiyonu
    global viewportSelected
    global viewportSelected2
    global viewportSelected3
    global mouse_click

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:

        mouse_click = True
        print("left mouse clicked", x, y)

        if 230 >= x >= 0 and 0 <= y <= 270:
            viewportSelected += 1

        if 550 >= x >= 300 and 0 <= y <= 270:
            viewportSelected2 += 1

        if 420 >= x >= 200 and 260 <= y <= 380:
            viewportSelected3 += 1

    else:
        mouse_click = False


def klavye(key, x, y):  # klavye fonksiyonu
    global deltax
    global deltay

    if key == GLUT_KEY_DOWN:
        deltay -= 1

    if key == GLUT_KEY_UP:
        deltay += 1

    if key == GLUT_KEY_RIGHT:
        deltax += 1

    if key == GLUT_KEY_LEFT:
        deltax -= 1
    glutPostRedisplay()


def drawView1(boyut):
    global viewportSelected
    global dx
    r = 1
    g = 1
    b = 1

    if viewportSelected % 3 == 0:
        r, g, b = random.random(), random.random(), random.random()

    if viewportSelected % 3 == 1:
        boyut = boyut * dx

    # 1.Viewport çaydanlık çizimi
    glViewport(20, 120, 300, 300)
    glLoadIdentity()
    glPushMatrix()
    glTranslatef(deltax, deltay, 1)
    glColor3f(r, g, b)
    glutSolidTeapot(boyut)
    glPopMatrix()


def drawView2(boyut):
    global viewportSelected2
    global dx
    r = 0
    g = 1
    b = 1

    if viewportSelected2 % 3 == 0:
        r, g, b = random.random(), random.random(), random.random()

    if viewportSelected2 % 3 == 1:
        boyut = boyut * dx

    # 2.Viewport çaydanlık çizimi
    glViewport(270, 120, 300, 300)
    glLoadIdentity()
    glPushMatrix()
    glTranslatef(deltax, deltay, 1)
    glColor3f(r, g, b)
    glutSolidTeapot(boyut)
    glPopMatrix()


def drawView3(boyut):
    global viewportSelected3
    global dx
    r = 0
    g = 1
    b = 0

    if viewportSelected3 % 3 == 0:
        r, g, b = random.random(), random.random(), random.random()

    if viewportSelected3 % 3 == 1:
        boyut = boyut * dx

    # 3.Viewport çaydanlık çizimi
    glViewport(160, 10, 300, 300)
    glLoadIdentity()
    glPushMatrix()
    glTranslatef(deltax, deltay, 1)
    glColor3f(r, g, b)
    glutSolidTeapot(boyut)
    glPopMatrix()


def DrawGLScene():  # Ana fonksiyon

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    drawView1(boyut)
    drawView2(boyut)
    drawView3(boyut)

    glFlush()
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(200, 200)
    glutCreateWindow('VİZE')
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutSpecialFunc(klavye)
    glutMouseFunc(mouse)
    InitGL(640, 480)
    glutMainLoop()


if __name__ == "__main__":
    main()
