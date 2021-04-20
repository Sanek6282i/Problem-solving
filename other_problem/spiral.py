"""
Print an n × n table filled with numbers from 1 to n ^ 2 in a spiral
starting from the upper left corner and twisted clockwise
"""

n = int(input())
matrix = [[0] * n for _ in range(n)]  # zero matrix n x n
counter = 1
start_i = 0
start_j = 0
end_i = n - 1
end_j = n - 1
flag = True
for i in range(n):  # first line
    matrix[0][i] = counter
    counter += 1
while flag:
    start_i += 1
    for i in range(start_i, end_i + 1):  # j = end_j
        if counter > n ** 2:
            flag = False
            break
        matrix[i][end_j ] = counter
        counter += 1
    end_j -= 1
    for j in range(end_j, start_j, -1):  # i = end_i
        if counter > n ** 2:
            flag = False
            break
        matrix[end_i][j] = counter
        counter += 1
    start_i += 1
    for i in range(end_i, start_j, -1):  # j = start_j
        if counter > n ** 2:
            flag = False
            break
        matrix[i][start_j] = counter
        counter += 1
    start_j += 1
    for j in range(start_j - 1, end_j):  # i = start_i
        if counter > n ** 2:
            flag = False
            break
        matrix[start_i][j] = counter
        counter += 1

print(*matrix, sep='\n')


