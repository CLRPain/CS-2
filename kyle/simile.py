adj = int(input())
noun = int(input())
adjlist = []
nounlist = []


for x in range(adj):
    adjlist.append(input())
    
for y in range(noun):
    nounlist.append(input())
    
for aword in adjlist:
    for nword in nounlist:
        print(f'{aword} as {nword}')