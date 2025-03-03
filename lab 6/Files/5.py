fn = "example.txt"  

n = int(input())

with open(fn, "w") as f:
    for line in range(n):
        b = input()
        f.write(b + "\n")