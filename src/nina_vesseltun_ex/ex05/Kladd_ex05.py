class Generator_class:
    def __init__(self, length):
        self.length = length

    def rand(self):
        for i in range(self.length):
            yield i

if __name__ == "__main__":
    class_object = Generator_class(10)
    for i in class_object.rand():
        print(i)

    liste = [1, 2, 3, 4]
    iterator = iter(liste)
    for i in range(len(liste)):
        print(next(iterator))