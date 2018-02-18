import fire
from logzero import logger

from cli import Cli


class Example(Cli):
    def __init__(self):
        Cli.__init__(self)

    def example(self, num1: int = 2, num2: int = 2):
        self.start("example")

        total = num1 + num2
        total_minus_one = total - 1

        logger.info(f"{num1} plus {num2} is {total}")
        logger.info(f"minus 1 that's {total_minus_one}")
        logger.warn("QUICK MATHS")


if __name__ == "__main__":
    fire.Fire(Example)
