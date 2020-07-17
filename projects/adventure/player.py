from util import Queue, Stack, Graph
from ast import literal_eval


class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
    def travel(self, direction, show_rooms=False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")

    def sanityMaze(self):
        pass
        
    def readMaze(self, map_file):
        # Loads the map into a dictionary
        room_graph=literal_eval(open(map_file, "r").read())
        return room_graph

    def travelMaze(self, starting_vertex, visited=None):
        room_graph = self.readMaze("maps/main_maze.txt")

        traversal_path = [] #>>> GLOBAL

        idStack = Stack()
        idStack.push(starting_vertex.id) # init

        if visited is None: # recursive attempt (NOT IMPLEMENTED)
            visited = set()
        print(f"\nYou are standing in room {starting_vertex.id} at {starting_vertex.description}\n") #> Flavor

        while len(visited) < len(room_graph):
            roomStack = Stack() # stack for next rooms
            current_room = idStack.stack[-1]
            visited.add(current_room)

            print(f"You visited room {current_room} ({len(visited)}/{len(room_graph)})  -----  time: {len(traversal_path)}")
            print(f"Description: {room_graph[current_room]}\n")

            possible_direction = room_graph[current_room][1]
            for direction, room_id in possible_direction.items():
                if room_id not in visited: # 
                    roomStack.push(room_id)
            if roomStack.size() > 0:
                current_room = roomStack.stack[0]
                idStack.push(current_room)
                print(f"Room Stack: {roomStack.stack}")
                print(f"Id Stack: {idStack.stack}")
            else:
                current_room = idStack.stack[-2]
                print(f"Room Stack: {roomStack.stack}")
                print(f"Id Stack: {idStack.stack}")
                # print(stack.stack)
                idStack.pop()
            for direction, room in possible_direction.items():
                if room == current_room:
                    traversal_path.append(direction)
        print(f"You are now standing in room {current_room}\n.")
        return traversal_path