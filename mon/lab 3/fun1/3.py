def solve(a, b):
    p = (a* 4 - b)//2
    return(p, a-p)

c = int(input())
d = int(input())
print(solve(c, d))