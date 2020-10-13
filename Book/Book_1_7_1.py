'''
진법 변환

진법을 변환하는 함수를 직접 만들어보자. 
다음 코드는 다른 진법의 숫자를 10진수로 변환한다.(2<=base<=10)
'''

# 내가 푼 코딩

number = str(input("숫자를 입력하세요 : "))
base = int(input("몇 진수 인가요?? : "))

for i in range(len(number)-1):
    if int(number[i]) >= base :
        print("숫자를 잘못 입력했습니다.")
    else:
        continue

decimal = int(number, base)
    
print(str(base) + "진수인 " + number + "를 10진수로 변환하면 " + str(decimal) + "입니다.")    


 # 숫자와 진수를 비교하는 for문이 정상적으로 작동하지 않음.

 # 정답

def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number = number // 10 # number를 10으로 나눈 후 소수점 무시
    return result

def test_convert_to_decimal():
    number, base = 1001, 2
    assert(convert_to_decimal(number, base) == 9) # assert는 사상검증 기능, 조건식 맞으면 ㅇㅋ
    print("테스트 통과")

if __name__ == '__main__':
    test_convert_to_decimal()
    



