import random
print('Magic 8 Ball Fortunes')
print('Reveal your name and recieve a fortune.')
input()
random_number = random.randint(1,9)
print(random_number)
if random_number == 1:
    print('Look forward and the path will show you the way.')
elif random_number == 2:
    print('Dream big if you have the drive to make it real.')
elif random_number == 3:
    print('You will meet someone of signifigance tomorrow.')
elif random_number == 4:
    print('Be creative and your creativity will be rewarded soon.')
elif random_number == 5:
    print('Be cautious, misfortune might be on your way.')
elif random_number == 6:
    print('Be aware of the signs: they foretell a warning.')
elif random_number == 7:
    print('Be happy and be healthy.')
elif random_number == 8:
    print('It is your lucky day.')
elif random_number == 9:
    print('Try again later...')
