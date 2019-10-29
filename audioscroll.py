from pymouse import PyMouseEvent, PyMouse
import os
import sys

if len(sys.argv) != 2:
    print("Missing or too many arguments! Usage: python3 audioscroll.py <u/d>")
    sys.exit(1)

if sys.argv[1] == "u":
    mult = 1
else:
    mult = -1


class Scrolling(PyMouseEvent):
    m = PyMouse()
    screen_width = m.screen_size()[0]

    def __init__(self):
        PyMouseEvent.__init__(self)

    def stop(self):
        self.state = False

    def scroll(self, x, y, vertical, horizontal):
        if x >= (self.screen_width - 1):
            if(vertical*mult > 0):
                os.system("amixer -D pulse sset Master 5%+")
            else:
                os.system("amixer -D pulse sset Master 5%-")


Mouse = Scrolling()
Mouse.run()
