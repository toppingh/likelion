if True :
    print("실행문장 실행")
print("if문 밖에 있는 실행문장")

if False :
    print("실행문장 실행")
print("if문 밖에 있는 실행문장")

# 예제
money = int(input("돈을 입력하세요 : "))
if money >= 10000 :
    print("택시를 탄다")
else :
    print("버스를 탄다")

# 예제2
num1 = int(input("첫번째 정수를 입력하세요 : "))
num2 = int(input("두번째 정수를 입력하세요 : "))

if num1 > num2 :
    print("첫번째 정수가 두번째 정수보다 큰 수 입니다.")
elif num1 == num2 :
    print("두 수가 같습니다.")
else :
    print("첫번쨰 정수가 두번쨰 정수보다 작은 수입니다.")

# 예제3
score = int(input("점수를 입력하세요 : "))
if score >= 90 and score <= 100 :
    print("A학점입니다.")
# elif score >= 80 :
    print("B학점입니다.")
elif score >= 70 :
    print("C학점입니다.")
elif score >= 60 :
    print("D학점입니다.")
else :
    print("F학점입니다.")

# 예제4
score = int(input("점수를 입력하세요 : "))
print('합격' if score >= 60 else '불합격')