from .vector import V2, LA
from .physics import KineInertial, RigidInertial
from .scene import Body
from .common import load


class Ball(Body):
  def __init__(self, phys=None, radius=0):
    self.phys = phys or RigidInertial()
    self.radius = radius

  def __load__(self, str):
    self.phys = load(self.phys, str)
    self.radius = load(self.radius, str)

  def render(self, gui):
    angular_off = V2.of_angle(self.phys.rigid.angular.pos) * self.radius
    gui.circle(self.phys.rigid.linear.pos, self.radius * 0.15)
    gui.circle(self.phys.rigid.linear.pos, self.radius)
    gui.line(self.phys.rigid.linear.pos + angular_off * 0.15,
        self.phys.rigid.linear.pos + angular_off)

  def move(self, dt, world):
    from math import sqrt

    for other in world.bodies[:world.bodies.index(self)]:

      dist = self.phys.rigid.linear.pos - other.phys.rigid.linear.pos
      if dist.length() < self.radius + other.radius and \
          (self.phys.rigid.linear.vel - other.phys.rigid.linear.vel).dot(
              self.phys.rigid.linear.pos - other.phys.rigid.linear.pos) < 0:

        energy = self.phys.rigid.linear.vel ** 2 / self.phys.inertia.linear + \
                 other.phys.rigid.linear.vel ** 2 / other.phys.inertia.linear
        print('before', energy)

        disp = self.phys.rigid.linear.pos - other.phys.rigid.linear.pos
        disp.inormalize()

        m1 = 1 / self.phys.inertia.linear
        m2 = 1 / other.phys.inertia.linear
        vel1 = self.phys.rigid.linear.vel.dot(disp)
        vel2 = other.phys.rigid.linear.vel.dot(disp)

        # TODO: implement M22 for k = vel * sm
        sm = V2(sqrt(m1), sqrt(m2))
        kero = V2(vel1 * sm.x, vel2 * sm.y)

        energy = kero ** 2
        momentum = kero.mult(sm)
        mass = m1 + m2

        norm = (sm / sqrt(mass)).roty2x()

        kero = kero.reflect(norm)

        vel1, vel2 = kero.x / sm.x, kero.y / sm.y

        self.phys.rigid.linear.vel.ireflect(disp, 1)
        other.phys.rigid.linear.vel.ireflect(disp, 1)
        self.phys.rigid.linear.vel += vel1 * disp
        other.phys.rigid.linear.vel += vel2 * disp

        energy = self.phys.rigid.linear.vel ** 2 / self.phys.inertia.linear + \
                 other.phys.rigid.linear.vel ** 2 / other.phys.inertia.linear
        print('after', energy)

    return Body.move(self, dt, world)

  def __str__(self):
    return f'{self.phys} {self.radius}'
