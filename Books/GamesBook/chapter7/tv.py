class Tv(object):
    def __init__(self, volume = 10, channel = 1):
        self.volume = volume
        self.channel = channel
    def channel_choice(self, channel):
        if 1 <= channel <= 20:
            self.channel = channel
        else:
            print('There is no channel №', channel)
    def volume_choice(self, volume):
        if volume in range(1, 21):
            self.volume = volume
        else:
            print('You cannot choose this level of volume')
    def __str__(self):
        rep = 'Current channel - ' + str(self.channel) + '\n'
        rep += 'Level of volume - ' + str(self.volume)
        return rep
    def ch_up(self):
        self.channel += 1
    def ch_down(self):
        self.channel -= 1
    def v_up(self):
        self.volume += 1
    def v_down(self):
        self.volume -= 1
def main():
    tvset = Tv()
    choice = None
    while choice != '0':
        print('''
        0 - Exit
        1 - Choose channel
        2 - Choose volume
        3 - Up
        4 - Down
        5 - Status
        ''')
        choice = input('Your choice...\n')
        if choice == '0':
            print('Goodbye')
        elif choice == '1':
            tvset.channel_choice(int(input('Channel №...\n')))
        elif choice == '2':
            tvset.volume_choice(int(input('Level of volume...\n')))
        elif choice == '3':
            setting = input('What would you like to change\n1 - Channel\n2 - Volume\n')
            if setting == '1':
                tvset.ch_up()
            elif setting == '2':
                tvset.v_up()
            else:
                print('There is not setting like', setting, '\n')
        elif choice == '4':
            setting = input('What would you like to change\n1 - Channel\n2 - Volume\n')
            if setting == '1':
                tvset.ch_down()
            elif setting == '2':
                tvset.v_down()
            else:
                print('There is not setting like', setting, '\n')
        elif choice == '5':
            print(tvset)
        else:
            print('Sorry, but ', choice, ' is not a valid choice\n')

main()
