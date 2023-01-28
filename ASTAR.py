from math import floor, inf, sqrt
import random


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position



# for i in range(len(harta)):
#     print (harta[i])


def A_Star(start,goal,maze):

    start_pos = (start%rr, start%k)
    start_node = Node(None,start_pos)

    start_node.g = start_node.h = start_node.f = 0


    goal_pos = (goal%rr,goal%k)
    end_node = Node(None, goal_pos)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []
    start_node.h = sqrt(((start_node.position[0] - end_node.position[0]) ** 2) + ((start_node.position[1] - end_node.position[1]) ** 2)) #H Score, Squared Euclidian Distance
    start_node.f = start_node.h
    open_list.append(start_node)
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node.h == 0:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
                
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] == 'X':
                continue
            

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        
        for child in children:
            inClosedList = False
            inOpenList = False
            # Child is on the closed list
            for closed_child in closed_list:
                if child.position == closed_child.position:
                    inClosedList = True
                    break

            if(inClosedList):
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1 # G-Score
            child.h = sqrt(((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)) #H Score, Euclidian Distance
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child.position == open_node.position and child.f > open_node.f:
                    inOpenList = True
                    break
            
            if(inOpenList):
                continue

            # Add the child to the open list
            open_list.append(child)
        
        open_list.sort(key= lambda x: x.f)
    
    print("No solution found!!!")
    return 0


# harta =[['X', '0', '0', '0', '0', '0', '0', 'X', '0', '0'],
#         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#         ['0', '0', '0', '0', 'X', '0', '0', '0', '0', '0'],
#         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#         ['0', '0', '0', '0', '0', '0', 'X', '0', '0', '0'],
#         ['X', '0', 'G', '0', '0', '0', '0', '0', '0', '0'],
#         ['0', '0', '0', '0', '0', '0', '0', '0', 'X', '0'],
#         ['0', '0', '0', '0', '0', '0', '0', '0', 'X', '0'],
#         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
#         ['X', 'X', 'X', 'X', 'X', '0', '0', '0', 'X', '0'],
#         ['0', '0', '0', '0', '0', 'S', '0', '0', '0', '0']]

# harta = [['0', '0', '0', 'X', '0'],
#          ['0', '0', '0', '0', '0'],
#          ['0', '0', '0', '0', '0'],
#          ['0', '0', '0', '0', 'X'],
#          ['0', '0', '0', '0', 'X'],
#          ['X', '0', '0', '0', '0'],
#          ['0', 'X', 'X', 'X', '0'],
#          ['0', 'X', 'X', 'X', '0']]
# start = 20
# goal = 39

harta = []
#Parameters
rr = 6 #Rreshtat
k = 6 #Kolonat
obsNumber = 5 #Numri i bllokadave  


for i in range(rr):
    harta.append([])
    for j in range(k):
        harta[i].append('0')

goal = random.randint(0,rr*k-1)
lista = list(range(rr*k))
lista.remove(goal)
start = random.sample(lista,1)[0]


lista.remove(start)

  

obs = list(random.sample(lista,obsNumber))

# for i in obs:
#     harta[i%rr][i%k] = 'X'
for i in range(obsNumber):
        rr1 = random.randint(0, rr - 1)
        k1 = random.randint(0, k - 1)
        harta[rr1][k1] = 'X'

harta [goal%rr][goal%k] = 'G'
harta [start % rr][start%k] = 'S'


harta [goal % rr ][goal%k] = 'G'
harta [start % rr ][start%k] = 'S'

# harta = [['G', '0', '0', '0', 'X', '0'],
#          ['X', '0', '0', '0', '0', '0'],
#          ['0', '0', '0', '0', '0', '0'],
#          ['0', '0', '0', 'X', '0', 'X'],
#          ['0', '0', '0', '0', 'S', '0'],
#          ['0', '0', '0', '0', '0', '0']]
# goal = 0
# start = 28
# start = 143
# goal = 62

for i in range(len(harta)):
        print(harta[i])
print("="*100)
path = A_Star(start, goal, harta)
print(path)
