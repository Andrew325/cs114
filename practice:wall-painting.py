print('How wide is the wall?')
width = int(input())
print('How high is the wall?')
height = int(input())
print('How much is a gallon of paint?')
price = int(input())
gallon = 400
wall_size = width * height
wall_size = wall_size // gallon
cost = price * wall_size
print('It will cost $' + str(cost))
