# Decorators is used to add extra features to an existing code.


def div(a,b):
    print(a/b)


# Take new function working as decorators
def smart_div(func):

    # define function in function which actually used to change code
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)

    return inner


div = smart_div(div)


div(2, 4)
