# 작은 수를 입력하시오.
# 큰 수를 입력하시오.
# 작은 수에서 큰 수까지의 합은 00입니다.
# 작은 수에서부터 큰 수까지의 합을 구하시오.

a = int(input("작은 수를 입력하시오."))
b = int(input("큰 수를 입력하시오."))

arr = range(a, b+1)
sum = 0
for i in arr:
    sum += i
# print(a, "에서", b, "까지의 합은", sum, "입니다.")
# print(str(a) + "에서 " + str(b) + "까지의 합은 " + str(sum) + "입니다.")
print("{}에서 {}까지의 합은 {}입니다.".format(a, b, sum))
# .format()은 문자와 숫자를 가리지 않고 넣어줌