def yield_fun():
    a = 1
    b = 2
    yield a
    yield b


print(yield_fun())


generator = yield_fun()
print(next(generator))

print(next(generator))

