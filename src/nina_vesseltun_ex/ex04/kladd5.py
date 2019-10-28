class Even:
    def __init__(self, liste):
        self.liste = liste
        self.curren

    def evenf(self):
        for i in self.liste:
            yield i

numbers = [1, 2, 3, 4]
klasse = Even(numbers)
iterasjoner = klasse.evenf()
for j in iterasjoner:
    print(j)