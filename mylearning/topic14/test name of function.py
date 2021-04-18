def logger(func):


    def inner(a, * ta):


        print(func.__name__)
        return func(a, * ta)
    return inner

@logger    

def big_sum(a, * ta):


    s = a
    for i in ta:
        s += i
    return s


print(big_sum(1,2,3,4,5))


