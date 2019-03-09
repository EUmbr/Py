from time import sleep
from livewires import games, color


games.init(screen_width=852, screen_height=480, fps=60)


class Rocket(games.Sprite):
    VELOCITY_FACTOR = 4
    image = games.load_image('rocket.jpg', transparent=False)

    def __init__(self, x, y):
        super(Rocket, self).__init__(image=Rocket.image,
                                     x=x,
                                     y=y)


class Rocket1(Rocket):
    def update(self):
        self.dx = 0
        self.dy = 0
        if games.keyboard.is_pressed(games.K_s):
            self.dy = self.VELOCITY_FACTOR
        if games.keyboard.is_pressed(games.K_w):
            self.dy = -self.VELOCITY_FACTOR
        if (games.keyboard.is_pressed(games.K_w) and
           games.keyboard.is_pressed(games.K_s)):
            self.dx = 0
            self.dy = 0
        if self.top < 0:
            self.top = 0
        if self.bottom > games.screen.height:
            self. bottom = games.screen.height


class Rocket2(Rocket):
    def update(self):
        self.dx = 0
        self.dy = 0
        if games.keyboard.is_pressed(games.K_DOWN):
            self.dy = self.VELOCITY_FACTOR
        if games.keyboard.is_pressed(games.K_UP):
            self.dy = -self.VELOCITY_FACTOR
        if (games.keyboard.is_pressed(games.K_UP) and
           games.keyboard.is_pressed(games.K_DOWN)):
            self.dx = 0
            self.dy = 0
        if self.top < 0:
            self.top = 0
        if self.bottom > games.screen.height:
            self. bottom = games.screen.height


class Ball(games.Sprite):
    VELOCITY_FACTOR = 4
    SIZE_FACTOR = 2
    image = games.load_image('ball.png')

    def __init__(self, game, x, y):
        super(Ball, self).__init__(image=Ball.image,
                                   x=x,
                                   y=y)
        self.dx = self.VELOCITY_FACTOR
        self.dy = self.VELOCITY_FACTOR
        self.game = game

    def __str__(self):
        return 'Ball'

    def update(self):
        if self.right > games.screen.width + self.SIZE_FACTOR:
            self.right = games.screen.width + self.SIZE_FACTOR
            self.game.advance()
        if self.top < -self.SIZE_FACTOR:
            self.top = -self.SIZE_FACTOR
            self.dy = -self.dy
        if self.left < -self.SIZE_FACTOR:
            self.left = -self.SIZE_FACTOR
            self.game.advance()
        if self.bottom > games.screen.height + self.SIZE_FACTOR:
            self.bottom = games.screen.height + self.SIZE_FACTOR
            self.dy = -self.dy

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                self.dx = -self.dx


class Game:
    def __init__(self):
        self.rocket1 = Rocket1(x=30, y=games.screen.height // 2)
        games.screen.add(self.rocket1)

        self.rocket2 = Rocket2(x=822, y=games.screen.height // 2)
        games.screen.add(self.rocket2)

        self.ball = Ball(self, x=games.screen.width / 2,
                         y=games.screen.height / 2)
        games.screen.add(self.ball)

    def play(self):
        table_image = games.load_image('table.jpg', transparent=False)
        games.screen.background = table_image
        games.screen.mainloop()

    def advance(self):
        self.ball.x = games.screen.width / 2
        self.ball.y = games.screen.height / 2
        sleep(1)


def main():
    tennis = Game()
    tennis.play()


if __name__ == '__main__':
    main()
