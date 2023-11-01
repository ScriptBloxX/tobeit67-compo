import json
playerList = []
deadList = []
playerDict = {}

while True:
    n=input()
    if n.lower()=='start':
        break
    playerList.append(n)

while True:
    n=input()
    if n.lower()=='end':
        break
    deadList.append(n)
# convert
for i in playerList:
    playerDict[list(json.loads(i).keys())[0]] = list(json.loads(i).values())[0]
# sort
playerDictSort = sorted(playerDict,key=lambda k:(k.lower(),k))
deadList = sorted(deadList,key=lambda k:k.lower())
# output
duckcount=0
for i in playerDict:
    if i not in deadList and playerDict[i] == 'Duck':
        duckcount+=1
print(duckcount,'Ducks Remains')
print('***Alive***')
for i in playerDictSort:
    if i not in deadList:
        print(i,':',playerDict[i])
print('***Dead***')
for i in deadList:
    print(i,':',playerDict[i])

# print('debug')
# print(sorted(playerDict,key=lambda k:(k.lower(),k)))
# print(playerDict)