print("Attack Phase: Type in Spell to cast.")
input()

magic_power = 50

while magic_power > 0:
    print("You casted a spell.")
    magic_power -= 10
    print("MP consumed. " + str(magic_power) + " MP left")
    print("Attack Phase: Type in Spell to cast.")
    input()



print("Attack Phase: Type in Attack to perform.")
input()

hit_points = (50, 40, 30, 20, 10)
current_hp = 50
for current_hp in hit_points:
    print("Damage received.")
    current_hp -= 10
    print(str(current_hp) + " HP remaining.")
    print("Attack Phase: Type in Attack to perform.")
    input()


# for attack in range(5):
#     print("you have ", hp, "hit points remaining")
#     hp -= 10
#     print("You cast a spell")
