from livewires import games

games.init(screen_width=640, screen_height=480, fps=50)

missile_sound = games.load_sound('missile.wav')

games.music.load('theme.mid')

choice = None
while choice != 0:
    print(
        '''
        Sound and Music
        0 - Exit
        1 - Missile sound
        2 - Repeat missile sound
        3 - Stop missile sound
        4 - Music theme
        5 - Repeat music theme
        6 - Stop music theme
        '''
        )
    choice = input('Your choice:')
    print()

    if choice == 0:
        print('GOODBYE')

    elif choice == '1':
        missile_sound.play()

    elif choice == '2':
        loop = int(input())
        missile_sound.play(loop)

    elif choice == '3':
        missile_sound.stop()

    elif choice == '4':
        games.music.play()

    elif choice == '5':
        loop = int(input())
        games.music.play(loop)

    elif choice == '6':
        games.music.stop()

    else:
        print('Try again')

input()