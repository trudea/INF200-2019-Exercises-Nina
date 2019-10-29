class Squared:
    def __init__(self, liste):
        self.liste = liste

    def squaring(self):
        for j in [i*i for i in self.liste]:
            yield j

def justagen(liste):
    for i in liste:
        yield i

if __name__ == "__main__":
    test = [1, 2, 3]
    klassevariabelen = Squared(test)
    generatorobjektet = klassevariabelen.squaring()
    print(next(generatorobjektet))
    print(next(generatorobjektet))

