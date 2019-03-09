from livewires import games
import math

games.init(screen_width=600, screen_height=489, fps=50)


class Player(games.Sprite):
    VELOCITY_STEP = .03
    VELOCITY_STOP = .1
    VELOCITY_MAX = 3

    def update(self):
        self.dx = min(max(self.dx, -Player.VELOCITY_MAX), Player.VELOCITY_MAX)
        self.dy = min(max(self.dy, -Player.VELOCITY_MAX), Player.VELOCITY_MAX)
        if self.dy < 0:
            tan = -self.dx / self.dy
            angle = math.atan(tan)
            self.angle = angle * 180 / math.pi
        elif self.dy > 0:
            tan = -self.dx / self.dy
            angle = math.atan(tan)
            self.angle = angle * 180 / math.pi + 180
        elif self.dx > 0:
            self.angle = 90
        elif self.dx < 0:
            self.angle = 270

        if games.keyboard.is_pressed(games.K_s):
            self.dy += Player.VELOCITY_STEP
        elif self.dy > 0:
            self.dy -= 0.1
            if self.dy < 0:
                self.dy = 0
        if games.keyboard.is_pressed(games.K_w):
            self.dy -= Player.VELOCITY_STEP
        elif self.dy < 0:
            self.dy += 0.1
            if self.dy > 0:
                self.dy = 0

        if games.keyboard.is_pressed(games.K_d):
            self.dx += Player.VELOCITY_STEP
        elif self.dx > 0:
            self.dx -= 0.1
            if self.dx < 0:
                self.dx = 0
        if games.keyboard.is_pressed(games.K_a):
            self.dx -= Player.VELOCITY_STEP
        elif self.dx < 0:
            self.dx += 0.1
            if self.dx > 0:
                self.dx = 0

        if self.right > games.screen.width:
            self.right = games.screen.width
            self.dx = 0
        if self.top < 0:
            self.top = 0
            self.dy = 0
        if self.left < 0:
            self.left = 0
            self.dx = 0
        if self.bottom > games.screen.height:
            self.bottom = games.screen.height
            self.dy = 0
        if self.bottom > 209 and self.top < 200 and self.left < 31:
            self.bottom = 209
            self.dy = 0


        if self.overlapping_sprites and (self.dx != 0 or self.dy != 0):
            for sprite in self.overlapping_sprites:
                if str(sprite) == 'Ball':
                    sprite.move(self.dx, self.dy)
                else:
                    self.dx = -self.dx
                    self.dy = -self.dy



class Ball(games.Sprite):
    VELOCITY_FACTOR = 1.8

    def __str__(self):
        return 'Ball'

    def update(self):
        if self.right > games.screen.width:
            self.right = games.screen.width
            self.dx = -self.dx
        if self.top < 0:
            self.top = 0
            self.dy = -self.dy
        if self.left < 0:
            self.left = 0
            self.dx = -self.dx
        if self.bottom > games.screen.height:
            self.bottom = games.screen.height
            self.dy = -self.dy

        if self.dx > 0:
            self.dx *= .98
            if self.dx < 0.1:
                self.dx = 0
        if self.dx < 0:
            self.dx *= .98
            if self.dx > -0.1:
                self.dx = 0
        if self.dy > 0:
            self.dy *= .98
            if self.dy < 0.1:
                self.dy = 0
        if self.dy < 0:
            self.dy *= .98
            if self.dy > -0.1:
                self.dy = 0

        if 210 < self.y < 279 and self.x < 30:
            games.screen.quit()

        if self.overlapping_sprites:
            self.dx = -self.dx
            self.dy = -self.dy

    def move(self, player_dx, player_dy):
        self.dx = player_dx * Ball.VELOCITY_FACTOR
        self.dy = player_dy * Ball.VELOCITY_FACTOR

class Gate(games.Sprite):
    def move(self, player_dx, player_dy):
        pass

class Game:
    pass

pitch_image = games.load_image('pitch.png', transparent=False)

games.screen.background = pitch_image
player_image = games.load_image('player1.png')
the_player = Player(image=player_image,
                    x=games.screen.width / 2,
                    y=games.screen.height / 2)
games.screen.add(the_player)

ball_image = games.load_image('ball.png')
the_ball = Ball(image=ball_image,
                x=220,
                y=210)
games.screen.add(the_ball)

gate_image = games.load_image('gate.png')
gate1 = Gate(image=gate_image,
             y=210,
             right=30)
games.screen.add(gate1)

gate2 = Gate(image=gate_image,
             y=279,
             right=30)
games.screen.add(gate2)
games.screen.mainloop()
