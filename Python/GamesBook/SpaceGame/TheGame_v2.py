import math
import random

from livewires import games, color

games.init(screen_width=640, screen_height=480, fps=50)


class Wrapper(games.Sprite):
    def update(self):
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        self.destroy()


class Collider(Wrapper):
    def update(self):
        super(Collider, self).update()
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        new_explosion = Explosion(self.x, self.y)
        games.screen.add(new_explosion)
        self.destroy()


class Asteroid(Wrapper):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL: games.load_image('asteroid_small.bmp'),
              MEDIUM: games.load_image('asteroid_med.bmp'),
              LARGE: games.load_image('asteroid_big.bmp')}
    SPEED = 2
    SPAWN = 2
    POINTS = 30
    total = 0

    def __init__(self, game, x, y, size):
        super(Asteroid, self).__init__(
            image=Asteroid.images[size],
            x=x,
            y=y,
            dx=random.choice([-1, 1]) * Asteroid.SPEED * random.random() / size,
            dy=random.choice([-1, 1]) * Asteroid.SPEED * random.random() / size)
        self.size = size
        self.game = game
        Asteroid.total += 1

    def die(self):
        Asteroid.total -= 1
        self.game.score.value += Asteroid.POINTS // self.size
        self.game.score.right = games.screen.width - 10

        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(game=self.game, x=self.x, y=self.y, size=self.size - 1)
                games.screen.add(new_asteroid)
        super(Asteroid, self).die()
        if Asteroid.total == 0:
            self.game.advance()


class Ship(Collider):
    image = games.load_image('ship.bmp')
    sound = games.load_sound('thrust.wav')
    ROTATION_SPEED = 3
    VELOCITY_STEP = .05
    MISSILE_DELAY = 25
    VELOCITY_MAX = 3

    def __init__(self, game, x, y):
        super(Ship, self).__init__(image=Ship.image, x=x, y=y)
        self.missile_wait = 0
        self.game = game

    def update(self):
        super(Ship, self).update()

        self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
        self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)

        if self.missile_wait > 0:
            self.missile_wait -= 1

        if games.keyboard.is_pressed(games.K_w):
            Ship.sound.play()
            self.dy -= Ship.VELOCITY_STEP
        if games.keyboard.is_pressed(games.K_s):
            Ship.sound.play()
            self.dy += Ship.VELOCITY_STEP
        if games.keyboard.is_pressed(games.K_d):
            Ship.sound.play()
            self.dx += Ship.VELOCITY_STEP
        if games.keyboard.is_pressed(games.K_a):
            Ship.sound.play()
            self.dx -= Ship.VELOCITY_STEP
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle, self.dx, self.dy)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY

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

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        super(Ship, self).die()
        self.game.end()


class Missile(Collider):
    image = games.load_image('missile.bmp')
    sound = games.load_sound('missile.wav')
    BUFFER = 45
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle, ship_dx, ship_dy):
        Missile.sound.play()
        angle = ship_angle * math.pi / 180
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        x = ship_x + buffer_x
        y = ship_y + buffer_y
        dx = ship_dx + Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = ship_dy + Missile.VELOCITY_FACTOR * -math.cos(angle)
        super(Missile, self).__init__(image=Missile.image,
                                      x=x, y=y,
                                      dx=dx, dy=dy)
        self.lifetime = Missile.LIFETIME

    def update(self):
        super(Missile, self).update()

        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()


class Explosion(games.Animation):
    sound = games.load_sound('explosion.wav')
    images = ['explosion1.bmp',
              'explosion2.bmp',
              'explosion3.bmp',
              'explosion4.bmp',
              'explosion5.bmp',
              'explosion6.bmp',
              'explosion7.bmp',
              'explosion8.bmp',
              'explosion9.bmp']

    def __init__(self, x, y):
        super(Explosion, self).__init__(images=Explosion.images,
                                        x=x, y=y,
                                        repeat_interval=5,
                                        n_repeats=1,
                                        is_collideable=False)
        Explosion.sound.play()


class Game:
    def __init__(self):
        self.level = 0
        self.sound = games.load_sound('level.wav')

        self.score = games.Text(value=0,
                                size=30,
                                color=color.white,
                                top=5,
                                right=games.screen.width - 10,
                                is_collideable=False)
        games.screen.add(self.score)

        self.ship = Ship(game=self,
                         x=games.screen.width / 2,
                         y=games.screen.height / 2)
        games.screen.add(self.ship)

    def play(self):
        games.music.load('theme.mid')
        games.music.play(-1)
        earth_image = games.load_image('earth.jpg', transparent=False)
        games.screen.background = earth_image
        self.advance()
        games.screen.mainloop()

    def advance(self):
        self.level += 1
        BUFFER = 150

        for i in range(self.level):
            x = self.ship.x
            y = self.ship.y
            while (self.ship.x - x) ** 2 + (self.ship.y - y) ** 2 < BUFFER ** 2:
                x = random.randrange(games.screen.width)
                y = random.randrange(games.screen.height)
            new_asteroid = Asteroid(game=self,
                                    x=x, y=y,
                                    size=Asteroid.LARGE)
            games.screen.add(new_asteroid)

        level_message = games.Message(value='Level' + str(self.level),
                                      size=40,
                                      color=color.yellow,
                                      x=games.screen.width / 2,
                                      y=games.screen.height / 10,
                                      lifetime=3 * games.screen.fps,
                                      is_collideable=False)
        games.screen.add(level_message)
        if self.level > 1:
            self.sound.play()

    def end(self):
        end_message = games.Message(value='Game Over',
                                    size=100,
                                    color=color.pink,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=100 * games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
        games.screen.add(end_message)


def main():
    astrocrash = Game()
    astrocrash.play()


if __name__ == '__main__':
    main()
