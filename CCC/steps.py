step = ''
steplist = []
while step != '99999':
    step = input()
    steplist.append(step)
    
steplist.pop(-1)
move = ''
for x in steplist:
    sum = int(x[0])+int(x[1])
    if sum%2 == 1:
        print('left', x[2:])
        move = 'left'
    elif sum%2 == 0 and sum != 0:
        print('right', x[2:])
        move = 'right'
    else:
        print(move, x[2:])
