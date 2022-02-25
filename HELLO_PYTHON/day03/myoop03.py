class LeeJaeyong:
    # True, False 문제는 무조건 flag를 넣어준다.(개발자들 간의 암묵적인 약속)
    def __init__(self):
        print("이재용: 생성자")
        self.flag_lipbalm = True
    def beStealed(self):
        self.flag_lipbalm = False
    def __del__(self):
        print("이재용: 소멸자")
    
class Trump:
    def __init__(self):
        print("트럼프: 생성자")
        self.cnt_hotel = 5
    def goElection(self):
        self.cnt_hotel += 10
    def __del__(self):
        print("트럼프: 소멸자")
        
class TrumpLee(LeeJaeyong, Trump):
    def __init__(self):
        print("트럼프리: 생성자")
        LeeJaeyong.__init__(self)
        Trump.__init__(self)
    def __del__(self):
        print("트럼프리: 소멸자")
        LeeJaeyong.__del__(self)
        Trump.__del__(self)

if __name__ == '__main__':
    t = TrumpLee()
    print(t.flag_lipbalm)
    print(t.cnt_hotel)
    t.beStealed()
    t.goElection()
    print(t.flag_lipbalm)
    print(t.cnt_hotel)