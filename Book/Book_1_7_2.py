'''
두 정수의 최대 공약수 구하기
'''
result = 0

x = input("숫자를 입력하시오 : ")
y = input("숫자를 입력하시오 : ")

def sol(self):
    for i in range(min(x, y), 0, -1):
        if y % i == 0 and x % i == 0:
            result = i

    return result

def test():
    return print("최대공약수는 : ", str(result))

if __name__ == '__main__':
    test()
    
# 함수형으로 바꾸는 과정이 어렵군
# 사실 input을 넣을 필요가 없는 것 같다. def에 나와 있으니까

# 정답
def finding_gcd(a, b):
    while(b != 0):
        result = b
        a, b = b, a % b
    return result

def test_finding_gcd():
    number1 = 21
    number2 = 12
    assert(finding_gcd(number1, number2) == 3)
    print("테스트 통과")

if __name__ == '__main__':
    test_finding_gcd()
    