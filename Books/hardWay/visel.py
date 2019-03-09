def main():
    instructions()
    start_game()
    game()


def instructions():
    print('Welocome!\nIt is a game!')


def start_game():
    word = input('Type a world, please\n').lower
    length = len(word)
    guess = '_' * length
    lifes = 8


def printing():
    print(' <3 ' * lifes, word, sep='\n')

def game():
	while length != 0 or lifes != 0:
		printing()
		chooser()
	if lifes == 0:
		lose()
	else:
		win()

def chooser():
	letter = input('Type a letter').lower
	if letter in word:
		index = word.index(letter)
		new_word = word[:index] + letter + word[index+1:]
		length -= 1

def win():
	print('You win!')

def lose():
	print('You lose')


main()

