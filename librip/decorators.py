def print_result(any_func):
    def wrapper(*args):
        if len(args) == 0:
            result = any_func()
        else:
            result = any_func(args[0])
        print(any_func.__name__)
        if type(result) == list:
            for i in result:
                print(i)
        elif type(result) == dict:
            for key in result:
                print(str(key) + " = " + str(result[key]))
        else:
            print(result)
        return result
    return wrapper