
def check_border(matrix_data, i, j):
    if matrix_data[i][j] == 0:
        return 0
    elif matrix_data[i][j] == 1:  # если 1, то ищем границы кратера
        temp[i][j] = ['X']  # записываем поля, которые мы уже проверили
        for k in [-1, 1]:
            x = i + k
            y = j
            if x < 0:
                continue
            if x > len(matrix_data) - 1:
                continue
            if temp[x][y] == ['X']:  # если X, то это поле мы уже проверяли
                return 0
            if matrix_data[x][y] == 0:
                continue
            elif matrix_data[x][y] == 1:
                temp[x][y] = ['X']
                check_border(matrix_data, x, y)

        for m in [-1, 1]:
            x = i
            y = j + m
            if y < 0:
                continue
            if y > len(matrix_data[0]) - 1:
                continue
            if temp[x][y] == ['X']:  # если X, то это поле мы уже проверяли
                return 0
            if matrix_data[x][y] == 0:
                continue
            elif matrix_data[x][y] == 1:
                temp[x][y] = ['X']
                check_border(matrix_data, x, y)
    return 1


def calculate(matrix_data):
    count_craters = 0
    global temp  # матрица полей, которые уже проверены
    temp = [['o' for _ in range(len(matrix_data[0]))] for _ in range(len(matrix_data))]
    for i in range(len(matrix_data)):
        for j in range(len(matrix_data[0])):
            count_craters += check_border(matrix_data, i, j)
    return count_craters


def read_file():
    data_file = []
    with open('files/4.txt', 'rt') as f:
        for line in f:
            data_file.append([int(x) for x in line.split()])
    return data_file


def check_craters():
    matrix = read_file()
    craters = calculate(matrix)
    print('craters =', craters)
    return craters


temp = []
check_craters()
