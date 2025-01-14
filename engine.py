import random

class Fov:
    def __init__(self, cell_number, type):
        self.row = random.randrange(0, cell_number)
        self.col = random.randrange(0, cell_number)
        self.index = self.get_index(cell_number)
        self.visible = True

class Creature:

    def __init__(self, cell_number, row, col, type):
        self.row = row
        self.col = col
        self.index = self.get_index(cell_number)
        self.type = type
        self.directions = ['L', 'D', 'R', 'U', 'S']
        self.zombie_dir = random.choices(self.directions, weights=(0.25, 0.25, 0.25, 0.25, 0.0), k=1)

    def get_index(self, cell_number):
        return self.row * cell_number + self.col
    
    def get_direction_human(self):
        choice = random.choices(self.directions, weights=(0.0, 0.0, 0.0, 0.0, 1.0), k=1)
        return choice
    
    def get_direction_zombie(self):
        choice = self.zombie_dir
        return choice
    
    def move(self, cell_number, type, occupiedFields = {}):
        direction = ''
        if type == 'Zombie':
            direction = self.get_direction_zombie()
        elif type == 'Human':
            direction = self.get_direction_human()
        else:
            return 0
        
        # compute new position
        #print(direction)
        if 'L' in direction and self.type=='Zombie':
            if self.col == 0:
                self.col = self.col + 1     # creature can not exit grid but bounces off the wall
                self.zombie_dir = ['R']
            else:
                self.col = self.col - 1     
        elif 'D' in direction and self.type=='Zombie':
            if self.row == cell_number-1:
                self.row = self.row - 1     # creature can not exit grid but bounces off the wall
                self.zombie_dir = ['U']
            else:
                self.row = self.row + 1
        elif 'R' in direction and self.type=='Zombie':
            if self.col == cell_number-1:
                self.col = self.col -1      # creature can not exit grid but bounces off the wall
                self.zombie_dir = ['L']
            else:
                self.col = self.col + 1
        elif 'U' in direction and self.type=='Zombie':
            if self.row == 0:
                self.row = self.row + 1     # creature can not exit grid but bounces off the wall
                self.zombie_dir = ['D']
            else:
                self.row = self.row - 1
        elif direction == 'S':
            pass
        else:
            pass
        self.index = self.get_index(cell_number)

        # check collision with zombie
        if self.index in occupiedFields:
            self.type = 'Zombie'


# maxNumZombies = 2
# cell_number = 10
# numZombies = random.randrange(0, maxNumZombies)
# for i in range(numZombies):
#     zombie = Creature(cell_number, 'Zombie')
#     print(zombie.row)
#     print(zombie.col)
#     print(zombie.index)

#     print("After move:")
#     zombie.move(cell_number, 'Zombie')
#     print(zombie.row)
#     print(zombie.col)
#     print(zombie.index)