
# case 1
def test01():
    print('\ntest01')
    a=[1,2,3]
    b=a
    b.append(5)
    print('a:',a)
    print('b:',b)

# case 2
def test02():
    print('\ntest02')
    a=[[1,2],[3,4]]
    b=a[:]
    b.append(5)
    print('a:',a)
    print('b:',b)

# case 3
def test03():
    print('\ntest03')
    a=[1,2,3]
    b=a[:]
    b.append(5)
    print('a:',a)
    print('b:',b)

# case 4
def test04():
    print('\ntest04')
    a=[[1,2],[3,4]]
    b=a[:]
    b[0].append(5)
    print('a:',a)
    print('b:',b)   

test01()
test02()
test03()
test04()


