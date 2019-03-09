from livewires import games


games.init(screen_width=640, screen_height=480, fps=50)


class Ship(games.Sprite):
    """Moving spaceship"""

    def update(self):
        if games.keyboard.is_pressed(games.K_w):
            self.y -= 1
        if games.keyboard.is_pressed(games.K_s):
            self.y += 1
        if games.keyboard.is_pressed(games.K_d):
            self.x += 1
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 1
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += 1
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= 1
        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270


def main():
    earth_image = games.load_image('earth.jpg', transparent=False)
    games.screen.background = earth_image
    ship_image = games.load_image('ship.bmp')
    the_ship = Ship(image=ship_image,
                    x=games.screen.width / 2,
                    y=games.screen.height / 2)
    games.screen.add(the_ship)
    explosion_files = ['explosion1.bmp',
                       'explosion2.bmp',
                       'explosion3.bmp',
                       'explosion4.bmp',
                       'explosion5.bmp',
                       'explosion6.bmp',
                       'explosion7.bmp',
                       'explosion8.bmp',
                       'explosion9.bmp']

    explosion = games.Animation(images=explosion_files,
                                x=480,
                                y=240,
                                n_repeats=0,
                                repeat_interval=5)
    games.screen.add(explosion)

    games.screen.mainloop()


if __name__ == '__main__':
    main()
