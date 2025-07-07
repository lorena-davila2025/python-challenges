'''
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
'''

import math

def calculate_polygon_area(polygon):
    area = None
    a = polygon["a"]
    if polygon["type"] == "Triangle":
        b = polygon["b"]
        c = polygon["c"]
        semi_perimeter = ( a + b + c) / 2
        result = semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)
        area = math.sqrt(result)
    elif polygon["type"] == "Rectangle":
        b = polygon["b"]
        area = a * b
    else:
        area = a * 2
    return area

t = {
    "type": "Triangle",
    "a": 3,
    'b': 4,
    'c': 5,
}
result = calculate_polygon_area(t)
print(t, result)

s = {
    "type": "Square",
    "a": 3
}
result = calculate_polygon_area(s)
print(s, result)

r = {
    "type": "Rectangle",
    "a": 3,
    'b': 4,
}
result = calculate_polygon_area(r)
print(r, result)


# testing with classes

class Polygon:
    def __init__(self, type: str):
        self.type = type
        self.area = None

    def calculate_area(self):
        return self.area

class Rectangle(Polygon): # if no height is passed assume Square
    def __init__(self, width, height = None):
        super().__init__("Rectangle")
        self.width = width
        self.height = width if height is None else height

    def calculate_area(self):
        self.area = self.width * self.height
        return self.area

class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        semi_perimeter = (self.a + self.b + self.c) / 2
        result = semi_perimeter * (semi_perimeter - self.a) * (semi_perimeter - self.b) * (semi_perimeter - self.c)
        self.area = math.sqrt(result)
        return self.area

rect = Rectangle(3, 6)
print("rect1", rect.__getstate__())
rect.calculate_area()
print("rect",rect, rect.area)

triangle = Triangle(3, 4, 5)
triangle.calculate_area()
print("Triangle area:", triangle.area)

square = Rectangle(4)
square.calculate_area()
print("Square area:", square.area)
