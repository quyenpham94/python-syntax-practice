def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    total_left = 0
    total_right = 0

    for i in range(len(matrix)):
        total_left = total_left + matrix[i][i]
        total_right = total_right + matrix[i][-1-i]
    return  total_left + total_right
m1 = [
     [1,   2],
     [30, 40],
     ]
print(sum_up_diagonals(m1))
m2 = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     ]
print(sum_up_diagonals(m2))