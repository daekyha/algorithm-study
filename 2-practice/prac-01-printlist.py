# lec0914 - python 리스트 케이스별 출력

# case 1
def test01():
    print('\ntest01')
    a=[1,2,3]
    b=a
    b.append(5)
    print('a:',a)
    print('b:',b)
"""
 b=a   
    1. a와 b는 같은 리스트를 참조
"""
# case 2
def test02():
    print('\ntest02')
    a=[1,2,3]
    b=a[:]
    b.append(5)
    print('a:',a)
    print('b:',b)
"""
 슬라이싱
   1. a[0:2]  ->  0, 1번째 요소 복제 (index 2는 포함하지 않음)
   2. a[:]    ->  전체 요소 복제
"""
# case 3
def test03():
    print('\ntest03')
    a=[[1,2],[3,4]]
    b=a[:]
    b.append(5)
    print('a:',a)
    print('b:',b)
"""
  요소가 [1,2]라면 내용물은 ref가 들어있기에 슬라이싱을 통한 복제를 해도 같은 ref를 가르킴
"""

# case 4
def test04():
    print('\ntest04')
    a=[[1,2],[3,4]]
    b=a[:]
    a[1].append(5)
    print('a:',a)
    print('b:',b)   

test01()
test02()
test03()
test04()

print("=================================================================================")
# ======================================================================================= #
import copy
# 1. copy.copy => 얕은 복사. a[:]와 동일.
# 2. copy.deepcopy => 깊은 복사.

# Algorithm-01-python-p.116
# Ex 1. 리스트 복제
o = [1, [2, 3], 4]
k = o[:]
s = copy.copy(o)
d = copy.deepcopy(o)
o[1][0] = 200
o.append(10)
print("[ Ex 01 ]")
print(o)
print(k)
print(s)
print(d)

# Ex 2. 해쉬 복제
o = {'a' : 1,  'b' : [2,3]}
s = copy.copy(o)
d = copy.deepcopy(o)
o['b'].append(100)
print("[ Ex 02 ]")
print(o)
print(s)
print(d)

# Ex 3. 클래스 복제
class Myclass:
    def __init__(self, x):
        self.x = x

o = Myclass([1, 2, 3])
s = copy.copy(o)
d = copy.deepcopy(o)
o.x.append(100)
print("[ Ex 03 ]")
print(o.x)
print(s.x)
print(d.x)
