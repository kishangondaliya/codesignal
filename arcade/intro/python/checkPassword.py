def checkPassword(attempts, password):
    def check():
        while True:
            attemp = yield
            if attemp == password:
                yield True

    checker = check()
    for i, attempt in enumerate(attempts):
        next(checker)
        if checker.send(attempt):
            return i + 1

    return -1
