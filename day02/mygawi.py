import random

# 가위바위보 게임을 작성하시오.
com = ""
user = input("가위/바위/보를 입력하시오.")
result = ""

# rnd = int(random.random() * 3) + 1
#
# if rnd == 1:
#     com = "가위"
# elif rnd == 2:
#     com = "바위"
# elif rnd == 3:
#     com = "보"

# if com == user:
#     result = "비김"
# elif (com == "가위" and user == "바위") or (com == "바위" and user == "보") or (com == "보" and user == "가위"):
#     result = "승리"
# else:
#     result = "패배"

rnd = random.random()

if rnd > 0.66:
    com = "가위"
elif rnd > 0.33:
    com = "바위"
else:
    com = "보"

if com == "가위" and user == "가위":
    result = "비김"
if com == "가위" and user == "바위":
    result = "승리"
if com == "가위" and user == "보":
    result = "패배"

if com == "바위" and user == "바위":
    result = "비김"
if com == "바위" and user == "보":
    result = "승리"
if com == "바위" and user == "가위":
    result = "패배"

if com == "보" and user == "보":
    result = "비김"
if com == "보" and user == "가위":
    result = "승리"
if com == "보" and user == "바위":
    result = "패배"

print("일반 가위바위보 게임 결과 : 컴퓨터는 {}, 유저는 {}, 결과는 {}".format(com, user, result))

# 가위바위보 게임을 작성하시오.
# if com == user:
#     result = "비김"
# elif (com == "가위" and user == "바위") or (com == "바위" and user == "보") or (com == "보" and user == "가위"):
#     result = "패배"
# else:
#     result = "승리"

if com == "가위" and user == "가위":
    result = "비김"
if com == "가위" and user == "바위":
    result = "패배"
if com == "가위" and user == "보":
    result = "승리"

if com == "바위" and user == "바위":
    result = "비김"
if com == "바위" and user == "보":
    result = "패배"
if com == "바위" and user == "가위":
    result = "승리"

if com == "보" and user == "보":
    result = "비김"
if com == "보" and user == "가위":
    result = "패배"
if com == "보" and user == "바위":
    result = "승리"

print("바보 가위바위보 게임 결과 : 컴퓨터는 {}, 유저는 {}, 결과는 {}".format(com, user, result))