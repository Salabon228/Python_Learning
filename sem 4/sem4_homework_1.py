def transposition(matrix: list[int]) -> list[int]:
    # Определение размеров исходной матрицы
    rows = len(matrix)
    cols = len(matrix[0])

    # Создание пустой транспонированной матрицы
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix


matrix = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]

transposition(matrix)


def print_matrix(data: list) -> None:
    res = []
    for i in data:
        for j in i:
            res.append(j)
        print(i)

print_matrix(transposition(matrix))
