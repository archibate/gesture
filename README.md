# Gesture.py

A 2D rigid-body real-time physics engine in Python.

To use:
```py
import gesture as gs
```

To run the little demo:

```bash
cd gesture
pip install pyopengl
python main.py
```

Directory orginization:

`gesture/`
- `__init__.py` - top-level of this package.
- `bodies.py` - different type of bodies like ball, cube, etc.
- `common.py` - common utilities used by all modules.
- `display.py` - displaying & rendering scene.
- `physics.py` - the physics implementation.
- `scene.py` - simulation scene / session.
- `vector.py` - vector arithmetics.
