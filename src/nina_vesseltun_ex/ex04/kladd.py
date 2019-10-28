class ListRand:
    def __init__(self, liste):
        self.liste = liste

    def rand(self):
        for i in self.liste:
            yield i


if __name__ == "__main__":
    tall = list(range(5))
    print(tall)
    klasse = ListRand(tall)
    x = klasse.rand()
    for i in range(5):
        print(next(x))

    print(next(x))
