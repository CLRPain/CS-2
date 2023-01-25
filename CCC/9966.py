min = int(input())
max = int(input())
list = []
num = 0
for x in range(min, max+1):
    for let in str(x):
        if int(let) in [0, 1, 8]:
            list.append(x)
            break
        elif int(let) in [6, 9]:
            list.append(x)
            break

for y in list:
    if len(str(y)) == 1 and y in [0, 1, 8]:
        num += 1
        print(y)
    elif str(y) == str(y)[::-1]: #palindrome
        if str(y) in [6, 9]:
            y2 = 
        num += 1
        print(y)
print(num)
