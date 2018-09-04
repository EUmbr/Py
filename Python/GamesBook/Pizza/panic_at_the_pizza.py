from livewires import games, color
import random

games.init(screen_width=640, screen_height=480, fps=50)


def chef_more():
    the_chef = Chef()
    games.screen.add(the_chef)


class Pan(games.Sprite):
    image = games.load_image('pan.bmp')
    flag = False
    def __init__(self):
        super().__init__(image=Pan.image,
                         x=games.mouse.x,
                         bottom=480)
        self.score = games.Text(value=0,
                                size=25,
                                color=color.black,
                                top=5,
                                right=630)
        games.screen.add(self.score)

    def update(self):
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > 640:
            self.right = 640

        self.check_catch()

    def check_catch(self):
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = 630
            pizza.handle_caught()
        if self.score.value == 500 and not self.flag:
            chef_more()
            self.flag = True


class Pizza(games.Sprite):
    image = games.load_image('pizza.bmp')
    speed = 2

    def __init__(self, x, y=90):
        super().__init__(image=Pizza.image,
                         x=x,
                         y=y,
                         dy=Pizza.speed)

    def update(self):
        if self.bottom > 480:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        self.destroy()

    def end_game(self):
        end_message = games.Message(value='GAME OVER',
                                    size=150,
                                    color=color.pink,
                                    x=320,
                                    y=240,
                                    lifetime=250,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


class Chef(games.Sprite):
    image = games.load_image('chef.bmp')

    def __init__(self, y=55, speed=2, odds_change=100):
        super().__init__(image=Chef.image,
                         x=320,
                         y=y,
                         dx=speed)

        self.odds_change = odds_change
        self.time_till_drop = 0

    def update(self):
        if self.left < 0 or self.right > 640:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
        self.check_drop()

    def check_drop(self):
        if self.time_till_drop > 0:
            self.time_till_drop -= 1
        else:
            new_pizza = Pizza(x=self.x)
            games.screen.add(new_pizza)
            self.time_till_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1


def main():
    wall_image = games.load_image('wall.jpg', transparent=False)
    games.screen.background = wall_image
    the_chef = Chef()
    games.screen.add(the_chef)
    the_pan = Pan()
    games.screen.add(the_pan)
    games.mouse.is_visible = False
    games.screen.event_grab = True

    games.screen.mainloop()


if __name__ == '__main__':
    main()
