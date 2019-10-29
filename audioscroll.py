from pymouse import PyMouseEvent, PyMouse
import os
import sys

if len(sys.argv) != 3:
    print("Missing or too many arguments!")
    print("Usage: python3 audioscroll.py <u/d> <l/f>")
    sys.exit(1)

if sys.argv[1] == "u":
    u_d = 1
else:
    u_d = -1

if sys.argv[2] == "l":
    l_r = 1
else:
    l_r = 0


class Scrolling(PyMouseEvent):
    m = PyMouse()
    screen = m.screen_size()
    screen_size = (screen[0], 0)

    def __init__(self):
        PyMouseEvent.__init__(self)

    def stop(self):
        self.state = False

    def scroll(self, x, y, vertical, horizontal):
        if abs(x - self.screen_size[l_r]) < 2:
            if(vertical*u_d > 0):
                os.system("amixer -D pulse sset Master 5%+")
            else:
                os.system("amixer -D pulse sset Master 5%-")


Mouse = Scrolling()
Mouse.run()
