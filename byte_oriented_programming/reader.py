import struct

class Vector:
    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Vector({self.x}, {self.y}, {self.z})'

class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f'Color({self.red}, {self.green}, {self.blue})'

class Vertex:
    def __init__(self, vector, color):
        self.vector = vector
        self.color = color

    def __repr__(self):
        return f'Vertex({self.vector}, {self.color})'


def make_color_vertex(x, y, z, red, green, blue):
    return Vertex(Vector(x, y, z), Color(red, green, blue))

def main():
    with open("colors.bin", "rb") as f:
        buffer = f.read()

    vertices = [make_color_vertex(*fields) for fields in struct.iter_unpack('@3f3Hxx', buffer)]

    print(vertices)

if __name__ == "__main__":
    main()
