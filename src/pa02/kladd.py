def myfunc(a, b, *liste):
    print(a)
    print(b)
    for element in liste:
        print(element[0])

mylist = [3, 4]
myfunc(1, 2, mylist)