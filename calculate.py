str1 = '안녕'
str2 = '하세요'
str3 = 1
str4 = 9
print(str1 + str2)
print(str3 + str4)

int1 = 10
int2 = 2
print(int1 - int2)
print(int1 * int2)
print(int1 / int2) # 나누기
print(int1 // int2) # 나눈 후 몫
print(int1 % int2) # 나눈 후 나머지

# 예제
num1 = int(input("정수를 입력하세요 >> "))
num2 = int(input("정수를 입력하세요 >> "))

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print("더하기 결과 : ", sum)
print("빼기 결과 : %d" % sub)
print("곱하기 결과 : %d" % mul)
print("나누기 결과 : %d" % div)

print("%d" % 1234.56)
print("%f" % 1234.56)
print("%s" % "python")

print("%4d" % 1234)
print("%08.2f" % 1234.56) # .을 포함해 8자리, 빈자리는 0으로
print("%5s" % "abc") # 5자리, 빈자리는 공백

first_one = float(input("1학년 1학기 성적을 입력하세요 : "))
first_two = float(input("1학년 2학기 성적을 입력하세요 : "))
second_one = float(input("2학년 1학기 성적을 입력하세요 : "))
second_two = float(input("2학년 2학기 성적을 입력하세요 : "))
placement = float(input("현장실습 성적을 입력하세요 : "))

grade = first_one + first_two + second_one + second_two + placement
avg = grade / 5

print("황다은 학생의 지금까지의 학점은 : %.2f 입니다." % avg)

# 예제2
kor = int(input("국어 점수를 입력하세요 >> "))
math = int(input("수학 점수를 입력하세요 >> "))
eng = int(input("영어 점수를 입력하세요 >> "))

sum = kor + math + eng
avg = sum / 3

print("합계 : %d" % sum)
print("평균 : %d" % avg)

n1 = int(input("정수 입력 : "))
n2 = int(input("지수 입력 : "))
n3 = n1 ** n2
print("값은 %d입니다." % n3)

a = 3
b = 10
print(a > b)
print(a <= b)
print(a == b)
print(a != b)

c = 5
print(not a < b)
print(a < b and c < b)
print(a < b and c > b)
print(a < b or c > b)

