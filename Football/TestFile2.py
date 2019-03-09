from livewires import games, color
import math
import random

games.init(screen_width=600, screen_height=489, fps=50)


class Player(games.Sprite):
    VELOCITY_STEP = .03
    VELOCITY_STOP = .1
    VELOCITY_MAX = 3
    image = games.load_image('player1.png')

    def __init__(self, game, x, y):
        super(Player, self).__init__(image=Player.image,
                                     x=x,
                                     y=y)
        self.game = game

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

        if self.overlapping_sprites and (self.dx != 0 or self.dy != 0):
            for sprite in self.overlapping_sprites:
                if str(sprite) == 'Ball':
                    sprite.move(self.dx, self.dy)


class Ball(games.Sprite):
    VELOCITY_FACTOR = 1.8
    image = games.load_image('ball.png')

    def __init__(self, game, x, y):
        super(Ball, self).__init__(image=Ball.image,
                                   x=x,
                                   y=y)
        self.game = game


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

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                if str(sprite) == 'Target':
                    sprite.hit()
                else:
                    self.dx = -self.dx
                    self.dy = -self.dy

    def move(self, player_dx, player_dy):
        self.dx = player_dx * Ball.VELOCITY_FACTOR
        self.dy = player_dy * Ball.VELOCITY_FACTOR


class Target(games.Sprite):
    image = games.load_image('target.png')

    def __init__(self, x, y, game):
        super(Target, self).__init__(image=Target.image,
                                     x=x,
                                     y=y)
        self.game = game

    def __str__(self):
        return 'Target'

    def hit(self):
        self.game.score.value += 10
        self.game.advance()
        self.destroy()


class Game:
    def __init__(self):
        self.sound = games.load_sound('level.wav')

        self.score = games.Text(value=0,
                                size=40,
                                color=color.white,
                                x=games.screen.width / 2,
                                top=5,
                                is_collideable=False)
        games.screen.add(self.score)

        self.player = Player(game=self,
                             x=games.screen.width / 2 - 100,
                             y=games.screen.height / 2)
        games.screen.add(self.player)

        self.ball = Ball(game=self,
                         x=games.screen.width/2,
                         y=games.screen.height/2)
        games.screen.add(self.ball)

    def play(self):
        #games.music.load('theme.mid')
        #games.music.play(-1)
        pitch_image = games.load_image('pitch.png', transparent=False)
        games.screen.background = pitch_image
        self.advance()
        games.screen.mainloop()

    def advance(self):
        BUFFER = 50
        x = self.ball.x
        y = self.ball.y
        while (self.ball.x - x) ** 2 + (self.ball.y - y) ** 2 < BUFFER ** 2:
            x = random.randint(30, games.screen.width - 30)
            y = random.randint(30, games.screen.height - 30)
        new_target = Target(game=self,
                            x=x,
                            y=y)
        games.screen.add(new_target)

        self.sound.play()

def main():
    football = Game()
    football.play()

if __name__ == '__main__':
    main()
