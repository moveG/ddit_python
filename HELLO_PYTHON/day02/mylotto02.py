import random

arr = list(range(1, 45+1))
lotto = list()

# while len(lotto) < 6:
while True:
    rnd = int(random.random() * len(arr))
    if arr[rnd] > 0:
        lotto.append(arr[rnd])
        arr[rnd] = -1

    if len(lotto) >= 6:
        break
    # else:
    #     continue
    #     pass

print(lotto)