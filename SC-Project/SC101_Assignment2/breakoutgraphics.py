"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

The breakoutgraphics contains all objects/methods
which are used and exist in YiLin's breakout game.

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10      # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 175      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2,
                            y=window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=window_width/2-ball_radius, y=window_height/2-ball_radius)

        # scoreboard
        self.score = 0
        self.scoreboard = GLabel('Score: ' + str(self.score), x=5, y=40)
        self.scoreboard.font = '-20'
        self.window.add(self.scoreboard)

        # create remaining-lives figures
        self.live_sign1 = GOval(20, 20, x=self.window.width-75, y=15)
        self.live_sign2 = GOval(20, 20, x=self.window.width-50, y=15)
        self.live_sign3 = GOval(20, 20, x=self.window.width-25, y=15)
        self.live_sign1.filled = True
        self.live_sign2.filled = True
        self.live_sign3.filled = True
        self.live_sign1.color = 'purple'
        self.live_sign2.color = 'purple'
        self.live_sign3.color = 'purple'
        self.live_sign1.fill_color = 'purple'
        self.live_sign2.fill_color = 'purple'
        self.live_sign3.fill_color = 'purple'
        self.window.add(self.live_sign1)
        self.window.add(self.live_sign2)
        self.window.add(self.live_sign3)

        # game over label
        self.game_over = GLabel('GAME OVER')
        self.game_over.font = '-40'

        # game winning label
        self.win = GLabel('YOU WIN!')
        self.win.font = '-40'

        # Draw bricks
        brick_y = brick_offset
        for i in range(brick_rows):
            brick_x = 0
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i+1 <= brick_rows/5:
                    self.brick.color = 'red'
                    self.brick.fill_color = 'red'
                elif i+1 <= brick_rows/5*2:
                    self.brick.color = 'orange'
                    self.brick.fill_color = 'orange'
                elif i+1 <= brick_rows/5*3:
                    self.brick.color = 'yellow'
                    self.brick.fill_color = 'yellow'
                elif i+1 <= brick_rows/5*4:
                    self.brick.color = 'green'
                    self.brick.fill_color = 'green'
                else:
                    self.brick.color = 'blue'
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=brick_x, y=brick_y)
                brick_x += brick_width+brick_spacing
            brick_y += brick_height+brick_spacing
        self.ball_touch_brick()
        self.remove_all_bricks()

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.set_ball_velocity()

        # Initialize our mouse listeners
        onmousemoved(self.move_the_paddle)
        onmouseclicked(self.handle_click)
        self.is_first_click = False
        self.count = 0

    def move_the_paddle(self, event):
        self.paddle.x = event.x-self.paddle.width/2
        if event.x < self.paddle.width/2:
            self.paddle.x = 0
        if event.x > self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width

    def ball_at_side(self):
        ball_at_side = self.ball.x <= 0 or self.ball.x+self.ball.width >= self.window.width
        return ball_at_side

    def ball_at_ceiling(self):
        ball_at_ceiling = self.ball.y <= 0
        return ball_at_ceiling

    def ball_at_bottom(self):
        ball_at_bottom = self.ball.y+self.ball.height >= self.window.height
        return ball_at_bottom

    def reset_ball(self):
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.__dx = 0
        self.__dy = 0
        self.is_first_click = False
        self.count = 0
        self.window.add(self.ball)

    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def handle_click(self, event):
        if self.count is 0:
            self.is_first_click = True
            self.count += 1
        else:
            self.is_first_click = False

    def get_vx(self):
        vx = self.__dx
        return vx

    def get_vy(self):
        vy = self.__dy
        return vy

    def ball_touch_brick(self):
        ball_left_top = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_right_top = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        ball_left_bottom = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        ball_right_bottom = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)

        is_ball_touch_brick = False

        if ball_left_bottom is not self.paddle:
            if ball_left_top is not self.scoreboard and ball_right_top is not self.scoreboard and \
                    ball_left_bottom is not self.scoreboard and ball_right_bottom is not self.scoreboard and \
                    ball_left_top is not self.live_sign1 and ball_right_top is not self.live_sign1 and \
                    ball_left_bottom is not self.live_sign1 and ball_right_bottom is not self.live_sign1 and \
                    ball_left_top is not self.live_sign2 and ball_right_top is not self.live_sign2 and \
                    ball_left_bottom is not self.live_sign2 and ball_right_bottom is not self.live_sign2 and \
                    ball_left_top is not self.live_sign3 and ball_right_top is not self.live_sign3 and \
                    ball_left_bottom is not self.live_sign3 and ball_right_bottom is not self.live_sign3:
                if ball_left_top is not None:
                    is_ball_touch_brick = True
                    self.score += 100
                    self.scoreboard.text = 'Score: ' + str(self.score)
                    self.window.remove(ball_left_top)
                elif ball_right_top is not None:
                    self.score += 100
                    self.scoreboard.text = 'Score: ' + str(self.score)
                    self.window.remove(ball_right_top)
                    is_ball_touch_brick = True
                elif ball_left_bottom is not None:
                    self.score += 100
                    self.scoreboard.text = 'Score: ' + str(self.score)
                    self.window.remove(ball_left_bottom)
                    is_ball_touch_brick = True
                elif ball_right_bottom is not None:
                    self.score += 100
                    self.scoreboard.text = 'Score: ' + str(self.score)
                    self.window.remove(ball_right_bottom)
                    is_ball_touch_brick = True

        return is_ball_touch_brick

    def ball_touch_paddle(self):
        ball_left_top = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_right_top = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        ball_left_bottom = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        ball_right_bottom = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height)
        is_ball_touch_paddle = False

        if ball_left_top is self.paddle or ball_right_top is self.paddle or \
                ball_left_bottom is self.paddle or ball_right_bottom is self.paddle:
            is_ball_touch_paddle = True
        return is_ball_touch_paddle

    def game_is_over(self):
        self.window.add(self.game_over, x=(self.window.width-self.game_over.width)/2,
                        y=self.window.height/2+self.game_over.height)

    def remove_all_bricks(self):
        remove_all_brick = False
        if self.score == 100*BRICK_ROWS*BRICK_COLS:
            remove_all_brick = True
        return remove_all_brick

    def is_win(self):
        self.window.add(self.win, x=(self.window.width-self.win.width)/2, y=self.window.height/2)
