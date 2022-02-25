import random

# lotto = range(1, 6+1)
# lottoNum = ""
#
# for i in lotto:
#     num = int(random.random() * 45) + 1
#     lottoNum += str(num) + " "
#
# print(lottoNum)

# arr = [1, 2, 3, 4, 5, 6]
# rnd = int(random.random() * 6)
#
# a = arr[rnd]
# b = arr[0]
# # arr[0] = a
# # arr[rnd] = b
#
# for i in arr:
#     arr[0] = a
#     arr[rnd] = b
#
# print(arr)

arr = list(range(1, 45+1))
# print(arr)

for i in range(1000):
    rnd = int(random.random() * 45)
    a = arr[rnd]
    b = arr[0]
    arr[0] = a
    arr[rnd] = b
# print(arr)

# for i in range(6):
#    print(arr[i], end=" ")

# print(" ")
# print(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])

arr_cut = arr[0:6]
print(arr_cut)