def fibonacci(n):
    if n < 0:
        fib = -1
    elif n == 0:
        fib = 0
    elif n == 1:
        fib = 1
    else:
        while n>0:
            num_1 = 0
            num_2 = 1


    return fib

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')