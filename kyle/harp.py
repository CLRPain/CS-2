'''turns = input()+'A'
srt = 0
for x in range(1 , len(turns)):
    bef = turns[x-1].isnumeric()
    now = turns[x].isnumeric()
    #print(turns[x-1], turns[x])
    #print(bef, now)

    if bef == True and now == False:
        new = turns[srt:x]
        for y in new:
            if y == '-':
                print(turns[srt:turns.index(y)],' loosen ', turns[turns.index(y)+1:x])
                srt = x
                break
            elif y == '+':
                print(turns[srt:turns.index(y)],' tighten ', turns[turns.index(y)+1:x])
                srt = x
                break'''
            
turns = input()+'A'
srt = 0
turnlist = []
for x in range(1 , len(turns)):
    bef = turns[x-1].isnumeric()
    now = turns[x].isnumeric()
    if bef == True and now == False:
        turnlist.append(turns[srt:x])
        srt = x

for y in turnlist:
    print(y.replace('-', ''))
