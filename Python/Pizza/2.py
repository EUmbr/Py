from livewires import games

games.init(screen_width=640, screen_height=480, fps=50)


class Pizza(games.Sprite):
    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        if self.top < 0 or self.bottom > games.screen.height:
            self.dy = -self.dy


def main():
    wall_image = games.load_image('wall.jpg', transparent=False)
    games.screen.background = wall_image

    pizza_image = games.load_image('pizza.bmp')
    the_pizza = Pizza(image=pizza_image,
                      x=320,
                      y=240,
                      dx=2,
                      dy=2,
                      is_collideable=True)
    the_pizza2 = Pizza(image=pizza_image,
                       x=145,
                       y=455,
                       dx=2,
                       dy=2,
                       is_collideable=True)
    games.screen.add(the_pizza)
    games.screen.add(the_pizza2)
    games.screen.mainloop()


if __name__ == '__main__':
    main()
