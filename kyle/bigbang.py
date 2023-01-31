k = int(input())
mess = input()

num = 0
newmess = ''
for x in mess:
    num += 1
    s = (3*num)+k
    x = (ord(x)-s)
    if x <= 64:
        xnum = 65-x
        x = 91-xnum
    newmess += chr(x)

print(newmess)