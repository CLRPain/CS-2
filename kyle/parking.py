num = int(input())
yes = input()
tmr = input()
both = 0
for x in range(num):
    if yes[x] == 'C' and tmr[x] == 'C':
        both += 1
print(both)