from livewires import games, color

games.init(screen_width=640, screen_height=480, fps=50)


class Pan(games.Sprite):
    image = games.load_image('pan.bmp')

    def __init__(self):
        super().__init__(image=Pan.image,
                         x=games.mouse.x,
                         bottom=480)
        self.score = games.Text(value=0,
                                size=25,
                                color=color.black,
                                right=630,
                                top=5)
        games.screen.add(self.score)

    def update(self):
        self.x = games.mouse.x

        if self.right > 640:
            self.right = 640

        if self.left < 0:
            self.left < 0

        self.check_catch()

    def check_catch(self):
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = 630
            pizza.handle_collide()


class Pizza(games.Sprite):
    image = games.load_image('pizza.bmp')
    speed = 4

    def __init__(self, x, y):
        super().__init__(image=Pizza.image,
                         x=x,
                         y=y,
                         dx=Pizza.speed,
                         dy=Pizza.speed)

    def update(self):
        if self.top < 0:
            self.dy = -self.dy
        if self.bottom > 480:
            self.end_game()
            self.destroy()
        if self.right > 640 or self.left < 0:
            self.dx = -self.dx

    def handle_collide(self):
        self.dy = -self.dy

    def end_game(self):
        end_message = games.Message(value='GAME OVER',
                                    size=150,
                                    color=color.pink,
                                    x=320,
                                    y=240,
                                    lifetime=250,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


def main():
    wall_image = games.load_image('wall.jpg', transparent=False)
    games.screen.background = wall_image
    the_pan = Pan()
    games.screen.add(the_pan)
    the_pizza = Pizza(320, 240)
    games.screen.add(the_pizza)
    games.mouse.is_visible = False
    games.screen.event_grab = True

    games.screen.mainloop()


if __name__ == '__main__':
    main()
