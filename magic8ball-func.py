import random

print('Magic 8 Ball Fortunes')
print('Reveal your name and recieve a fortune.')
name_for_number = input('Type name ')
rn = len(name_for_number)


def eight_ball(random_number):
    ''' The random number to tell a corresponding fortune.'''
    if random_number == 1:
        return 'Look forward and the path will show you the way.'
    elif random_number == 2:
        return 'Dream big if you have the drive to make it real.'
    elif random_number == 3:
        return 'You will meet someone of signifigance, tomorrow.'
    elif random_number == 4:
        return 'Be creative and your creativity will be rewarded soon.'
    elif random_number == 5:
        return 'Be cautious, misfortune might be on your way.'
    elif random_number == 6:
        return 'Be aware of the signs: they foretell a warning.'
    elif random_number == 7:
        return 'Be happy and be healthy.'
    elif random_number == 8:
        return 'It is your lucky day.'
    elif random_number == 9:
        return 'Try again later...'

rn = random.randint(1,9)
fortune = eight_ball(rn)
print(fortune)
