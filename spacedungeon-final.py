import random
import sys

print('Welcome to Space Dungeon: Revelation\'s Voyage\n')

print('In this game, you are a passenger on the frigate starship, the Revelation, \
 coming back from a recent voyage. Carrying valuable cargo, the Revelation has come \
 under surprise attack by alien creatures seeking to claim their prize. \
 They board the ship and take over, killing crew members and passengers alike. \
 You take on the task to fight your way to the helm of the ship and get help.\n')

"""text based game where user makes decisions which affect a series of
encounters with 'enemies'"""


player = {
'HP': 100,
'attack': 100,
'defense': 100,
'name': '',
'player_class': ''
}

enemy1 = {
'HP': 70,
'attack': 60,
'defense': 60,
'name': 'Void Knight, Ibrixal'
}

enemy2 = {
'HP': 50,
'attack': 50,
'defense': 50,
'name': 'Space Wraith, Adar Tul'
}

enemy3 = {
'HP': 50,
'attack': 50,
'defense': 50,
'name': 'Invading Marauder, Getryth'
}

enemy4 = {
'HP': 50,
'attack': 50,
'defense': 50,
'name': 'Sun Beast, Paruth'
}

enemy5 = {
'HP': 100,
'attack': 70,
'defense': 70,
'name': 'Astral Demon Drake'
}
player['name'] = input('Type Name: \n')

print('Welcome',player['name'], 'Please select a class from the choices below.\n')
print('Soldier - Trained fighters with formal military training.\n \
Weapon - Fusion Core Assault Rifle\n')
print('Mercenary - Skillful warriors for hire with a sketchy past.\n \
Weapon - Dual Avarice-47 Handguns\n')
print('Wizard - Magic users with high degrees of intelligence and power.\n \
Weapon - LR-20 Pistol and Enchanted Spear\n')
print('Knight - Armored fighters with a code of honor.\n \
Weapon - .45 Caliber Heat Claymore and Light Shield\n')
print('Technician - Skilled engineers with technical based combat abilities and expertise.\n \
Weapon - Multi-faceted Welding Tool\n')
print('Civilian - Very little experience in combat, but strong in will.\n \
Weapon - 2490 Handgun\n')

player['player_class'] = input('Type Class: \n')



def game_over(player):
    print("GAME OVER -- ",player['name'], "You and everyone on the Revelation has died to the invaders.\n \
    They now take over and plot a course to Earth. Your fate has been sealed.", player['name'], "HP:", player['HP'])
    return sys.exit()


def get_item(player):
    item_list = ["a First Aid.", "Regenerative Paste.", "Nanomachines, son."]
    if player['HP'] <= 40:
        print("You found",item_list[2], "Your health increased by",
        (abs(player['HP'] - 100)), "HP.")
        player['HP'] += (abs(player['HP'] - 100))
    elif player['HP'] <= 60:
            print("You found",item_list[1], "Your health increased by",
            (40), "HP.")
            player['HP'] += (abs(player['HP'] + 40))
    elif player['HP'] <= 80:
        print("You found",item_list[0], "Your health increased by",
        (20), "HP.")
        player['HP'] += (abs(player['HP'] + 20))
        return player




    """print("You find a ", item_list[random.randint(0, 2)], "your health increased by ",
    (abs(player['HP'] - 100)), "HP")
    player['HP'] += (abs(player['HP'] - 100))
    return player"""


def attack(opponent):
    rand_damage = random.randint(8, 38)
    opponent['HP'] -= rand_damage
    if rand_damage >= 27:
        print(rand_damage, 'critical damage!')
    else:
        print(rand_damage, 'damage')
    return opponent


def fight(oppo1, oppo2):
    print('You encounter',oppo2['name'])
    while (oppo1['HP'] > 0) and (oppo2['HP'] > 0):
        print(oppo1['name'],"attacks",oppo2['name'])
        attack(oppo2)
        if oppo2['HP'] <= 0:
            print(oppo1['name'], "wins.",oppo2['name'], "falls.")
        else:
            print(oppo2['name'],"attacks",oppo1['name'])
            attack(oppo1)
        if oppo1['HP'] <= 0:
            print(oppo2['name'],"defeats",oppo1['name'])
            game_over(oppo1)
    print(oppo1['name'], 'HP:', oppo1['HP'])
    print(oppo2['name'], 'HP:', oppo2['HP'])


def encounter(player, opponent):
    if player['HP'] > 70:
        fight(player, opponent)
        # if player['HP'] <= 0:
        #     return game_over(player)
        input('Press Enter to continue')
    #elif opponent['name'] == 'Space Wraith, Adar Tul':
        #fight(player, opponent)
        #input('Press Enter to continue')
        # return player
    elif opponent['name'] == 'Astral Demon Drake':
            fight(player, opponent)
            input('Press Enter to continue')
            # return player
    else:
        get_item(player)
        input('Press Enter to continue')



"""there are 5 encounters, each encounter offers an option to open a door,
the door will either have an enemy or an item"""


def main():
    # fight(player, enemy1)

    # get_item(player)
    print('You find a set of weapons and take up arms, making your way through a long corridor on the ship. Up ahead you find...\n\n')
    input('Press Enter to continue')
    encounter(player, enemy4)
    print('At the end of the corridor, you open the door. On the other side...\n\n')
    input('Press Enter to continue')
    encounter(player, enemy2)
    print('Now, you find yourself in a large room. You see...\n\n')
    input('Press Enter to continue')
    encounter(player, enemy3)
    print('You finally make your way to the bridge. What you find at the helm is...\n\n')
    input('Press Enter to continue')
    encounter(player, enemy1)
    print('You take a moment to rest, but the entire ship starts to shake from impact damage.\
    You look out the windows to see something big encircling the ship.\
    The ship controls unlocks defensive measures and releases armaments. You get ready to fight...\n\n')
    input('Press Enter to continue')
    encounter(player, enemy5)
    print('The Drake takes a cannon shot to the face and falls, drifting into deep space.')
    input('Press Enter to continue')
    if player['HP'] <= 0:
        game_over(player)
    else:
        print("You have taken back the Revelation and sent an emergency signal to Earth.\n \
     Armed forces arrive in full to eliminate the remaining invaders and rescue the survivors.\n \
     Everyone is heading home.\n \
     You have survived. -- WINNER", player['name'], "HP:", player['HP'])


if __name__ == "__main__":
    # print("Executing as main program")
    # print("Value of __name__ is: ", __name__)
    main()
