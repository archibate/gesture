from .vector import V2, LA
from .common import load


### A Simulated Body

class Body:
  def interact(self, world):
    return world.gravity

  def move(self, dt, world):
    acc = self.interact(world)
    self.phys.move(dt, acc)


### Simulation Scene

class World:
  def __init__(self):
    self.bodies = []
    self.celestial_pos = V2(0.5, 0.5)
    self.gravity = LA(V2(0, -0), 0)

  def add(self, body, *args):
    if isinstance(body, type):
      body = load(body, *args)
    self.bodies.append(body)
    return body

  def render(self, gui):
    for body in self.bodies:
      body.render(gui)

  def move(self, dt):
    for body in self.bodies:
      body.move(dt, self)
