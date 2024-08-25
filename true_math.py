from math import inf


def divide(first, second):
    if second == 0:
        print(inf)
        return inf
    result = first / second
    print(result)


