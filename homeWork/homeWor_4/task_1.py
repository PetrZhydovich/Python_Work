# Напишите функцию для транспонирования матрицы

def trans_matrix(a):   
    matrix =[]
    for i in range(0, len(a[0])):
        matrix.append([])
        for j in range(0, len(a)):
            matrix[i].append(a[j][i])
    
    return matrix

t_matrix = [[9, 1], [8, 2], [7, 3]]

print(trans_matrix(t_matrix))  