def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    list_of_squares = []
    for k in range(n):
        if k % 3 == 1:
            list_of_squares.append(k**2)
    return list_of_squares


if __name__ == '__main__':
    if squares_by_comp(10) != squares_by_loop(10):
        print('ERROR!')