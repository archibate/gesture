from .vector import V2, LA
from .common import load


### (p, q) Pair

class Kine:
  __slots__ = ['pos', 'vel']

  def __init__(self, pos, vel):
    self.pos = pos
    self.vel = vel

  def move(self, dt, acc):
    self.pos += self.vel * dt
    self.vel += acc * dt

  def __load__(self, str):
    self.pos = load(self.pos, str)
    self.vel = load(self.vel, str)

  def __str__(self):
    return f'{self.pos} {self.vel}'


### Linear & Angular (p, q) Pair

class Rigid(LA):
  def __init__(self, linear=None, angular=None):
    linear = linear or Kine(V2(0, 0), V2(0, 0))
    angular = angular or Kine(0, 0)
    LA.__init__(self, linear, angular)

  def move(self, dt, acc):
    self.linear.move(dt, acc.linear)
    self.angular.move(dt, acc.angular)

  def __str__(self):
    return f'{self.linear} {self.angular}'


### A Rigid Body with Inertia

class RigidInertial:
  def __init__(self, rigid=None, inertia=None):
    self.rigid = rigid or Rigid()
    self.inertia = inertia or LA(0, 0)

  def move(self, dt, acc):
    self.rigid.move(dt, self.inertia.mult(acc))

  def __load__(self, str):
    self.rigid = load(self.rigid, str)
    self.inertia = load(self.inertia, str)

  def __str__(self):
    return f'{self.rigid} {self.inertia}'


### A Kinematic Point with Inertia

class KineInertial:
  def __init__(self, kine=None, inertia=0):
    self.kine = kine or Kine(V2(0, 0), V2(0, 0))
    self.inertia = inertia

  def move(self, dt, acc):
    self.kine.move(dt, self.inertia * acc)

  def __load__(self, str):
    self.kinematic = load(self.kinematic, str)
    self.inertia = load(self.inertia, str)

  def __str__(self):
    return f'{self.kinematic} {self.inertia}'
