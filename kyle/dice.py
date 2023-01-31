round = int(input())
rolls = []
p0 = 100
p1 = 100
for x in range(round):
    rolls.append(input().split(' '))
    
for roll in rolls:
    r0 = int(roll[0])
    r1 = int(roll[1])
    if r0 < r1:
        p0 -= r1
    elif r0 > r1:
        p1 -= r0
print(p0)
print(p1)