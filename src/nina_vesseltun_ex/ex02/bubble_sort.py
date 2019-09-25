def bubble_sort(data):    # endrer koden inne i funksjonen også listen utenfor?
    copy = list(data)     # er dette ok?
    for i in range(len(copy)-1):
        for j in range(len(copy)-i-1):
            if copy[j] > copy[j+1]:
                copy[j], copy[j+1] = copy[j+1], copy[j]
    return copy


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
