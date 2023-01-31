min = int(input())
max = int(input())
list = []
num = 0
for x in range(min, max+1):
    x = str(x)
    for let in x:
        if int(let) in [0, 1, 8]:
            list.append(x)
            break
        elif int(let) in [6, 9]:
            list.append(x)
            break

for y in list:
    if len(y) == 1 and y in ['0', '1', '8']:
        num += 1
        print(y)
    elif y == y[::-1]: #palindrome
        if '6' in y or '9' in y:
            for let in y:
                if let == '6':
                    y2 = y[:y.index(let)] +'9'+y[y.index(let)+1:]
                elif let == '9':
                    y2 = y[:y.index(let)] +'6'+y[y.index(let)+1:]
            print(y, y2, 'bef')
            if y == y2:
                num += 1
                print(y, y2, 'num')
        else:
            num += 1
            print(y)
print(num)
