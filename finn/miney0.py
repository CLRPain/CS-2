#2d miney no way
import random

l = []
for x in range(10):
    temp = []
    for y in range(10):
        temp.append(0)
    l.append(temp)
    

x = random.sample(range(10), 5)
y = random.sample(range(10), 5)    
for z in range(5):
    l[x[z]][y[z]] = "B"
for list in l:
    for x in list:
        if x == "B":
            ycoord = l.index(list)
            xcoord = list.index(x)
            
            for row in range(-1,2):
                for col in range(-1,2):
                    if 0 <= (xcoord + row) < 10 and 0 <= (ycoord + col) < 10:
                        if l[ycoord + col][xcoord + row] != "B":
                            l[ycoord + col][xcoord + row] += 1

for list in l:
    for x in list:
        print(x, "", end = "")
    print()        