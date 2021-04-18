def logger(func):


    def inner(a, * ta):

        str_res = func.__name__ + ", " + str(a)
        for s in ta:
            str_res = str_res + ", " + str(s)
        print(str_res)
        return func(a, * ta)
    return inner

@logger    

def big_sum(a, * ta):

    s = str(a)  
    for i in ta:
        s += str(i)
    return s


print(big_sum(1,2,3,4,5))


