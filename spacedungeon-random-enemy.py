import random
print('Enter a movement action to perform.')
action = input()
#def random_enemy(enemy):
    #random_num = random.randint(0,3)
    #return print(enemy[random_num])

#print_enemy()

enemy = ['Space Wraith',
    'Infinite Beast',
    'Void Knight',
    'Invading Eye',
    'Cosmic Storm Eater',
    'Blind Sun Maurader']
if action:
    print('You encountered a ' + enemy[random.randint(0, len(enemy) - 1)])
