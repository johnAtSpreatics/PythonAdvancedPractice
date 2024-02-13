# 파이썬 심화 과정 실습문제 3번
# wrapper() 함수와 데코레이터를 사용하여 함수 구현

# 2. 함수를 입력 받고 입력 받은 함수가 실행 되기 전에 "function calling" 문자열을 
#    출력하는 logged() 라는 이름의 wrapper 함수를 만들기
def logged(func):
    def wrapper(*args, **kwargs):
        print('function calling')
        return func(*args, **kwargs)
    return wrapper

# 1. 두 개의 정수를 입력 받고 더한 뒤 반환하는 add() 함수 만들기
# 3. 데코레이터 어노테이션을 사용하여 add()만 사용해도 logged() wrapper
#    함수가 실행되도록 만들기
@logged
def add(x, y):
    return x + y

print(add(1, 2))

