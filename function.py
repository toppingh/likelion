def add(a, b) :
    return a + b

print(add(3, 4))

def sub(a, b) :
    return a - b

result = sub(a = 7, b = 3)
print(result)

a = 3
b = 4
c = add(a, b)
print(c)

def say() :
    return 'Hi'
a = say()
print(a)

# 예제1
def print_coin() :
    return "비트코인"

print(print_coin())

# 예제2
def print_with_smile(b) :
    print(b + ":D")
b = input()
print(print_with_smile(b))

# 예제3
def number_minus(a, b) :
    return a - b

num1 = int(input("첫번쨰 숫자 입력 : "))
num2 = int(input("두번째 숫자 입력 : "))
print(number_minus(num1, num2))

# 예제4
def order_coffee(glass, option='hot'):
    print(f'{glass}잔 / {option}')

order_coffee(3, 'iced')
order_coffee(3)
order_coffee(option='iced', glass=3)

# 예제5
def what_time(hour, minute, second):
    print(f'{hour}시 {minute}분 {second}초')

what_time(20, 11, 30)
what_time(1, 15, 25)

# 예제6
def name_age(name, age) :
    print(f'이름:{name}, 나이:{age}')

name_age("홍길동", 17)