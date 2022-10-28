import sys
import os
from importlib import import_module
import inspect

argcount = len(sys.argv)

if argcount <= 1:
    print('Use command "python3 run.py --usage" for help.')
    exit()
elif sys.argv[1] == "--usage":
    print("Usage: python3 run.py <filename.py> <args>")
    exit()
elif argcount == 2:
    print("Not enough arguments")
    exit()
else:
    fname = sys.argv[1]
    args = sys.argv[2:]
    print(f"Filename   = {fname}")
    print(f"Argunments = {args}\n")
    
if fname in os.listdir('.'):
    module = import_module(fname.split('.')[0])
    Solution = getattr(module, dir(module)[0])
    sol = Solution()
    func = getattr(sol, [f for f in dir(sol) if f.startswith("__") == False][0]) #if callable(f)])
    print("Output:")
    func(args[0])
else:
    print("File not found")


#### OLD CODE ###
#print(getattr(dir(module)[0], 'isPalindrome'))
#print(f"functions = {functions}")
#print([f for f in inspect.getmembers(classes[0], predicate=inspect.isfunction)]) #if callable(f)])
#print(classes[0].stream
#function = getattr(module, classes[0], )
#print(function)
