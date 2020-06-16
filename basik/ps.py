# Returns a list of all running processes
def proc_list():
    from sh import ps
    from re import findall
    list = findall(r'\s\S*\n', ps("-e").stdout.decode())
    procs = []
    for item in list:
        procs.append(item.strip())
    return procs


# Check if a program is running
def running(name):
    return name in proc_list()
# Check if a program is running but requires psutil
def running_fast(name): 
    from psutil import process_iter
    for proc in process_iter():
        if name.lower() in proc.name().lower():
            return True
    return False
