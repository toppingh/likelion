list1 = [1, 2, 3]
list2 = [4, 5, 6, 7]
print(list1 + list2)

l = [1, 2, 3, 4, 5]
print(type(l))

list3 = [2, 5, 7, 9, 10]
print(list3[0])
print(list3[3])
print(list3[2] + list3[-1])

list4 = [0, 1, 2, 3, 4]
print(list4[1:3])
print(list4[:2])
print(list4[3:])
print(list4[3:4])

list5 = ['hello', 'my', 'name', 'is', 'hwang']
print(list5)

list4.append(5) # 값 추가
print(list4)

list4.insert(1, 6) # 인덱스에 값 추가
print(list4)

list4.sort() # 오름차순 정렬
print(list4)

list4.reverse() # 역순으로 표시
print(list4)

del list4[6] # 인덱스에 있는 값 삭제
print(list4)

list5.remove('hello') # 해당 값 삭제
print(list5)

print(list5.index('is')) # 찾고자 하는 값의 인덱스

print(list5.pop()) # 마지막 값 삭제

list12 = ['a', 'b', 'c', 'd']
list12.pop()
print(list12)

list13 = [0, 1, 2]
print(len(list13))