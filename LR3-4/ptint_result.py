def print_result(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        temp = func(*args, **kwargs)
        if type(temp) is list:
            for el in temp: print(el)
        elif type(temp) is dict:
            for key,value in temp.items(): print(f"{key} = {value}")
        else: print(temp)
        return temp
    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
