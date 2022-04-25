# ---------------------------------------------------------------------------------------------------------
# Jessica Ayer
# SNHU IT-140: Introduction to Scripting Text Based Game
# 05/15/2021
# ---------------------------------------------------------------------------------------------------------

# The dictionary links a room to other rooms and places items in each room.
rooms = {
    'in the front yard': {'south': 'at the deli', 'west': 'at home', 'north': "at the neighbor's house",
                          'east': 'at the dog park', 'item': 'no items to get'},
    'at the deli': {'north': 'in the front yard', 'east': 'at the dog groomer', 'item': 'bones'},
    'at the dog groomer': {'west': 'at the deli', 'north': 'at the veterinary office', 'item': 'bandannas'},
    'at the veterinary office': {'south': 'at the dog groomer', 'item': 'treats'},
    'at home': {'east': 'in the front yard', 'item': 'food'},
    "at the neighbor's house": {'south': 'in the front yard', 'east': 'at the beach', 'item': 'water'},
    'at the beach': {'west': "at the neighbor's house", 'item': 'the dog catcher'},  # Villain
    'at the dog park': {'west': 'in the front yard', 'north': 'at the pet store', 'item': 'balls'},
    'at the pet store': {'south': 'at the dog park', 'item': 'ropes'}
}
# Start player in Front Yard.
current_room = 'in the front yard'
inventory = {'items': []}


# instructions function
def print_instruction():
    print('Instructions:')
    print('Use the move commands to navigate between the different locations. Use the get command to collect the\n'
          'items in each location. Collect all seven items before running into the dog catcher to win the game.\n')
    print('Move commands: go north, go south, go east, go west')
    print("Get command: get 'item' (bones, bandannas, treats, food, water, balls, ropes)")
    print('Type exit to quit the game.')


# stats function
def print_stats():
    print('\n8=8 8=8 8=8 8=8 8=8 8=8\n')
    print(name, 'is', current_room)
    print('Inventory:', inventory)


# Introduction and instructions
print('\n8=8 8=8 8=8 8=8 8=8 8=8')
print('  Dog Adventure Game')
print('8=8 8=8 8=8 8=8 8=8 8=8\n')
print_instruction()
print('\n8=8 8=8 8=8 8=8 8=8 8=8\n')
name = input("What is your dog's name?\n")
print(name, 'was  left at home while the family went to work. The last person to leave accidentally left the front\n'
            'yard gate open so', name, 'decided to go on an adventure. Help', name, 'navigate the neighborhood and\n'
            'collect toys and treats before getting caught by the dog catcher. Woof!')

# start the game
print_stats()
user_input = input('Enter your move:')


# create loop to play the game
while user_input != 'exit':                                # exit loop
    next_move = user_input.split(' ')
    next_move[0] = next_move[0].lower()
    while len(inventory['items']) != 7:                    # play until all items are collected
        if next_move[0] == 'go':                           # go command loop
            move = next_move[-1].lower()
            if move in rooms[current_room]:                # inner loop valid move
                current_room = rooms[current_room][move]
                item_to_get = rooms[current_room]['item']
                if rooms[current_room]['item'] == 'the dog catcher':        # lose game
                    print('\n8=8 8=8 8=8 8=8 8=8 8=8\n')
                    print('Oh no!, The dog catcher saw', name, 'the adventure is over.\n Thank you for playing. \n'
                          'Goodbye!')
                    print('\n8=8 8=8 8=8 8=8 8=8 8=8\n')
                    exit()
                else:                                       # next move
                    print_stats()
                    print(name, 'sees', item_to_get, '\n')
                    user_input = input('Enter your move:')
                    next_move = user_input.split(' ')
                    move = next_move[-1].lower()
            else:                                           # loop for invalid move command
                print(name, "can't go that way!\n")
                user_input = input('Enter your move:')
                next_move = user_input.split(' ')
                move = next_move[-1].lower()
        elif next_move[0] == 'get':                         # get command loop
            get_item = next_move[-1].lower()
            if get_item in rooms[current_room]['item']:     # get item loop
                item_to_get = rooms[current_room]['item']
                if item_to_get != 'nothing to get':         # add item to inventory
                    inventory['items'].append(get_item)
                    rooms[current_room]['item'] = 'nothing to get'
                    print_stats()
                else:                                       # invalid get item loop
                    print('There are no items here.')
                    user_input = input('Enter your move:')
                    next_move = user_input.split(' ')
                    get_item = next_move[-1].lower()
            else:                                           # invalid get command
                user_input = input('Enter your move:')
                next_move = user_input.split(' ')
                get_item = next_move[-1].lower()
        else:
            print(name, "can't do that!\n")                 # invalid command
            user_input = input('Enter your move:')
            next_move = user_input.split(' ')
    print('\n8=8 8=8 8=8 8=8 8=8 8=8\n')                    # winner script
    print('Congratulations!\nYou helped', name, 'find all of the items without getting caught by the dog catcher.')
    print('Thank you for playing.')
    print('Goodbye!')
    exit()
# exit script
print('\n8=8 8=8 8=8 8=8 8=8 8=8\n')                        # exit script
print('Thank you for playing.')
print('Goodbye!')
exit()
