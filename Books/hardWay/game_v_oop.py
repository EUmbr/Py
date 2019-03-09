def main():
	word = input('Word?\n')
	length = len(word)
	lifes = 8
	guessed = [] 
	tried = []
	win = False
	while lifes > 0 and not win:
		char = input('Char?\n').lower()
		if len(char) != 1:
			print('Type one char')
			continue
		if char in guessed:
			print('this letter is already guessed')
			continue
		if char in tried:
			print('You have already tried this letter')
			continue
		if char in word:
			guessed.append(char)
		else:
			tried.append(char)
			lifes -= 1
		print(' <3 ' * lifes)
		new_word = ''
		for x in word:
			if x not in guessed:
				new_word += '_'
			else:
				new_word += x
		if new_word == word:
			win = True
		print(new_word)
	if lifes == 0:
		print('You lose')
		print('The right word is', word)
	else:
		print('You win')

main()