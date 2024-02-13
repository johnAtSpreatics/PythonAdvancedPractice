matrix = [[11, 12, 13],
          [21, 22, 23],
          [31, 32, 33]]

for r, row in enumerate(matrix):
    for c, value in enumerate(row):
        print("Row %d, Column %d: %d" %((r + 1), (c + 1), value))