# 출력할 단수를 입력하시오.(2~9)

num = int(input("출력할 단수를 입력하시오.(2~9)"))


for i in range(1, 9+1):
    print("{} * {} = {}".format(num, i, num * i))

# for문을 쓰는 것보다 알아보기 쉽게 쓰는 것이 중요함
print("{} * {} = {}".format(num, 1, num * 1))
print("{} * {} = {}".format(num, 2, num * 2))
print("{} * {} = {}".format(num, 3, num * 3))
print("{} * {} = {}".format(num, 4, num * 4))
print("{} * {} = {}".format(num, 5, num * 5))
print("{} * {} = {}".format(num, 6, num * 6))
print("{} * {} = {}".format(num, 7, num * 7))
print("{} * {} = {}".format(num, 8, num * 8))
print("{} * {} = {}".format(num, 9, num * 9))