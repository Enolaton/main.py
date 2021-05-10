number = int(input())
numCount = 0
# sum = 0

def numWeight(x): # 리스트에 O가 있으면 1을 저장
    if numList[x] == 'o':
        numList[x] += 1

def numChange():
    if numList[i] == 'o':
        numList[i] = 1
    elif numList[i] == 'x':
        numList[i] = 0
    else:
        print('error')

while( numCount < number ):
    numList = list(input())
    numVolume = len(numList)
    for i in range(0, numVolume-1):
        numChange()
        print(numList)
        for j in range(1, numVolume-1):
            x = j-1
            numWeight(x)
            print(numList)
    numCount += 1
