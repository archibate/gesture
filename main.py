import gesture as gs
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

w = gs.World()
# pos_x pos_y | vel_x vel_y | angle ang_vel | inv_mass inv_rotin | radius
w.add(gs.Ball, '+0.0 +0.0\n+0.0 +0.0\n+0.0 +0.0\n1.0 0.0\n0.1\n')
w.add(gs.Ball, '-0.6 -0.1\n+0.3 +0.1\n+0.0 +0.0\n4.0 0.0\n0.05\n')

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(512, 512)
glutCreateWindow('G-A-M-E')

gui = gs.Renderer_OpenGL()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    w.render(gui)
    w.move(1 / 60)
    glFlush()

def timer(interval):
  glutTimerFunc(interval, timer, interval)
  glutPostRedisplay()

def keyboard(key, x, y):
  if key == b'\x1b':
    exit()

glutDisplayFunc(display)
glutTimerFunc(1000 // 60, timer, 1000 // 60)
glutKeyboardFunc(keyboard)
glutMainLoop()
