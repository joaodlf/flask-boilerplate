import sys

if "pytest" in sys.modules:
    from config.config_example import *
else:
    from config.config import *
