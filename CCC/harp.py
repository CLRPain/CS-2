turns = input()+'A'
srt = 0
for x in range(1 , len(turns)):
    bef = turns[x-1].isnumeric()
    now = turns[x].isnumeric()
    #print(turns[x-1], turns[x])
    #print(bef, now)

    if bef == True and now == False:
        new = turns[srt:x]
        print(srt, x)
        for y in new:
            print(y, 'a')
            if y == '-':
                print(new[srt:new.index(y)],' loosen ', new[new.index(y)+1:x])
                srt = x
                break
            elif y == '+':
                print(new[srt:new.index(y)],' tighten ', new[new.index(y)+1:x])
                srt = x
                break
            
            