print('Enter a number to have it written.')

number = input()

number = int(number)
tens = number // 10
ones = number % 10



if number == 1:
elif number == 2:
elif number == 3:
elif number == 4:
elif number == 5:
elif number == 6:
elif number == 7:
elif number == 8:
elif number == 9:
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
