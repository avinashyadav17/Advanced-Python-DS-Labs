def square_numbers(n):
    for i in range(n):
        yield i*i
for value in square_numbers(10):
    print(value)