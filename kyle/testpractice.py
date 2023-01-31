import random


l = []
for x in range(10):
    temp = []
    for y in range(10):
        temp.append(0)
        
    l.append(temp)
    
sam1 = random.sample(range(10), 10)
sam2 = random.sample(range(10), 10)
for bomb in range(10):
    for r in range(-1, 2):
        for c in range(-1, 2):
            if 0<=(sam1[bomb]+r)<10 and 0<=(sam2[bomb]+c)<10:
                print(sam1[bomb]+r, sam2[bomb]+c)
                #l[(sam1[bomb]+r)][(sam2[bomb]+c)] += 1
    l[sam1[bomb]][sam2[bomb]]="B"

for a in range(10):
    for b in range(10):
        print(l[a][b],'',  end = '')    
    print()


    
