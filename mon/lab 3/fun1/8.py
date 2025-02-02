def spy_game(n):
    for i in range (2, len(n)):
        if int(n[i]) == 7: 
            if (int(n[i-2]) == 0 and int(n[i-1]) == 0):
                return True
    return False

m = input().split()
print(spy_game(m))