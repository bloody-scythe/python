def morse():
    with open("morse") as f:
        code = {}
        for line in f:
            line = line.split(':')
            code.setdefault(*line)
        return code

