import sys

if "pytest" in sys.modules:
    from config.test_config import *
else:
    from config.config import *
