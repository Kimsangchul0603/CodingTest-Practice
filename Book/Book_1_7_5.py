'''
n비트 소수 생성하기
n비트 = 10진수 n을 2진수로 표현했을 때 숫자가 n개
'''
import math

list = []


bit = int(input("숫자 입력 : "))
for i in range(2^(bit-1), 2^(bit)):
    for j in range(2, bit):
        if i % j == 0:
            break
        if j == i:
            list.append(i)

print(list)

# 안되는 원인을 잘 못찾겠다.
   

