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
        #top left corner
        if x == 0 and y == 0:
            sum += self.world_array[y + 1][x]
            sum += self.world_array[y + 1][x + 1]
            sum += self.world_array[y][x + 1]
        #bottom right corner
        elif x == self.length-1 and y == self.width-1:
            sum += self.world_array[y - 1][x]
            sum += self.world_array[y - 1][x - 1]
            sum += self.world_array[y][x - 1]
        #bottom left corner
        elif x == 0 and y == self.width - 1:
            sum += self.world_array[y][x + 1]
            sum += self.world_array[y - 1][x + 1]
            sum += self.world_array[y - 1][x]
        #top right corner
        elif x == self.length-1 and y == 0:
            sum += self.world_array[y][x - 1]
            sum += self.world_array[y + 1][x - 1]
            sum += self.world_array[y + 1][x]
        #top border
        elif y == 0 and x != 0 and x != self.length - 1:
            sum += self.world_array[y + 1][x]#bottom check
            sum += self.world_array[y + 1][x + 1]#diagonal check
            sum += self.world_array[y + 1][x - 1]
            sum += self.world_array[y][x - 1]#side check
            sum += self.world_array[y][x + 1]
        #bottom border
        elif y == self.width - 1 and x != 0 and x != self.length - 1:
            sum += self.world_array[y - 1][x]#top check
            sum += self.world_array[y - 1][x + 1]#diagonal check
            sum += self.world_array[y - 1][x - 1]
            sum += self.world_array[y][x + 1]#side check
            sum += self.world_array[y][x - 1]
        #left border
        elif x == 0 and y != 0 and y != self.width - 1:
            sum += self.world_array[y][x + 1]
            sum += self.world_array[y + 1][x + 1]
            sum += self.world_array[y - 1][x + 1]
            sum += self.world_array[y + 1][x]
            sum += self.world_array[y - 1][x]
        #right border
        elif x == self.length-1 and y != 0 and y != self.width - 1:
            sum += self.world_array[y][x -1]
            sum += self.world_array[y + 1][x - 1]
            sum += self.world_array[y - 1][x - 1]
            sum += self.world_array[y + 1][x]
            sum += self.world_array[y - 1][x]
        #case where it is not on any of the edges
        else:
            sum += self.world_array[y][x - 1]#leftright check
            sum += self.world_array[y][x + 1]
            sum += self.world_array[y + 1][x + 1]#top diagonal check
            sum += self.world_array[y + 1][x - 1]
            sum += self.world_array[y - 1][x + 1]#bottom diagonal check
            sum += self.world_array[y - 1][x - 1]
            sum += self.world_array[y + 1][x]#topbottom check
            sum += self.world_array[y - 1][x]
        return sum
    def get_next_gen(self):
        y = 0
        x = 0
        new_array = []
        while y < 100:
            x = 0
            temp_array = []
            while x < 100:
                if self.count_neighbours(x,y) > 3:
                    temp_array.append(0)
                elif self.count_neighbours(x,y) < 2:
                    temp_array.append(0)
                elif self.world_array[y][x] == 0 and self.count_neighbours(x,y) == 3:
                    temp_array.append(1)
                else:
                    temp_array.append(self.world_array[y][x])
                x += 1
            new_array.append(temp_array)
            y += 1
        self.world_array = new_array

hello = World(100,100)
hello.fill_board()
hello.print_world()
time.sleep(0.5)
os.system('clear')
while True:
    hello.get_next_gen()
    hello.print_world()
    time.sleep(0.5)
    os.system('clear')
