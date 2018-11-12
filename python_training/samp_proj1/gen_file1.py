
# generator can be created in two ways - generator function , generator comprehension

def fun_a():
    return "a"


def gen_a():
    yield "a"
    yield "b"
    yield "c"

print(fun_a())
ret = gen_a()
print(type(ret))
print(next(ret))
print(next(ret))
print(next(ret))
# generator can contain many yield statements