num = int(input())
prepay = 0
prename = ''
for x in range(num):
    name = input()
    pay = int(input())
    if pay > prepay:
        prepay = pay
        prename = name
        
print(prepay)
print(prename)