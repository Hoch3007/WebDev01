def check_subtract():

    assert subtract(5, 2) == 3
    assert subtract(10, 10) == 0
    assert subtract(5.2, 4.9) == 0.3


def subtract(a, b):

    return round(a-b, 1)


if __name__ == '__main__':
    check_subtract()
    print("Passed all tests")

