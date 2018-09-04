import random

from livewires import games, color

games.init(screen_width=640, screen_height=480, fps=50)

wall_image = games.load_image('wall.jpg', transparent=False)
games.screen.background = wall_image

pizza_image = games.load_image('pizza.bmp')
pizza = games.Sprite(image=pizza_image, x=320, y=240)
games.screen.add(pizza)


def new_score():
    score = games.Message(value='9909567',
                          size=60,
                          color=color.black,
                          x=750,
                          y=30,
                          dx=-1,
                          lifetime=850,
                          after_death=new_score)
    games.screen.add(score)

new_score()

def new_message():
    won_message = games.Message(value='YOU WIN!',
                                size=50,
                                color=color.pink,
                                x=random.randint(40, 600),
                                y=random.randint(10, 470),
                                lifetime=100,
                                after_death=new_message)

    games.screen.add(won_message)


new_message()

games.screen.mainloop()
