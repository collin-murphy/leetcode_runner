import sys
import os
from importlib import import_module
import inspect

argcount = len(sys.argv)

if argcount <= 1:
    print('Use command "python3 run.py --usage" for help.')
    exit
elif sys.argv[1] == "--usage":
    print("Usage: python3 run.py <filename.py> <args>")
    exit
else:
    fname = sys.argv[1]
    args = sys.argv[2:]
    print(f"Filename = {fname}")
    print(f"Args = {args}")
    
if fname in os.listdir('.'):
    module = import_module(fname.split('.')[0])

#module.Solution().isPalindrome(args[0])

classes = [x for x in dir(module) if inspect.isclass(getattr(module, x))]
functions = dir(classes[0])
print([f for f in functions if "__" in f])
#function = getattr(module, classes[0], )
#print(function)
