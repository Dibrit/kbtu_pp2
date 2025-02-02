def solve(n):
    d= []
    for i in range(len(n)):
        d.append(n[len(n) - i - 1] )
    return d

m = input().split()
print(solve(m))