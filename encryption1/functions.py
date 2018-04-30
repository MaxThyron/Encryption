
def create_matrix(size):
    matrix = []

    for i in range(size):
        line = []
        for j in range(size):
            line.append(size * i + j + 1)
        matrix.append(line)

    return matrix

def create_null_matrix(size):
    null_matrix = []

    for i in range(size):
        null_matrix.append([0] * size)

    return null_matrix 

def rotate_matrix(base):  
    for i in range(len(base)//2):
        for j in range(i, len(base)-i-1):
            index1 = len(base)-i-1
            index2 = len(base)-j-1
            t = base[i][j]
            base[i][j] = base[index2][i]
            base[index2][i] = base[index1][index2]
            base[index1][index2] = base[j][index1]
            base[j][index1] = t

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print("%2s" % matrix[i][j], end = "")
        print()

def print_key(key):
    for value in key:
        print(value, end = " ")
    print()

def print_scrypt_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if i == n // 2 and j == 0:
                print("─" * (2 * n - n // 2) + "┼" + "─" * (2 * n - n // 2) + "\n" + "%2d" % matrix[i][j], end = " ")
            elif j == n // 2:
                print("│", "%2d" % matrix[i][j], end = " ")
            else:
                print("%2d" % matrix[i][j], end = " ")

        print()
