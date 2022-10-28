import sys
import os
from importlib import import_module
import inspect

argcount = len(sys.argv)

#check if arguments are correct
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
    
#What to do if the correct amount of arguments are correct
#check if file exists
if fname in os.listdir('.'):
    #get module name
    module = import_module(fname.split('.')[0])
    
    #get first class in file
    Solution = getattr(module, dir(module)[0])
    
    #create instance of class
    sol = Solution()

    #get first function and call it
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
