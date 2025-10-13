def blocks(n):
    return 0 if n <= 0 else n + blocks(n - 1)


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = factorial(6)


def print_count_down(n):
    if n <= 0:
        print("BOOM")
    else:
        print(n)
        print_count_down(n - 1)


print_count_down(n)
