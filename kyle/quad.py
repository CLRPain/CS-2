xpoint = int(input())
ypoint = int(input())
xneg = False
yneg = False

if xpoint < 0:
    xneg = True
if ypoint < 0:
    yneg = True


if xneg == False and yneg == False:
    print(1)
elif xneg == True and yneg == False:
    print(2)
elif xneg == True and yneg == True:
    print(2)
elif xneg == False and yneg == True:
    print(4)