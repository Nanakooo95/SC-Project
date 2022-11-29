"""
File: draw_line
Name: Yi Lin Yang
-------------------------
TODO:
This program will draw straight lines wherever the user wants!
Also, as many lines as they want!
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10

window = GWindow()
is_it_odd = True                    # Judge the click is the odd times or not
dot = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(draw_line)


def draw_line(mouse):
    """
    :param mouse: the mouse event, getting the position where the mouse is
    is_it_odd: judge if the times of the mouse click is odd
    """
    global is_it_odd
    # the times is odd, draw the start point
    if is_it_odd:
        window.add(dot, mouse.x - SIZE / 2, mouse.y - SIZE / 2)         # the start point of the line
        is_it_odd = False           # next times will be even, so reassign is_it_odd False

    # the times is even, draw the line
    else:
        line = GLine(dot.x, dot.y, mouse.x - SIZE / 2, mouse.y - SIZE / 2)
        window.add(line)
        window.remove(dot)
        is_it_odd = True


if __name__ == "__main__":
    main()
