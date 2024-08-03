#4 - Harry

'''
Algorithm:
1. input = number of gold coins in Harry's Bag, 2nd line = denoting worth of gold coins, 3rd for instructions - Harry or Remove , 4th - value of x to sleep
2. check instruction if it harry or remove
3. output - print the number of coins in the Monk's
 bag, the first time their worth becomes equal to X

'''


num_of_goldcoins_harrys_bag = int(input('Enter the number of coins in Harry\'s bag :'))
coins = list(input(f'Enter the worth {num_of_goldcoins_harrys_bag} in Harry\s bag:'))
num_of_inst = int(input('Enter the number of instructions:'))
x = int(input('Enter the worth should be in bag for Monk to sleep:'))
instructions = []

for j in range(num_of_inst):
    instructions.append(input())

print('Instructions = ', instructions)

def monk_bag_to_sleep(N, coins, Q, X, instructions):
    harry_bag = coins[::-1]  
    monk_bag = []
    monk_total = 0
    coin = 0
    
    for instruction in instructions:
        if instruction == 'Harry':
            if harry_bag:
                coin = harry_bag.pop()
                monk_bag.append(coin)
                monk_total += coin
                if monk_total == X:
                    print(len(monk_bag))
                    return
        elif instruction == 'Remove':
            if monk_bag:
                coin = monk_bag.pop()
                monk_total -= coin

monk_bag_to_sleep(num_of_goldcoins_harrys_bag, coins, num_of_inst, x, instructions)

print(monk_bag_to_sleep)