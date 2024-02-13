# 파이썬 심화 과정 실습문제 2번
# map()과 람다식을 사용하여 소수(Prime Number) 판별하기

num = int(input("소수인지 판단할 숫자를 입력하세요 :"))
num_list = list(range(2, num))

prime_list = list(map(lambda x:num % x == 0, num_list))

if True in prime_list:
    print("%d는 소수가 아닙니다." % num)
else:
    print("%d는 소수입니다." % num)