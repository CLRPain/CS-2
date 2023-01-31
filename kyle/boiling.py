temp = int(input())
pres = (5*temp)-400
print(pres)
if pres > 100:
    print(-1)
elif pres < 100:
    print(1)
else:
    print(0)