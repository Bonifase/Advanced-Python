"""
Kafka - the advanture game you cannot win
"""

def go_north(position):
    i, j = position
    new_position = (i, j + 1)
    return new_position

def go_east(position):
    i, j = position
    new_position = (i + 1, j)
    return new_position

def go_south(position):
    i, j = position
    new_position = (i, j - 1)
    return new_position

def go_west(position):
    i, j = position
    new_position = (i - 1, j)
    return new_position

def look(position):
    return position

def quit(position):
    return None

def play():

    position = (0, 0)
    alive = True

    while position:

        locations = {
            (0, 0): lambda: print("You are in a maze of twisty passages, all alike."),
            (1, 0): lambda: print("You are on a road in a dark forest. To the north you can see a tower."),
            (1, 1): lambda: print("There is a tall tower here, with no obvious door, A path leads east.")
        }

        try:
            location_action = locations[position]
        except KeyError as e:
            print("There is nothing here.")
        else:
            location_action()

        command = input()

        actions = {
            'N': go_north,
            'E': go_east,
            'S': go_south,
            'W': go_west,
            'L': look,
            'Q': quit
        }

        try:
            command_action = actions[command]
        except KeyError as e:
            print("I don't understand.")
        else:
            position = command_action(position)
