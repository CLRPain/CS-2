num = int(input())
shift = int(input())
total = num
for x in range(shift):
    add = num*(10**(x+1))
    total += add
print(total)