import random

def histogram(c, i):
    print("Take a guess.")
    a = int(input())
    if( a > c):
        print("Your guess is too high.")
        return histogram(n, i+1)
    elif( a < c):
        print("Your guess is too low.")
        return histogram(n, i+1)
    else:
        return i
    

print("Hello! What is your name?")
a = input()
n = random.randint(1, 20)
print("Well", a, ", I am thinking of a number between 1 and 20.")
i= 0;
print("Good job", a ,"!You guessed my number in", histogram(n, i))