dic1 = {'name' : 'DE', 'age' : 23, 'phone' : '010-6263-8901'}
print(dic1)
print(type(dic1))

dic1["birth"] = "11/22"
print(dic1)

# 딕셔너리 예제
dic_test = {'노래제목' : '아무노래'}
print(dic_test)

dic_test["가수"] = "지코"
dic_test["날짜"] = "2020.01.13"
print(dic_test)

del dic1["name"]
print(dic1)

print(dic1["age"])

# print(dic1["성별"]) # 키값 에러
temp = dic1.get("성별")
print(temp)

print(dic1.keys()) # 키 값 가져오기
print(dic1.values()) # value 값 가져오기

print("성별" in dic1)
print("age" in dic1)

dic2 = {'name' : 'DE'}
dic2.clear()
print(dic2)