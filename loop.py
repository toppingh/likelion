lion = "멋사 최고다..."
num = 1
while num <= 13:
    print(lion)
    num += 1

num = 1
while True :
    num += 1
    print(num)
    if num > 3 :
        break



# 예제1
while True :
    num1 = int(input("첫번째 정수를 입력하세요 : "))
    num2 = int(input("두번째 정수를 입력하세요 : "))
    print("두 정수의 합 : %d" % (num1 + num2))

    if num1 == 0 and num2 == 0 :
        break

list_food = ['햄버거', '치킨', '피자', '떡볶이']
for food in list_food :
    print(food)

hi = '안녕하세요'
for s in hi :
    print(s)

# 예제2
score_list = [90, 45, 70, 60, 55]
for score in score_list :
    if score >= 60 :
        print("합격입니다")
    else :
        print("불합격입니다")

# 예제3
score_list = [90, 45, 70, 60, 55]
number = 1
for score in score_list :
    if score >= 60 :
        print("%d번 학생은 합격입니다." % number)
    else :
        print("%d번 학생은 불합격입니다." % number)
    number += 1

for i in range(1, 10, 1) :
    print(i)

for i in range(1, 10, 1) :
    print(i, end=' ')

예제4
for i in range(97, 76, -1) :
    print(i, end=' ')

#예제5
for t in range(23, 41, 1) :
    print(t, end=' ')

