#!/usr/bin/env python
import sys
import os
from importlib import import_module
import inspect

def main():
    directory = 'solutions'
    argcount = len(sys.argv)

    #check if arguments are correct
    if argcount <= 1:
        print('Use command "./run.py --usage" for help.')
        exit()
    elif sys.argv[1] == "--usage":
        print('Usage: ./run.py <filename.py> <args>\nStore solutions in the "{directory}/" directory11\ncat solutions/125-valid_palindrome.py | xclip -sel clip')
        exit()
    elif argcount == 2:
        print('Not enough arguments')
        exit()
    else:
        path = sys.argv[1]
        args = sys.argv[2:]
        print(f'File path  = {path}')
        print(f'Arguments = {args}\n')
        
    #What to do if the correct amount of arguments are correct
    #check if file exists
    fname = ('./' + path).split('/')[-1] 
    if fname in os.listdir(directory):
        #get module name (the '.' splits the direcories instead of '/')
        module = import_module(directory + '.' + fname.split('.')[0])

        #get first class in file
        Solution = getattr(module, dir(module)[0])
        
        #create instance of class
        sol = Solution()

        #get first function and call it
        func = getattr(sol, [f for f in dir(sol) if f.startswith('__') == False][0]) #if callable(f)])
        print('Output:')
        func(args[0])
        
    else:
        print(f'File not found in "{directory}/" directory.')

if __name__ == "__main__":
    main()
