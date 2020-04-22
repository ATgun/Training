class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name, say):
        print('{}아' '{}'.format(to_name, say))

    def introduce(self):
        print("안녕! 내 이름은 " + self.name + "! " + str(self.age) + " 살이지")

class Police(Person):
    def arrest(self, to_arrest):
        print("넌 체포됐다, " + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("다음엔 뭘 만들지? 아 이걸 만들어야겠다: " + to_program)

wonie = Person("워니", 20)
TG = Police("블넬", 33)
KJ = Programmer("꿀벙", 33)

wonie.introduce()
TG.introduce()
TG.arrest("꿀벙")
KJ.introduce()
KJ.program("섹무새")