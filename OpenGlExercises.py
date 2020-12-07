#Alperen İnci
#18120205016

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

#degiskenler

window = 0

#rotasyonlar
X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0

zoom = 0.5

deltax = 0.0
deltay = 0.0

perimeter = 1.0
left_mouseclick = 0
right_mouseclick = 0

x_rotation=0
y_rotation=0

x_d=0
y_d=0

mouseHold = False

#Bu fonksiyonlar çaydanlığa tut-döndür-bırak özelliği ekler.(mouseRot,mouse,mouseMotion)
def mouseRot():
    global x_rotation
    global y_rotation
    global mouseHold
    if (mouseHold != False):
        x_rotation += 0.3
        y_rotation += 0.4
    glutPostRedisplay()


def mouse(button, state, x, y):
    global x_d
    global y_d
    global mouseHold
    if (button == GLUT_LEFT_BUTTON and state == GLUT_DOWN):

        mouseHold = True
        x_d = x - y_rotation
        y_d = -y + x_rotation
    else:
        mouseHold = False


def mouseMotion(x, y):
    global x_rotation
    global y_rotation
    if mouseHold:
        y_rotation = x - x_d
        x_rotation = y + y_d
        glutPostRedisplay()


def InitGL(Width, Height): #init fonksiyonu
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glScale(zoom, zoom, zoom)
    glMatrixMode(GL_MODELVIEW)


def MouseWheel(*args):#Bu Fonksiyon farenin tekerleği ile zoom yapmamıza yarar.
    global zoom
    print(args)
    if args[1] == -1:
        zoom -= 0.05
    elif args[1] == 1:
        zoom += 0.05
    else:
        pass
    glutPostRedisplay()


def keyPressed(*args):#küp ü yukari asagi , saga ve sola hareket ettiren fonksiyon
    global deltax
    global deltay

    if args[0] == b"\x1b":

        sys.exit()
    if args[0]  == b"a":
        print(args)
        deltax-=1
    elif args[0]  == b"d":
        print(args)
        deltax+=1
    elif args[0] == b"w":
        print(args)
        deltay += 1
    elif args[0] == b"s":
        print(args)
        deltay -= 1
    glutPostRedisplay()


def DrawGLScene():# Ana fonksiyon
    global X_AXIS, Y_AXIS, Z_AXIS
    global zoom
    global perimeter

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_BLEND)


    #1.Viewport çaydanlık çizimi
    glViewport(20, 20, 300, 350)
    glLoadIdentity()
    glPushMatrix()
    glRotatef(x_rotation, 1.0, 0.0, 0.0)
    glRotatef(y_rotation, 0.0, 1.0, 0.0)
    glColor3f(0, 0, 1)
    glutSolidTeapot(0.5)
    glPopMatrix()

    if left_mouseclick:
        perimeter += 0.1
    if right_mouseclick:
        perimeter -= 0.1

    #2.Viewport küp çizimi
    glViewport(220, 200, 300, 300)
    glTranslatef(deltax, deltay, 1)
    display = (640, 480)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -6.0)

    glRotatef(X_AXIS, 1.0, 0.0, 0.0)
    glRotatef(Y_AXIS, 0.0, 1.0, 0.0)
    glRotatef(Z_AXIS, 0.0, 0.0, 1.0)
    glScale(zoom, zoom, zoom)


    glBegin(GL_QUADS)

    #küpün her bir yüzeyinin renginin ve konumunun ayarı.
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glColor3f(0.0, 1.0, 0.8)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glEnd()

    #kupun donus hizinin ayarlanmasi
    X_AXIS = X_AXIS - 0.01
    Z_AXIS = Z_AXIS - 0.01

    glFlush()
    glutSwapBuffers()



def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(200, 200)
    window = glutCreateWindow('OpenGL ODEV 6')
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(640, 480)
    glutMouseWheelFunc(MouseWheel)
    glutMouseFunc(mouse)
    glutMotionFunc(mouseMotion)

    glutMainLoop()



if __name__ == "__main__":
    main()
