### OpenGL wrapper for gesture renderer interface

class Renderer:
  def circle(self, pos, radius):
    raise NotImplementedError

  def line(self, begin, end):
    raise NotImplementedError


class Renderer_OpenGL(Renderer):
  def circle(self, center, radius):
    from OpenGL.GL import glBegin, glVertex2f, glEnd, GL_LINE_LOOP
    import math

    cx, cy = center
    N = 36

    glBegin(GL_LINE_LOOP)
    for a in range(N):
      a = math.tau * a / N
      dx, dy = math.cos(a) * radius, math.sin(a) * radius
      glVertex2f(cx + dx, cy + dy)

    glEnd()

  def line(self, begin, end):
    from OpenGL.GL import glBegin, glVertex2f, glEnd, GL_LINES

    ax, ay = begin
    bx, by = end

    glBegin(GL_LINES)
    glVertex2f(ax, ay)
    glVertex2f(bx, by)
    glEnd()
