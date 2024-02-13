# 파이썬 심화 과정 실습문제 5번
# 코루틴을 생성하고 값 주고 받기

# 1. 새로운 값이 추가될 때마다 값을 누적하여 평균을 계산해주는 코루틴 
#    avg_coroutine() 함수 만들기
def avg_coroutine():
    sum = 0
    average = 0
    count = 1
    while True:
        x = (yield average) 
        sum += x
        average = sum / count        
        # 3. 코루틴에서는 계산 횟수, 누적 값을 출력
        print("cr: count %d, total %d" %(count, sum))
        count += 1
        
co = avg_coroutine()
next(co)

# 2. 1부터 5까지 값을 코루틴으로 전달하기
# 4. 메인 루틴에서는 코루틴으로부터 받은 평균 값을 출력
print("main: average %0.1f" %co.send(1))
print("main: average %0.1f" %co.send(2))
print("main: average %0.1f" %co.send(3))
print("main: average %0.1f" %co.send(4))
print("main: average %0.1f" %co.send(5))

