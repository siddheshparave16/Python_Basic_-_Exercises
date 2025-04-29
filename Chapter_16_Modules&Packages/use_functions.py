import math
import random
import sys

import functions


"""
- To use definitions and statements in a module in another module, we need to 'import' it into this module.  
- import functions make the definition in 'function.py' available in 'use_functions.py'
- Standard module - math, random
- User-defined module - functions
"""

functions.display()
functions.show()


# it runs as module with name __main__. It indicates that we are executing the main module.
print(__name__)


# a module can import multiple modules.

a = 100
b = 200

print(math.sin(0.5))
print(math.cos(0.5))
print(random.random())
print(random.randint(30, 45))


for p in sys.path:
    print(p)











