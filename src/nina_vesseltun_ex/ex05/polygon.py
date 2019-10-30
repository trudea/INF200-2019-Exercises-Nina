class Polygon:
    def __init__(self, points):
        self.points = [[float(x), float(y)] for x, y in points]
        self.current_idx = None

    def __repr__(self):
        return f'Polygon with {len(self)} points at {id(self)}'

    def __len__(self):
        return len(self.points)

    def __getitem__(self, item):
        return self.points[item]

    def __setitem__(self, item, value):
        x, y = value
        self.points[item] = [float(x), float(y)]

    def __add__(self, value):
        x_add, y_add = value
        points = [[x + float(x_add), y + float(y_add)] for x,y in self.points]
        return Polygon(points)

    def __radd__(self, value):
        return self + value

    def draw(self):
        return NotImplementedError

    def __iter__(self):
        return iter(PolygonPointIterator(self))

    def __next__(self):
        if self.current_idx == None:
            raise RuntimeError(f'{type(self)} is not initialized as an iterator')
        if self.current_idx == len(self):
            raise StopIteration
        point = self.points[self.current_idx]
        self.current_idx += 1
        return point

    def iterlines(self):
        for idx, point in enumerate(self):
            next_point = self[(idx + 1) % len(self)]
            yield [point, next_point]

class PolygonPointIterator:
    def __init__(self, polygon):
        self.polygon = polygon
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == len(self.polygon):
            raise StopIteration
        point = self.polygon[self.idx]
        self.idx += 1
        return point

class PolygonLineIterator:
    def __init__(self, polygon):
        self.polygon = polygon
        self.current_idx = None

    def __iter__(self):
        self.current_idx = 0
        return self

    def __next__(self):
        if self.current_idx == len(self.polygon):
            raise StopIteration
        first_point = self.polygon[self.current_idx]
        second_point = self.polygon[(self.current_idx + 1) % len(self.polygon)]
        self.current_idx += 1
        return [first_point, second_point]


class Rectangle(Polygon):
    def __init__(self, top_left, bottom_right):
        x_left, y_top = top_left
        x_right, y_bottom = bottom_right
        super().__init__([ [x_left, y_top], [x_left, y_bottom],
                           [x_right, y_bottom], [x_right, y_top] ])

class Square(Rectangle):
    def __init__(self, top_left, line_length):
        x_left, y_top = top_left
        bottom_right = [x_left + line_length, y_top - line_length]
        super().__init__(top_left, bottom_right)

for line in Polygon([[1, 2], [3, 4], [5, 6]]).iterlines():
    print(line)