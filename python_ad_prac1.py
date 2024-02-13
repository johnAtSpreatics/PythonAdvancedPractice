# 파이썬 심화 과정 실습문제 1번
# enumerate()와 2중 for문을 사용하여 행렬 표시하기

matrix = [[11, 12, 13],
          [21, 22, 23],
          [31, 32, 33]]

for r, row in enumerate(matrix):
    for c, value in enumerate(row):
        print("Row %d, Column %d: %d" %((r + 1), (c + 1), value))
