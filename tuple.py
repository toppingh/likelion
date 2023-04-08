# tuple1 = (0, 1, 2, 3, ('a', 'b', 'c'), 5)
# print(tuple1[2])
# print(tuple1[4])
# print(tuple1[:5])
# print(tuple1[3:])
# print(len(tuple1))
#
# # in, not in
# str1 = '파이썬 최고'
# print('파이썬' in str1)
# print('파이썬' not in str1)
#
# list1 = [77, 38, 10]
# print(33 in list1)
# print(33 not in list1)
#

for i in range(1, 6) :
    for j in range(1, i + 1) :
        print(j, end='')
    for k in range(i + 1, 6) :
        print("*", end='')
    print()


class sports:
    def like_sports(self):
        print("좋아하는 스포츠는?")

class volley(sports):
    def volleyball(self):
        print("배구")

class soccer(sports):
    def soccerball(self):
        print("축구")

def main():
    v = volley()
    v.like_sports()
    v.volleyball()

main()
