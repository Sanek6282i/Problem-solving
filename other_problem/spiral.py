"""
Print an n × n table filled with numbers from 1 to n ^ 2 in a spiral
starting from the upper left corner and twisted clockwise
"""

n = int(input())
matrix = [[0] * n for _ in range(n)]  # zero matrix n x n
counter = 1
si = 0
sj = 0
ei = n - 1
ej = n - 1
flag = True
while flag:
    for i in range(n):  # first line
        matrix[0][i] = counter
        counter += 1
    for i in range(si, ei + 1):  # j = end_j
        if counter > n ** 2:
            flag = False
            break
        matrix[i][ej] = counter
        counter += 1
    for j in range(ej, sj, -1):  # i = end_i
        if counter > n ** 2:
            flag = False
            break
        matrix[ei][j] = counter
        counter += 1
    for i in range(ei, sj, -1):  # j = start_j
        if counter > n ** 2:
            flag = False
            break
        matrix[i][sj] = counter
        counter += 1

print(*matrix, sep='\n')


