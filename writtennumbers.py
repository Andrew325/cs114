print('Enter a number to have it written.')

number = input()

number = int(number)



if number == 1:
    ones = "one"
elif number == 2:
    ones = "two"
elif number == 3:
    ones = "three"
elif number == 4:
    print("four")
elif number == 5:
    print("five")
elif number == 6:
    print("six")
elif number == 7:
    print("seven")
elif number == 8:
    print("eight")
elif number == 9:
    print("nine")
elif number == 10:
    print("ten")
elif number == 11:
    print("eleven")
elif number == 12:
    print("twelve")
elif number == 13:
    print("thirteen")
elif number == 14:
    print("fourteen")
elif number == 15:
    print("fifteen")
elif number == 16:
    print("sixteen")
elif number == 17:
    print("seventeen")
elif number == 18:
    print("eighteen")
elif number == 19:
    print("ninteen")
elif number == 20:
    print("twenty")
elif number >= 20:
    print("twenty-" + str(number % 10))
