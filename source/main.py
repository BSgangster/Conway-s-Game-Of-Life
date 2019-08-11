import os,time,random

class World:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        self.world_array = []

    def fill_board(self):
        counter_x = 0
        counter_y = 0
        while counter_y < self.width:
            counter_x = 0
            temp_array = []
            while counter_x < self.length:
                temp_array.append(random.randrange(0,2))
                counter_x += 1
            self.world_array.append(temp_array)
            counter_y += 1

    def print_world(self):
        for i in self.world_array:
            for z in i:
                print(z,end='')
            print('\n',end='')

    def count_neighbours(self,x,y):
        sum = 0
        print((x,y))
        #top left corner
        if x == 0 and y == 0:
            sum += self.world_array[x+1][y]
            sum += self.world_array[x+1][y+1]
            sum += self.world_array[x][y+1]
        #bottom right corner
        elif x == self.length-1 and y == self.width-1:
            sum += self.world_array[x - 1][y]
            sum += self.world_array[x - 1][y - 1]
            sum += self.world_array[x][y - 1]
        #bottom left corner
        elif x == 0 and y == self.width - 1:
            sum += self.world_array[x + 1][y]
            sum += self.world_array[x + 1][y - 1]
            sum += self.world_array[x][y - 1]
        #top right corner
        elif x == self.length-1 and y == 0:
            sum += self.world_array[x - 1][y]
            sum += self.world_array[x - 1][y + 1]
            sum += self.world_array[x][y + 1]
        #top border
        elif y == 0 and x != 0 and x != self.length - 1:
            sum += self.world_array[x][y + 1]
            sum += self.world_array[x + 1][y + 1]
            sum += self.world_array[x - 1][y + 1]
            sum += self.world_array[x - 1][y]
            sum += self.world_array[x + 1][y]
        #bottom border
        elif y == self.width - 1 and x != 0 and x != self.length - 1:
            sum += self.world_array[x][y - 1]
            sum += self.world_array[x + 1][y - 1]
            sum += self.world_array[x - 1][y - 1]
            sum += self.world_array[x + 1][y]
            sum += self.world_array[x - 1][y]
        #left border
        elif x == 0 and y != 0 and y != self.width - 1:
            sum += self.world_array[x + 1][y]
            sum += self.world_array[x + 1][y + 1]
            sum += self.world_array[x + 1][y - 1]
            sum += self.world_array[x][y + 1]
            sum += self.world_array[x][y - 1]
        #right border
        elif x == self.length and y != 0 and y != self.width - 1:
            sum += self.world_array[x - 1][y]
            sum += self.world_array[x - 1][y + 1]
            sum += self.world_array[x - 1][y - 1]
            sum += self.world_array[x][y + 1]
            sum += self.world_array[x][y - 1]
        #case where it is not on any of the edges
        else:
            sum += self.world_array[x - 1][y]
            sum += self.world_array[x + 1][y]
            sum += self.world_array[x + 1][y + 1]
            sum += self.world_array[x - 1][y + 1]
            sum += self.world_array[x - 1][y - 1]
            sum += self.world_array[x + 1][y - 1]
            sum += self.world_array[x][y + 1]
            sum += self.world_array[x][y - 1]
        return sum

hello = World(20,20)
hello.fill_board()
hello.print_world()
y = 0
x = 0
while y < 20:
    x = 0
    while x < 20:
        print(hello.count_neighbours(x,y))
        x += 1
    y += 1