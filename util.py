import sys

# Takes a file and iterates on it in chunks of 'block'
def rblocks(file, block=32):
    chunk = '0'
    while len(chunk) > 0:
        chunk = file.read(block)
        yield chunk

# Takes a function and it arguments and returns the time it took to run
def runtime(func, *arg, unit = 'sec'):
    from time import time
    oldtime = time()
    ret = func(*arg)
    if unit == 'sec':
        took = (time() - oldtime)
    elif unit == 'mil':
        took = (time() - oldtime) * 1000
    elif unit == 'min':
        tool = (time() - oldtime) / 60
    return {'f_return' : ret, 'time' : took}

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
def mod_find(module):
    command = "import %s\nglobal _\n_ = %s.__file__"
    exec(command % (module,module))
    return _

if __name__ == "__main__":
    if sys.argv[1] == "mod_find":
        try:
            print(mod_find(sys.argv[2]))
        except:
            print("ERROR: Module file not found!")

# Gets a character from input without waiting
# def getch():
#     from tty import setcbreak as cbreak
#     import termios
#     import sys
#     old = termios.tcgetattr(sys.stdout)
#     cbreak(sys.stdout)
#     char = input()
#     termios.tcsetattr(sys.stdout, termios.TCSAFLUSH, old)

# Checks if a program is running

def running(name): #Check if a program is running
    import psutil
    for proc in psutil.process_iter():
        if name.lower() in proc.name().lower():
            return True
    return False
