# function to get list of directions for traversal

def get_traversal(room_graph, player):

    # this is the directions that the test will follow. 'n', 's', 'e', 'w'
    # whenever we leave room in a new direction we will append that direction to 
    # this traversal_path
    traversal_path = []

    # because we are getting total directions for a player to travel thru each room
    # we need a place to keep all our previous rooms direction as well. 
    # if the room that we are in is an "end node", or doesnt have any rooms attached to
    # it except for the previous room. we will need to back track by "pop" of the last previous
    # room direction and move backwards to the previous room
    # this will contain directions 'n', 's', 'e', 'w'
    previous_directions = []

    # because we are keeping track of directions to back track thru traveled rooms
    # we will need a dictionary that contains the opposite directions. if we go north
    # to a new room, our previous room is in the 'south' direction, so we would append
    # 's' to the previous room. If we went 'west' then we would append 'e' to our previous
    opposite_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

    # we need a queue to add our possible directions that we can move from our current
    # room
    # room_queue = []
    # originally had this as a list, but seems like we need to know each direction as it applies to each room
    room_queue = {}

    # need a place to keep all our visited rooms. Need to visit all rooms before we 
    # are finished traversing
    explored = set()

    while len(explored) < len(room_graph):

        # get the current room id by calling the current room id method from player class
        current_room = player.current_room.id
        print(current_room)
        # print(explored)
        # if the current room is not in the visited set then we need to add it to the
        # the visited set and get the possible directions that we can move
        if current_room not in explored:
            explored.add(current_room)
            
            # i dont think the list is working... its appending a list of lists each time.
            # when we pop off the last item we get a list of directions. We want to be able to 
            # isolate it to a specific direction. so we can use the pop to get the next direction
            # we should go. 
            # # room_queue.append(player.current_room.get_exits())
            room_queue[current_room] = player.current_room.get_exits()

        # if the length of the set of directions of the room_queue is 0. that means there
        # are no exits and we need to back track.
        # to back track we need to travel in the previous direction
        elif len(room_queue[current_room]) == 0:
            
            # previous direction is the last item in previous_directions
            prev_dir = previous_directions.pop()

            # because we are moving backwards we need to add that to our traversal path
            traversal_path.append(prev_dir)

            # actually travel back that direction to the previous room
            player.travel(prev_dir)

        # finally if the current room we are in has been visited then we need to
        # move to another room. Our next direction is stored in our room_queue
        else:

            # next direction is the last item direction in our room_queue directions
            next_dir = room_queue[current_room].pop()

            # add this direction to our traversal path that we will travel
            traversal_path.append(next_dir)

            # need to add the room that we are leaving to the previous directions
            # to do this we will add the value from our opposite directions dictionary
            # that corresponds to the next_dir key
            # i.e if our next_dir == 'n' then the value that corresponds with the 'n' key 
            # in our opposite direction dictionary is 's'
            previous_directions.append(opposite_directions[next_dir])

            # travel to the next room that is in the "next_dir"
            player.travel(next_dir)

    return traversal_path