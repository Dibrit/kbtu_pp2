a1 = int(input())
if a1 == 1:
    print(10 > 9)
    print(10 == 9)
    print(10 < 9)
elif a1 == 2:
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    else:
        print("b is not greater than a")
elif a1 == 3:
    print(bool("Hello"))
    print(bool(15))
elif a1 == 4:
    x = "Hello"
    y = 15
    print(bool(x))
    print(bool(y))
elif a1 == 5:
    print(bool("abc"))
    print(bool(123))
    print(bool(["apple", "cherry", "banana"]))
elif a1 == 6:
    print(bool(False))
    print(bool(None))
    print(bool(0))
    print(bool(""))
    print(bool(()))
    print(bool([]))
    print(bool({}))
elif a1 == 7:
    x = 200
    print(isinstance(x, int))