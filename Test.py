def delete(str, n):      # 'str' object has no attribute 'pop', 'remove' 해결(슬라이싱)
    front = str[:n]     # delete(idList, i) 만 하면 제거가 안되므로, 밑에 처럼 값을 복사해야 값 제거 됨
    back = str[n+1:]        # idList = delete(idList, i) -> 반복문 중에 삭제하면 인덱스 범위 오류 발생
    return front + back

def noneCount(list, num):
    for i in list[:]:
        if i == None:
            num += 1
    return num

id = input("ID를 입력해주세요\n")      # ...!@BaT#*..y.abcdefghijklm
print('변경 전 id:', id)

idList = list(id.lower())       # 레벨 1
print('변경 후 id:', id.lower())
print('1단계 id리스트', idList)      # 소문자로 변환

idCount = len(id)       # 레벨 2

for i in range(idCount):
    if idList[i].islower() == False:
        if idList[i].isalnum() == False:
            if idList[i] != '-':
                if idList[i] != '_':
                    if idList[i] != '.':
                        idList[i] = None
# idList = delete(idList, i)
# idList[i].pop() or .remove() 대신 사용

print('1.5단계 id리스트', idList)

# for i in range(idCount-noneCount(idList, 0)):
#     if idList[i] == None:
#         idList = delete(idList, i)
for i in idList[i]:
    idList.remove(None)

print('2단계 id리스트', idList) # 소문자, 숫자, 빼기, 밑줄, 마침표를 제외하고 제거

for i in range(idCount):
    if i > 0:
        if idList[i-1] == '.' and idList[i] == '.':
            idList[i] = None        # idList = delete(idList, i)

print('3단계 id리스트', idList)