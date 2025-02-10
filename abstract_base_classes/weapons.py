class SwordMeta(type):

    def __subclasscheck__(cls, subclass):
        return (
            hasattr(subclass, 'swipe') and callable(subclass.swipe) and hasattr(subclass, 'sharpen') and callable(subclass.sharpen)
        )


class Sword(metaclass=SwordMeta):
    pass


class BroadSword:

    def swipe(self):
        print("Swoosh!")

    def sharpen(self):
        print("Shink!")


class SamuraiSword:

    def swipe(self):
        print("Slice!")

    def sharpen(self):
        print("Shink!")


class Rifle:

    def fire(self):
        print("Bang!")