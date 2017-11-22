import random

print('Magic 8 Ball Fortunes')
print('Reveal your name and recieve a fortune.')
input('Your name: ')
random_fortune_number = random.randint(0,8)
print(random_fortune_number)

''' The random number to tell a corresponding fortune.'''

fortune = ['Look forward and the path will show you the way.',
'Dream big if you have the drive to make it real.',
'You will meet someone of signifigance, tomorrow.',
'Be creative and your creativity will be rewarded soon.',
'Be cautious, misfortune might be on your way.',
'Be aware of the signs: they foretell a warning.',
'Be happy and be healthy.',
'It is your lucky day.',
'Try again later...']

def eight_ball(random_fortune_number):
    return print(fortune[random_fortune_number])

eight_ball(random_fortune_number)
