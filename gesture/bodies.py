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
    for other in world.bodies:
      if other is self: continue

      dist = self.phys.rigid.linear.pos - other.phys.rigid.linear.pos
      if dist.length() < self.radius + other.radius:
        imp = 2 * self.phys.rigid.linear.vel.length() * dist.normalize()
        self.phys.rigid.linear.vel += imp

    return Body.move(self, dt, world)

  def __str__(self):
    return f'{self.phys} {self.radius}'
