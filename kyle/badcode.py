plain = input()
map = input()
mess = input()
key = {}

for x in range(len(plain)):
    key[map[x]] = plain[x]
    
newmess = ''
for let in mess:
    newmess += key.get(let, '.')
print(newmess)