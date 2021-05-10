numCount = int(input())
sum = 0

for i in range(numCount):
    charList = list(input())
    charLen = len(charList)
    numList = [0 for x in range(charLen)]
    for j in range(charLen):
        if charList[j] == 'O':
            numList[j] += 1
            if j > 0:
                if charList[j - 1] == 'O':
                    numList[j] = numList[j-1] + 1
        # print(charList)
        # print(numList)
        sum = sum + numList[j]
        j += 1
    print(sum)
    sum = 0
    numCount += 1