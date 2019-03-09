from livewires import games

games.init(screen_width=600, screen_height=489, fps=50)

pitch_image = games.load_image('pitch.png', transparent=False)
games.screen.background = pitch_image

goal_images = ['1.png',
               '2.png',
               '3.png',
               '4.png',
               '5.png',
               '6.png',
               '7.png',
               '8.png',
               '9.png',
               '10.png',
               '11.png',
               '10.png',
               '9.png',
               '8.png',
               '7.png',
               '6.png',
               '5.png',
               '4.png',
               '3.png',
               '2.png']

goal = games.Animation(images=goal_images,
                       x=300,
                       y=290,
                       repeat_interval=8,
                       n_repeats=0,
                       is_collideable=False)

games.screen.add(goal)

games.screen.mainloop()