# 두개의 숫자를 입력받아 두 수의 합을 출력하시오.
# a = input("첫번째 숫자를 입력하세요.")
# b = input("두번째 숫자를 입력하세요.")
# sum = int(a) + int(b)
# print("두 수의 합은", sum, "입니다.")

d = int(input("첫번째 숫자를 입력하세요."))
e = int(input("두번째 숫자를 입력하세요."))
sum = d + e
# print("두 수의 합은", d + e, "입니다.")
# print("두 수의 합은 " + str(sum) + "입니다.")
# print("두 수의 합은 {}입니다.".format(sum))
print("{}, {}의 합은 {}입니다.".format(d, e, sum))
