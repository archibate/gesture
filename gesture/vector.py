import math
from .common import load


### 2D Vector

class V2:
  __slots__ = ['x', 'y']

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def copy(self):
    return V2(self.x, self.y)

  def to_tuple(self):
    return (self.x, self.y)

  @staticmethod
  def from_tuple(tuple):
    x, y = tuple
    return V2(x, y)

  @staticmethod
  def of_angle(angle):
    return V2(math.cos(angle), math.sin(angle))

  def __getitem__(self, i):
    if i == 0:
      return self.x
    if i == 1:
      return self.y
    raise IndexError

  def __setitem__(self, i, value):
    if i == 0:
      self.x = value
    if i == 1:
      self.y = value
    raise IndexError

  def __len__(self):
    return 2

  def __add__(self, other):
    return V2(self.x + other.x, self.y + other.y)

  def __iadd__(self, other):
    self.x += other.x
    self.y += other.y
    return self

  __radd__ = __add__

  def __sub__(self, other):
    return V2(self.x - other.x, self.y - other.y)

  def __isub__(self, other):
    self.x -= other.x
    self.y -= other.y
    return self

  def __rsub__(self, other):
    return V2(other.x - self.x, other.y - self.y)

  def __mul__(self, other):
    return V2(self.x * other, self.y * other)

  def __imul__(self, other):
    self.x *= other.x
    self.y *= other.y
    return self

  __rmul__ = __mul__

  def __truediv__(self, other):
    return self * (1 / other)

  def __itruediv__(self, other):
    self.x /= other.x
    self.y /= other.y

  def __floordiv__(self, other):
    return V2(self.x // other, self.y // other)

  def __ifloordiv__(self, other):
    self.x //= other.x
    self.y //= other.y
    return self

  def dot(self, other):
    return self.x * other.x + self.y * other.y

  def cross(self, other):
    return self.x * other.y - self.y * other.x

  def length(self):
    return math.sqrt(self.x ** 2 + self.y ** 2)

  __abs__ = length

  def normalize(self):
    return self / self.length()

  def inormalize(self):
    self /= self.length()
    return self

  def __pow__(self, n):
    return (self.x ** 2 + self.y ** 2) ** (n / 2)

  def angle(self):
    return math.atan2(self.y, self.x)

  def __load__(self, str):
    self.x = load(self.x, str)
    self.y = load(self.y, str)

  def __str__(self):
    return f'{self.x} {self.y}'

  def __repr__(self):
    return f'V2({repr(self.x)}, {repr(self.y)})'

  def __hash__(self):
    return hash(self.x) + hash(self.y)

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __ne__(self, other):
    return self.x != other.x or self.y != other.y


### Linear + Angular

class LA:
  __slots__ = ['linear', 'angular']

  def __init__(self, linear, angular):
    self.linear = linear
    self.angular = angular

  def __add__(self, other):
    return LA(self.linear + other.linear, self.angular + other.angular)

  def __iadd__(self, other):
    self.linear += other.linear
    self.angular += other.angular

  __radd__ = __add__

  def __sub__(self, other):
    return LA(self.linear - other.linear, self.angular - other.angular)

  def __isub__(self, other):
    self.linear -= other.linear
    self.angular -= other.angular

  def __rsub__(self, other):
    return LA(other.linear - self.linear, other.angular - self.angular)

  def __mul__(self, other):
    return LA(self.linear * other, self.angular * other)

  def __imul__(self, other):
    self.linear *= other.linear
    self.angular *= other.angular

  __rmul__ = __mul__

  def mult(self, other):
    return LA(self.linear * other.linear, self.angular * other.angular)

  def __truediv__(self, other):
    return self * (1 / other)

  def __itruediv__(self, other):
    self.linear /= other.linear
    self.angular /= other.angular

  def __floordiv__(self, other):
    return LA(self.linear // other, self.angular // other)

  def __ifloordiv__(self, other):
    self.linear //= other.linear
    self.angular //= other.angular

  def __load__(self, str):
    self.linear = load(self.linear, str)
    self.angular = load(self.angular, str)

  def __str__(self):
    return f'{self.linear} {self.angular}'

  def __repr__(self):
    return f'LA({repr(self.linear)}, {repr(self.angular)})'
