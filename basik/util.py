import sys

# Takes a function and it arguments and returns the time it took to run
def runtime(func, *arg, unit='sec', prec=2):
    from time import time
    oldtime = time()
    ret = func(*arg)
    newtime = time()
    if unit == 'sec':
        took = (newtime - oldtime)
    elif unit == 'min':
        took = (newtime - oldtime) / 60
    elif unit == 'mil':
        took = (newtime - oldtime) * 1000
    else:
        raise Exception("Unknown unit")
    return round(took, prec) , ret

# Runs python script file
def run(file):
    with open(file) as f:
        code = compile(f.read(), file, 'exec')
        exec(code)

# Clears the screen
clear = "[H[2J[3J"
def cls():
    print(clear)

# Returns the full path to given module name
def modfind(module):
    from sys import argv
    command = "import %s\nglobal _\n_ = %s.__file__"
    exec(command % (module, module))
    return _
