### Load Object from a Serialized String

def load(x, str):
  if not isinstance(str, list):
    str = str.split()
  if isinstance(x, type):
    x = x()
  if isinstance(x, (int, float)):
    ent = str.pop(0) if str else 0
    try:
      x = int(ent)
    except ValueError:
      x = float(ent)
  else:
    x.__load__(str)
  return x
