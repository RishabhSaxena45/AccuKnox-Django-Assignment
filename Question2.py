class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
        self.dimensions = [{'length': self.length}, {'width': self.width}]
        
    def __iter__(self):
        return iter(self.dimensions)

rect = Rectangle(length=20, width=15)

for dimension in rect:
    print(dimension)