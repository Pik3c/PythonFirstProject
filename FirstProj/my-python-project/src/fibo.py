# Fibonacci numbers module

def fib(n):
    """Write Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Return Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def add_three_numbers(a, b, c):
    """Return the sum of three numbers."""
    return a + b + c

print (add_three_numbers(4,4,4))

#if __name__ == "__main__":
