def solve(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_prime(m):
    return [i for i in m if solve(int(i))]
    

m = input().split()
print(is_prime(m))