'''
user gives the data like this:
             "kerala-tiruvanathapuram" "karnataka-bangaluru" "tamil nadu-chennai"
you have to separate the states and store in the list states[] and also the separated capitals must be stored in capitals[]
'''

def varArgFunction(*arguments):
    print(arguments)
    states = []
    capitals = []

    for arg in arguments:
        parts = arg.split(' ')
        if len(parts) == 2:
            states = parts[0].strip()
            capitals = parts[1].strip()
            states.append(state)
            capitals.append(capitals)
    return states, capitals


#########################################################################

states_with_capitals =list(input('Enter the states with capital : '))
states_list, capital_list = varArgFunction(states_with_capitals)


print('states: ', states_list)
print('capitals: ', capital_list)
