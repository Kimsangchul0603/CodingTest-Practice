'''
피보나치 수열 만들기
'''

# 내 풀이

list = []

a = 1
b = 1
c = 0
list.extend([a, b])
for i in range(10):
    c = a + b
    a = b
    b = c
    list.append(c)
print(list)
