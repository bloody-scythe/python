
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

clear = "[H[2J[3J"
def cls():
    print(clear)


