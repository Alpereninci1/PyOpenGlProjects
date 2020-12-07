#Alperen inci 18120205016
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import sys


#global degiskenler
baslangic=time.time()#dongu baslangici degiskeni
periyot=12 #dongu periyodumuzun degeri
ayin_per=30 #ayin periyodu
yil=365
eksen_egikligi=23

def InitGL():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-5, 5, -5, 5)
    glMatrixMode(GL_MODELVIEW)

def UzaySahne(Width, Height): # Uzay sahnesinin dizaynı
   glViewport (0, 0, Width,Height)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity()
   gluPerspective(100, Width/Height, 1, 30)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   gluLookAt (0, 0, 5.2, 0, 0, 0, 0, 1, 0)

def GunesSistemi():#Gunes Dunya Ay Cizimi

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    #dongu icin zaman degiskenlerinin ayarlanmasi
    global zaman
    global dongu_suresi
    global donme_suresi
    global ay_dongusu
    zaman = time.time() - baslangic
    dongu_suresi = (zaman / periyot)
    donme_suresi = yil * dongu_suresi
    ay_dongusu = (yil / ayin_per) * dongu_suresi

    #gezegenlerin kendi etrafinda dondugunu anlayabilmek icin yaptıgim isiklandirma ve golgelendirme
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_BLEND)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

    #Gunes
    glColor3f(1,1,0)#gunesin rengi
    glPushMatrix()
    glRotatef(dongu_suresi * yil, 0, 1, 0)#gunesin kendi etrafinda donmesi
    glutSolidSphere(1.2, 20, 15)#gunesin sekli

    #Dunya
    glRotatef(dongu_suresi * yil, 0, 1, 0)#dunyanin gunes etrafinda donmesi
    glTranslatef(3.2, 0.1, 0)#dunyanin konumu
    glPushMatrix()

    glPushMatrix()

    glColor3f(0, 0.5, 1)#dunyanin rengi
    glRotatef(donme_suresi * yil, 0, 1, 0)#dunyanin kendi etrafinda donmesi
    glRotatef(90-eksen_egikligi, 1, 0, 0)#dunyanin eksen egikliği ile donmesi
    glutSolidSphere(0.3, 10, 8)#dunyanin sekli
    glPopMatrix()

    #Ay
    glPushMatrix()

    glColor4f(0.5, 0.5, 0.5, 1)#ay rengi
    glRotatef(ay_dongusu * yil, 0, 1, 0)#ay'in dunya etrafinda donmesi
    glTranslatef(1, 0, 0)#ay'in konumu
    glRotatef(90, 1, 0, 0)#ay'in kendi etrafinda donmesi
    glutSolidSphere(0.1, 8, 8)#ay'in sekli
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(1000,800)
    glutInitWindowPosition(70, 70)
    glutCreateWindow("Gunes dunya ve ayın birbirine gore hareketleri")
    InitGL()
    glutDisplayFunc(GunesSistemi)
    glutIdleFunc(GunesSistemi)
    glutReshapeFunc(UzaySahne)
    glutMainLoop()

main()