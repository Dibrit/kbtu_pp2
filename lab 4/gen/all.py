def a1(n):
    for i in range(n + 1):
        yield i ** 2

def a2(n):
    return ", ".join(str(i) for i in range(n + 1) if i % 2 == 0)


def a3(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def a4(a, b):
    for i in range(a, b + 1):
        yield i ** 2


def a5(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
print(a2(n))

a = int(input())
b  = int(input())
for i in a4(a, b):
    print(i)
    
n = int(input()) 
for i in a5(n):
    print(i)
