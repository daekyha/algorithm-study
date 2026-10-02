#===============================================================================#
# 1. 조건문
# - if/elif/else 순.
# - 조건 끝마다 : 붙히기.

num = 34
if num <= 10:
    print("case 1")
elif num <= 20:
    print("case 2")
else:
    print("case 3") 
    
#===============================================================================#
# 2. 반복문
# Ex 2.1. while
print("Ex 2.1.")
i = 0
while i < 5:
    print(i)
    i += 1
    if i==3:
        break

# Ex 2.2. for <var> in <seq>:
print("Ex 2.2.")
for var in [1,3,5]:
    print(var)

# Ex 2.3. for <var> in range([start], end, [step])
print("Ex 2.3.")
for var in range(0,10,5):
    print(var)
        