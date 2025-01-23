from functools import singledispatch

class Shape:
    """
    Base class for all shapes.
    :param solid: Boolean indicating whether the shape is solid or hollow.
    """
    def __init__(self, solid: bool) -> None:
        self.solid = solid


class Circle(Shape):
    """
    Class representing a Circle.
    :param center: The center point of the circle.
    :param radius: The radius of the circle.
    :param solid: Boolean indicating whether the circle is solid or hollow.
    """
    def __init__(self, center: int, radius: int, solid: bool) -> None:
        super().__init__(solid)
        self.center = center
        self.radius = radius


class Parallelogram(Shape):
    """
    Class representing a Parallelogram.
    :param pa: Point A of the parallelogram.
    :param pb: Point B of the parallelogram.
    :param pc: Point C of the parallelogram.
    :param solid: Boolean indicating whether the parallelogram is solid or hollow.
    """
    def __init__(self, pa: int, pb: int, pc: int, solid: bool) -> None:
        super().__init__(solid)
        self.pa = pa
        self.pb = pb
        self.pc = pc


class Triangle(Shape):
    """
    Class representing a Triangle.
    :param pa: Point A of the triangle.
    :param pb: Point B of the triangle.
    :param pc: Point C of the triangle.
    :param solid: Boolean indicating whether the triangle is solid or hollow.
    """
    def __init__(self, pa: int, pb: int, pc: int, solid: bool) -> None:
        super().__init__(solid)
        self.pa = pa
        self.pb = pb
        self.pc = pc


@singledispatch
def draw(shape: Shape) -> None:
    """
    Generic draw function for shapes.
    :param shape: The shape to be drawn.
    :raises TypeError: If the shape type is not registered.
    """
    raise TypeError(f"Don't know how to draw {shape}.")


@draw.register
def _(shape: Circle) -> None:
    """
    Draws a Circle.
    :param shape: The Circle to draw.
    """
    print("\u25CF" if shape.solid else "\u25A1")


@draw.register
def _(shape: Parallelogram) -> None:
    """
    Draws a Parallelogram.
    :param shape: The Parallelogram to draw.
    """
    print("\u25B0" if shape.solid else "\u25B1")


@draw.register
def _(shape: Triangle) -> None:
    """
    Draws a Triangle.
    :param shape: The Triangle to draw.
    """
    print("\u25B2" if shape.solid else "\u25B3")


def main() -> None:
    """
    Main function to create shapes and draw them.
    """
    shapes = [
        Circle(center=0, radius=4, solid=True),
        Parallelogram(pa=2, pb=4, pc=6, solid=True),
        Triangle(pa=2, pb=4, pc=6, solid=False),
    ]
    for shape in shapes:
        draw(shape)


if __name__ == "__main__":
    main()
