def has_33(n):
    for i in range (1, len(n)):
        if int(n[i]) == 3 and int(n[i-1]) == 3:   
           return True
    return False

m = input().split()
print(has_33(m))