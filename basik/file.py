# Takes a file and iterates on it in chunks of 'block'
def rblocks(file, block=32):
    chunk = '0'
    while len(chunk) > 0:
        chunk = file.read(block)
        yield chunk

