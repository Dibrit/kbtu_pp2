def histogram(n):
    for i in n:
        i = int(i)
        for j in range (i):
            print("*", end="")
        print()

m = input().split()
histogram(m)