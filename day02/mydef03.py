def addmin(a, b):
    return a + b, a - b

sum, min = addmin(3, 4)
print("sum :", sum, ", min :", min)
# 리턴이 여러개면 변수에 순서대로 삽입됨

tot = addmin(3, 4)
print(tot)
# 배열과 비슷함
print(tot[0], tot[1])

def addminmuldiv(a, b):
    return a + b, a - b, a * b, a / b

sum, min, mul, div = addminmuldiv(3, 4)
print(sum, min, mul, div)