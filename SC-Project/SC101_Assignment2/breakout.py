"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Welcome to YiLin's breakout game! Each bricks can earn 100 points.
Until all bricks are eliminated, you win!!!
TO notice, You have three chances to miss the ball.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts

graphics = BreakoutGraphics()
vx = 0
vy = 0


def main():
    global vx
    global vy
    lives = NUM_LIVES
    # the animation loop!
    while True:
        # pause
        pause(FRAME_RATE)
        # update
        graphics.ball.move(vx, vy)
        # check
        if graphics.is_first_click:
            graphics.set_ball_velocity()
            vx = graphics.get_vx()
            vy = graphics.get_vy()
            graphics.is_first_click = False
        # the condition to win
        if graphics.remove_all_bricks():
            graphics.is_win()
            break
        # the condition to lose lives
        if graphics.ball_at_bottom():
            lives -= 1
            if lives is 2:
                graphics.window.remove(graphics.live_sign1)
            if lives is 1:
                graphics.window.remove(graphics.live_sign2)
            if lives == 0:
                graphics.window.remove(graphics.live_sign3)
                graphics.game_is_over()
                break

            graphics.reset_ball()
            vx = 0
            vy = 0
        # conditions to rebound
        elif graphics.ball_at_side():
            vx = -vx
        elif graphics.ball_at_ceiling():
            vy = -vy
        elif graphics.ball_touch_paddle():
            vy = -vy
        elif graphics.ball_touch_brick():
            vy = -vy


if __name__ == '__main__':
    main()
