import random

# rnd = random.random()
# print(rnd)

# arr = range(1, 100+1)
# for i in arr:
#     rnd = random.random()
#     print("{}번째 랜덤값 {}".format(i, rnd))

for i in range(100):
    rnd = int(random.random() * 100) + 1
    print("{}번째 랜덤값 {}".format(i+1, rnd))