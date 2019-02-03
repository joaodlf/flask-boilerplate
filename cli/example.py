"""Example script. Serves as an example for further script development.

Usage:
    example.py NUM1 NUM2

Options:
    -h --help      Show this screen.

"""

from docopt import docopt
from logzero import logger

from cli import Cli


def run(args):
    cli = Cli("example")
    num1 = int(args["NUM1"])
    num2 = int(args["NUM2"])

    total = num1 + num2
    total_minus_one = total - 1

    logger.info(f"{num1} plus {num2} is {total}")
    logger.info(f"minus 1 that's {total_minus_one}")
    logger.warn("QUICK MATHS")


if __name__ == "__main__":
    arguments = docopt(__doc__)
    run(args=arguments)
