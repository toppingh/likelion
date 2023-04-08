class Human :
    def __init__(self):
        print("응애응애")

areum = Human()

class Human() :
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("고명", 25, "여자")
print(areum.name)

class animal() :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        print(f'나는 {self.name} {self.age}살임')

cat = animal('고양이', 3)
dog = animal('강아지', 4)
cat.say()
dog.say()

class Animal:

    def __init__(self, age, height, color, xpos, ypos):
        self.age = age
        self.height = height
        self.color = color
        self.xposition = xpos
        self.yposition = ypos
        self.velocity = 0

    def sound(self):
        pass

class Horse(Animal):
    def __init__(self, age, height, color, xpos, ypos):
        Animal.__init__(self, age, height, color, xpos, ypos)

if __name__ == '__main__':
    danbi = Horse(5, 160, 'brown', 0, 0)

    danbi.color()

class 딸기 :
    def Beverage(self):
        print("딸기우유")

class 우유(딸기) :
    def taste(self):
        print("달콤하고 맛있다!!!")

def main() :
    s = 우유()
    s.Beverage()
    s.taste()

main()

class 스포츠 :
    def we(self):
        print("우리는 스포츠")

class 농구(스포츠) :
    def basket(self):
        print("농구 재밌다!!!")

class 축구(스포츠) :
    def soccer(self):
        print("축구 신난다!!")

def sports() :
    b = 농구()
    s = 축구()
    b.basket()
    s.soccer()
    s.we()

sports()