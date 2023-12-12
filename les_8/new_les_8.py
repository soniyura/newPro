
def log(func):
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("file.txt", "w") as f:
            f.write(str(result))
        return result
    return wrapped()

def add(a: int, b: int) -> int:
    res = a + b
    with open("file.txt", "w") as f:
        f.write(str(res))
    return res

add = log(add)