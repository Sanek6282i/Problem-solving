# put your python code here
"""
Print an n × n table filled with numbers from 1 to n ^ 2 in a spiral
starting from the upper left corner and twisted clockwise
"""

n = int(input())
matrix = [[0] * n for _ in range(n)]  # zero matrix n x n
counter = 1
si = 0
sj = 0
ei = n
ej = n
flag = True
while counter <= n ** 2:
    for i in range(si, ei):
        matrix[sj][i] = counter
        counter += 1
    for j in range(sj + 1, ej):
        matrix[j][ei - 1] = counter
        counter += 1
    for i in range(ei - 2, si - 1, -1):
        matrix[ej - 1][i] = counter
        counter += 1
    for j in range(ej - 2, sj, -1):
        matrix[j][si] = counter
        counter += 1
    si += 1
    sj += 1
    ei -= 1
    ej -= 1
for i in matrix:
    print(*i)
