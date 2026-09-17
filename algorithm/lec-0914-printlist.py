
# case 1
def test01(self):
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
def test02(self):
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
def test03(self):
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
def test04(self):
    print('\ntest04')
    a=[[1,2],[3,4]]
    b=a[:]
    a[0].append(5)
    print('a:',a)
    print('b:',b)   

test01()
test02()
test03()
test04()


