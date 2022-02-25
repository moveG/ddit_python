import random

com = ""
user = input("홀/짝을 선택하시오.")
result = ""

rnd = random.random()

if rnd > 0.5 :
    com = "홀"
else:
    com = "짝"

if com == user :
    result = "승리"
else:
    result = "패배"

print("컴퓨터는 {}을 선택했고, 당신은 {}을 선택했습니다. 당신은 {}했습니다.".format(com, user, result))