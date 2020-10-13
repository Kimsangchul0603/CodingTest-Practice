'''
random 모듈
난수를 생성하는 random 모듈 생성
'''

import random

def testin_random():
    values = [1, 2, 3, 4]

    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))
    print(random.sample(values, 3))
    print(random.sample(values, 2))
    random.shuffle(values)
    print(values)

    print(random.randint(0, 10))

if __name__ == '__main__':
    testin_random()
     
# random에는 choice(하나 선택), sample(원하는 갯수 선택), shuffle(섞기), randint(범위 낸 랜덤변수) 등이 있다.