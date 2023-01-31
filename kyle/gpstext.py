def find(inp):
    for lists in key:
        if inp in lists:
            return lists.index(inp), key.index(lists)
    
text = input()
origin = (0,0)
move = 0
key = [['A', 'B', 'C', 'D', 'E', 'F'],
       ['G', 'H', 'I', 'J', 'K', 'L'],
       ['M', 'N', 'O', 'P', 'Q', 'R'],
       ['S', 'T', 'U', 'V', 'W', 'X'],
       ['Y', 'Z', ' ', '-', '.', 'enter']]

letlist = []
for let in text:
    loc = find(let)
    xmove = origin[0]-loc[0]
    ymove = origin[1]-loc[1]
    if xmove < 0:
        xmove *= -1
    if ymove <0:
        ymove *= -1
    move += ymove + xmove
    origin = loc
origin = (5,4)
xmove = origin[0]-loc[0]
ymove = origin[1]-loc[1]
if xmove < 0:
    xmove *= -1
if ymove <0:
    ymove *= -1
    
move += ymove + xmove
print(move)
    