from copy import copy
q = [1,2,3]
qq = copy(q)
print(id(q),"\t", id(qq))
a = ["주하","잠수", "재성"]
a[0] = "하"
a.append("abbb")
b =a[0].find("하")

a.extend([2,3])
print(a)
c = "%d alllldkdjkdfjld %2.2f" %(12,12.5)
print(c)

dic = {1 : 12, 2 : 13}
dic.get(3) # == NULL get 함수는 없을 때 에러가 아니라 NULL이 리턴

s1 = set([1,2,3,4,5])
s2 = set([2,3,4,5,6])
s3 = s1|s2 #합집합  s1.union(s2)
s4 = s1 & s2#교집합 s1.intersection(s2)
s1.update([7,8,9]) #여러개의 값을 추가해야할 때
s1.add(12) #한개의 값을 추가할 때
s1.remove(1) #지우기

message = "success" if 1 in a else "failure"
#-> 조건부 표현식 (내용) (조건) (예외)

#result = [num * 3 for num in a if a%2 == 0]

def sum_many(*args):
    sum  = 0
    for i in args:
        sum += i
    return sum;

def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은 :" + k)


def aa(aa = 3):
    return aa+1, aa-1, aa*2
    #이렇게 하면 튜플형인 하나의 값이 리턴, 초기값 설정 가능 

print(aa(4))

add = lambda t,y: t+y
#함수의 축약형으로 사용이 가능하다
print(add(5,6))

print(12121,end = ' ')
f = open("새파일.txt", "w", encoding="UTF-8")
for i in range(1,11):
    data = "%d줄입니다.\n" %i #->이거를 이용해서 웹 크롤링도 가능하다
    f.write(data)
f.close()