def histogram(n):
    for i in range(len(n) //2):
        if (n[i] != n[len(n) -1 - i]):
            return False
    return True

a = input()
print(histogram(a))