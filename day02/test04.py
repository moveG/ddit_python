import random

# # 스트라이크 게임
# result = ""
# count = 0
# com1 = 0
# com2 = 0
# com3 = 0
#
# while True:
#     com1 = int(random.random() * 9) + 1
#     com2 = int(random.random() * 9) + 1
#     com3 = int(random.random() * 9) + 1
#     if (com1 != com2) and (com2 != com3) and (com3 != com1):
#         break
#
# comArr = [com1, com2, com3]
# print(comArr)
#
# while True:
#     strike = 0
#     ball = 0
#     out = 0
#
#     num = input("3자리 숫자를 입력하세요.")
#     numArr = [int(num[0]), int(num[1]), int(num[2])]
#
#     if comArr[0] == numArr[0]:
#         strike += 1
#     if comArr[1] == numArr[1]:
#         strike += 1
#     if comArr[2] == numArr[2]:
#         strike += 1
#
#     if comArr[0] == numArr[1]:
#         ball += 1
#     if comArr[0] == numArr[2]:
#         ball += 1
#     if comArr[1] == numArr[0]:
#         ball += 1
#     if comArr[1] == numArr[2]:
#         ball += 1
#     if comArr[2] == numArr[0]:
#         ball += 1
#     if comArr[2] == numArr[1]:
#         ball += 1
#
#     out = 3 - strike - ball
#
#     if out == 3:
#         print("{}아웃".format(out))
#     else:
#         print("{}스트라이크, {}볼".format(strike, ball))
#
#     count += 1
#
#     if strike == 3:
#         break
#
# print("{}회 만에 정답을 맞췄습니다.".format(count))

# ------------------------------------------------------------------

# 스트라이크 게임
# result = ""
# count = 0
# com1 = 0
# com2 = 0
# com3 = 0
#
# while True:
#     com1 = int(random.random() * 9) + 1
#     com2 = int(random.random() * 9) + 1
#     com3 = int(random.random() * 9) + 1
#     if (com1 != com2) and (com2 != com3) and (com3 != com1):
#         break
#
# comArr = [com1, com2, com3]
# print(comArr)
#
# def gameStart(comArr, numArr):
#     strike = 0
#     ball = 0
#     out = 0
#
#     if comArr[0] == numArr[0]:
#         strike += 1
#     if comArr[1] == numArr[1]:
#         strike += 1
#     if comArr[2] == numArr[2]:
#         strike += 1
#
#     if comArr[0] == numArr[1]:
#         ball += 1
#     if comArr[0] == numArr[2]:
#         ball += 1
#     if comArr[1] == numArr[0]:
#         ball += 1
#     if comArr[1] == numArr[2]:
#         ball += 1
#     if comArr[2] == numArr[0]:
#         ball += 1
#     if comArr[2] == numArr[1]:
#         ball += 1
#
#     out = 3 - strike - ball
#
#     if out == 3:
#         print("{}아웃".format(out))
#     else:
#         print("{}스트라이크, {}볼".format(strike, ball))
#
#     return strike
#
# while True:
#     num = input("3자리 숫자를 입력하세요.")
#     numArr = [int(num[0]), int(num[1]), int(num[2])]
#
#     result = gameStart(comArr, numArr)
#
#     count += 1
#
#     if result == 3:
#         break
#
# print("{}회 만에 정답을 맞췄습니다.".format(count))

# ------------------------------------------------------------------

# 스트라이크 게임
def getRandom3():
    arr = list(range(1, 9 + 1))
    arr3 = []
    while len(arr3) < 3:
        rnd = int(len(arr) * random.random())
        if arr[rnd] > 0:
            arr3.append(arr[rnd])
            arr[rnd] = -1
    return arr3

def getStrike(com_arr, mine_str):
    ret = 0
    a = int(mine_str[0:1])
    b = int(mine_str[1:2])
    c = int(mine_str[2:3])

    if com_arr[0] == a:
        ret += 1
    if com_arr[1] == b:
        ret += 1
    if com_arr[2] == c:
        ret += 1

    return ret

def getBall(com_arr, mine_str):
    ret = 0
    a = int(mine_str[0:1])
    b = int(mine_str[1:2])
    c = int(mine_str[2:3])

    if com_arr[0] == b or com_arr[0] == c:
        ret += 1
    if com_arr[1] == a or com_arr[1] == c:
        ret += 1
    if com_arr[2] == a or com_arr[2] == b:
        ret += 1

    return ret

com3 = getRandom3()
print(com3)
count = 0

while True:
    mine3 = input("중복되지 않는 3자리 숫자를 입력하세요.")
    num_s = getStrike(com3, mine3)
    num_b = getBall(com3, mine3)
    print(num_s, "s", num_b, "b")
    count += 1

    if num_s == 3:
        print("{}회 만에 정답을 맞췄습니다.".format(count))
        break