def odd_one(L):
    types = [type(value) for value in L]

    for value_type in types:
        if types.count(value_type) == 1:
            return value_type.__name__


print(odd_one(eval(input().strip())))