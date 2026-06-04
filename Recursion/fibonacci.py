def fibonacci(n):

    # BASE CASE
    # fib(1) = 1 and fib(2) =1
    if n == 1 or n == 2:
        return 1
    
    # any other pos = prev + pos before that

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(103))