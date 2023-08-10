class Evaluator:
    def __init__(self, program=None) -> None:
        self.program = program
        self.pending = []

    def add_program(self, expression):
        self.program = expression


    def is_comment(self, item):
        return isinstance(item, str) and item.startswith('#')

    def evaluate(self):

        while self.program:
            item = self.program.pop()
            if not self.is_comment(item):
                self.program.append(item)
                break
        else:
            print("Program is empty")

        while self.program:
            item = self.program.pop()
            if callable(item):
                pass
        # end while
