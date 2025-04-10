class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Generator function that yields the length and width in order
        yield {'length': self.length}
        yield {'width': self.width}



r = Rectangle(10, 5)

for item in r:
    print(item)
