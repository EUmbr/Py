from livewires import games
import random

games.init(screen_width=640, screen_height=480, fps=50)


class Pan(games.Sprite):
    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()

    def check_collide(self):
        for pizza in self.overlapping_sprites:
            pizza.handle_collide()


class Pizza(games.Sprite):
    def update(self):
        if self.right > 640 or self.left < 0:
            self.dx = -self.dx
        if self.bottom > 480 or self.top < 0:
            self.dy = -self.dy


    def handle_collide(self):
        self.x = random.randrange(640)
        self.y = random.randrange(480)


def main():
    wall_image = games.load_image('wall.jpg', transparent=False)
    games.screen.background = wall_image

    pizza_image = games.load_image('pizza.bmp')
    the_pizza = Pizza(image=pizza_image,
                      x=random.randrange(640),
                      y=random.randrange(480),
                      )
    games.screen.add(the_pizza)

    pan_image = games.load_image('pan.bmp')
    the_pan = Pan(image=pan_image,
                  x=games.mouse.x,
                  y=games.mouse.y)

    games.screen.add(the_pan)

    games.mouse.is_visible = False

    games.screen.event_grab = True

    games.screen.mainloop()


if __name__ == '__main__':
    main()
