def spy_game(n):
    d = []
    for i in n:
        i = int(i)
        if i not in d:
            d.append(i)
    return d

m = input().split()
print(spy_game(m))