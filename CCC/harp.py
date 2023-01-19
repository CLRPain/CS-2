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
    if '-' in y:
        print(y.replace('-', ' loosen '))
    elif '+' in y:
        print(y.replace('+', ' tighten '))
