
#Alperen İNCİ
#18120205016
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import math
import sys

posx, posy = -1.5, -2.5 #tekerlekler icin verilen degiskenler
sid = 32
rad = 0.7


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)

x = 0.5
y = 0.0
z = 0.0
W = 500
H = 500

#araba ciziminin ayarlanmasi
def carDraw():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(1.0)

    glBegin(GL_POLYGON)
    glColor3f(x, y, z)

    glVertex2f(-3.0, -2.0)
    glVertex2f(-3.0, 0.0)
    glVertex2f(3.0, 0.0)
    glVertex2f(3.0, -2.0)

    glEnd()

    glColor4f(0.0, 1.0, 1.0, 1.0)

    glBegin(GL_POLYGON)

    glVertex2f(-1.8, 0.0)
    glVertex2f(-1.8, 1.8)
    glVertex2f(1.8, 1.8)
    glVertex2f(1.8, 0.0)

    glEnd()
    glColor3f(0.0, 0.0, 0.0)

    glBegin(GL_TRIANGLE_FAN)

    for i in range(50):
        cosine = rad * math.cos(i * 2 * math.pi / sid) + posx
        sine = rad * math.sin(i * 2 * math.pi / sid) + posy
        glVertex2f(cosine, sine)
        glColor3f(0.0, 0.0, 0.0)

    glEnd()
    glColor3f(0.0, 0.0, 0.0)

    glBegin(GL_TRIANGLE_FAN)

    for i in range(50):
        cosine = rad * math.cos(i * 2 * math.pi / sid) + posx + 3
        sine = rad * math.sin(i * 2 * math.pi / sid) + posy
        glVertex2f(cosine, sine)

    glEnd()

    glFlush()


def renkDegistirme(*args):
    global x, y, z

    if args[0] == bytes('r', 'utf-8'):
        x = 1
        y = 0
        z = 0

        glutPostRedisplay()
    elif args[0] == bytes('g', 'utf-8'):
        x = 0
        y = 1
        z = 0

        glutPostRedisplay()
    elif args[0] == bytes('b', 'utf-8'):
        x = 0
        y = 0
        z = 1

        glutPostRedisplay()
    elif args[0] == b"\x1b":
        sys.exit()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Car")
    glutDisplayFunc(carDraw)
    glutKeyboardFunc(renkDegistirme)
    init()
    glutMainLoop()


main()
# End of program
