"""
File: bouncing ball
Name: Yi Lin Yang
-------------------------
TODO:
This program can bounce the ball while the user clicking the mouse.
The bouncing ball will stop while the ball is out of the window.
The bouncing can be triggered by mouse-clicked only three times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
drop_or_not = False             # the swtich for starting bouncing the ball
drop_times = 0                  # bouncing triggered times

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global drop_times
    global drop_or_not
    onmouseclicked(count)
    vx = 0
    vy = 0
    ball = set_up_ball()
    window.add(ball, x=START_X, y=START_Y)

    while True:
        # Update
        ball.move(vx, vy)

        # Check
        if drop_or_not:
            vx = VX
            vy += GRAVITY
            if ball.y >= window.height:
                vy = -vy * REDUCE
            if ball.x >= window.width:
                drop_times += 1
                drop_or_not = False
                window.add(ball, x=START_X, y=START_Y)
        else:
            vx = 0
            vy = 0

        # Pause
        pause(DELAY)


def count(mouse):
    """
    judging each click whether bouncing the ball
    """
    global drop_or_not
    global drop_times
    if drop_times < 3:
        drop_or_not = True          # bounce the ball
    else:
        drop_or_not = False         # freeze


def set_up_ball():
    """
    the configuration of the ball
    """
    ball = GOval(SIZE, SIZE)
    ball.filled = True
    return ball


if __name__ == "__main__":
    main()
