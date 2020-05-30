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

        m1 = 1 / self.phys.inertia.linear
        m2 = 1 / other.phys.inertia.linear
        vel1 = self.phys.rigid.linear.vel.x
        vel2 = other.phys.rigid.linear.vel.x

        # TODO: implement M22 for k = vel * sm
        sm = V2(sqrt(m1), sqrt(m2))
        kero = V2(vel1 * sm.x, vel2 * sm.y)

        energy = kero ** 2
        momentum = kero.mult(sm)
        mass = m1 + m2


        norm = (sm / sqrt(mass)).roty2x()

        print('norm =', norm)
        print('energy before =', kero ** 2)
        print('kero before =', kero)
        kero = kero - 2 * kero.dot(norm) * norm
        print('kero after =', kero)
        print('energy after =', kero ** 2)

        vel1, vel2 = kero.x / sm.x, kero.y / sm.y

        self.phys.rigid.linear.vel.x = vel1
        other.phys.rigid.linear.vel.x = vel2

    return Body.move(self, dt, world)

  def __str__(self):
    return f'{self.phys} {self.radius}'
