print('Input amount(cents) to be converted into change.')
change = int(input())
# change = money * 100
quarters = 25
dimes = 10
nickels = 5
pennies = 1
total_quarters = change // 25
change = change - (total_quarters * 25)
total_dimes = change // 10
change = change - (total_dimes * 10)
total_nickels = change // 5
change = change - (total_nickels * 5)
total_pennies = change // 1
change = change - (total_pennies * 1)
print(str(total_quarters) + ' quarters')
print(str(total_dimes) + ' dimes')
print(str(total_nickels) + ' nickels')
print(str(total_pennies) + ' pennies')
