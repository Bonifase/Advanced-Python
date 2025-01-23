from typing import Any, Callable, List, Optional
import operator

class Evaluator:
    def __init__(self, program: Optional[List[Any]] = None) -> None:
        """
        Initializes the Evaluator object.
        :param program: A list representing the program (optional).
        """
        self.program: List[Any] = program if program is not None else []
        self.pending: List[Any] = []

    def add_program(self, expression: List[Any]) -> None:
        """
        Sets or replaces the program with a new one.
        :param expression: A list representing the program to be executed.
        """
        if not isinstance(expression, list):
            raise TypeError("Program must be a list.")
        self.program = expression

    @staticmethod
    def is_comment(item: Any) -> bool:
        """
        Checks if a given item is a comment.
        :param item: The item to check.
        :return: True if the item is a string starting with '#', False otherwise.
        """
        return isinstance(item, str) and item.startswith('#')

    def clean_program(self) -> None:
        """
        Removes comments from the program.
        """
        self.program = [item for item in self.program if not self.is_comment(item)]
        if not self.program:
            raise ValueError("Program contains no executable instructions.")

    def evaluate(self) -> None:
        """
        Executes the program by evaluating the instructions in a stack-based manner.
        """
        try:
            self.clean_program()  # Remove comments before starting evaluation.

            while self.program:
                item = self.program.pop()
                if callable(item):
                    self._process_callable(item)
                else:
                    self.pending.append(item)

            # If no break occurred during the loop, print the final result.
            print("Program executed successfully.")
            print("Result:", self.pending)

        except Exception as error:
            print(f"Error during evaluation: {error}")

    def _process_callable(self, func: Callable) -> None:
        """
        Processes a callable function/operator.
        :param func: The callable to apply to the pending stack.
        """
        try:
            result = func(*self.pending)
            self.pending.clear()
            self.program.append(result)
        except Exception as error:
            raise RuntimeError(f"Failed to execute function {func}: {error}")

if __name__ == "__main__":
    # Define a stack-based program.
    expression = list(reversed((
        "# A short stack program to add",
        "# And multiply some constants.",
        5,              # Push 5 onto the stack.
        2,              # Push 2 onto the stack.
        operator.add,   # Add the top two numbers (5 + 2).
        7,              # Push 7 onto the stack.
        operator.mul    # Multiply the top two numbers (7 * 7).
    )))

    # Initialize the evaluator and execute the program.
    evaluator = Evaluator()
    evaluator.add_program(expression)
    evaluator.evaluate()
