# class Animal:
#     age = 0
#
#     def getOld(self):
#         self.age += 1
#
#         return self.age
#
# class Human(Animal):
#     skill_lang = 0
#
#     def mimic(self):
#         self.skill_lang += 1
#
#         return self.skill_lang
#
# class OopTest:
#     print(Human.skill_lang)
#     print(Human.age)
#     hm = Human()
#
#     print(hm.mimic())
#     print(hm.getOld())


class Animal:
    def __init__(self):     # 생성자(__init__)
        print("Animal: 생성자")
        self.age = 0
    def getOld(self):
        self.age += 1
    def __del__(self):      # 소멸자(__del__)
        print("Animal: 소멸자")
    def __str__(self):
        return "Animal: " + str(self.age)

class Human(Animal):
    def __init__(self):
        print("Human: 생성자")
        super().__init__()
        self.skill_lang = 0
    def mimic(self):
        self.skill_lang += 1
    def __del__(self):
        print("Human: 소멸자")
        
if __name__ == '__main__':  # 메인(if __name__ == '__main__')
    # a = Animal()
    # print(a.age)
    # a.getOld()
    # print(a.age)
    
    h = Human()
    print(h)
    print(h.skill_lang)
    print(h.age)
    h.getOld()
    h.mimic()
    print(h)
    print(h.skill_lang)
    print(h.age)
    