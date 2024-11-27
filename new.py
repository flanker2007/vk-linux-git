m, n = map(int, input().split())

matrix = []

for i in range(m):
    matrix.append(list(map(int, input().split()[:n])))

count_bottom = 1
count_top = 1
temp = 0

if(m != n):
    print("Матрица не является особенной")
else:
    for i in range(1, m):
        for j in range(0, count_bottom):
            if(matrix[i][j] != 0):
                temp += 1 
        count_bottom += 1

    if(temp > 0):
        print("Матрица не является особенной")
    else:
        for i in range(0, m):
            for j in range(count_top, n):
                if(matrix[i][j] != 0):
                    temp += 1 
            count_top += 1

        if(temp > 0):
            print("Матрица верхнетреугольная")
        else:
            for i in range(m):
                if(matrix[i][i] != 1):
                        temp += 1
                        
            if(temp > 0):
                print("Матрица диагональная")
            else:
                print("Матрица единичная") 

print("merge-conflict-branch")