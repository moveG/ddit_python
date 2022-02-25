# arr = range(1, 11)
arr = range(1, 10+1)
# 범위가 1~10까지라는 것을 표시하기 위해 11이 아닌 10+1을 사용함

# 1~10까지의 합계 구하기
sum = 0
for i in arr:
    sum += i
    # sum += arr[i-1]
# i는 배열의 인덱스가 아니라 arr안의 아이템(item)이라는 뜻

print("sum :", sum)

