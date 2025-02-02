import struct

class Vector:
    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

def main():
    with open("colors.bin", "rb") as f:
        buffer = f.read()

    items = struct.unpack_from('@fffHHH', buffer)

    print(repr(items))

if __name__ == "__main__":
    main()
