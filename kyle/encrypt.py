key = input()
mess = input()
new = ''
for x in mess:
    if x.isalpha():
        new+= x
    
mess = ''    
for let in range(len(new)):
    char = ord(new[let])
    num = ord(key[let%3])-65
    a = char+num
    if char + num > 90:
        a = 64 + (char+num-90)
    mess += chr(a)
    
print(mess)