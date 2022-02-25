# 스크립트 언어라서 순서가 중요함(위에서부터 읽음)
def add(a, b):
    return a + b
def minus(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

sum = add(3, 4)
min = minus(3, 4)
mul = multiply(3, 4)
div = divide(3, 4)

print("sum :", sum)
print("min :", min)
print("mul :", mul)
print("div :", div)