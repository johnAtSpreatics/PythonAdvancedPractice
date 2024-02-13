# 파이썬 심화 과정 실습문제 4번
# 2차원 리스트 및 2중 for문 활용하기 

import random
from pprint import pprint

matrix = []

# 1. 랜덤한 2자리 수로 채워진 10x10 크기의 2차원 리스트를 만들기
for i in range(10):
    line = []
    for j in range(10):
        line.append(random.randrange(10, 100))
    matrix.append(line)
    
# 2. 만들어진 2차원 리스트에서 30보다 크고, 60보다 작은 값을 찾아서 11로 바꾸기
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if 30 < matrix[i][j] and matrix[i][j] < 60:
            matrix[i][j] = 11
            
# 3. 11이 아닌 값의 전체 평균을 구하고 11이 아닌 값을 전부 전체 평균 값으로 변경하기
sum = 0
count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != 11:
            sum += matrix[i][j]
            count += 1
            
average = int(sum / count) # 11이 아닌 값의 평균, 정수형

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != 11:
            matrix[i][j] = average
            
pprint(matrix, indent = 1, width = 100) # 보기 좋게 출력하기