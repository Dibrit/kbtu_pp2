import re

def a1(text):
    return re.findall(r'\b[A-Z][a-z]+\b', text)

def a2(text):
    return bool(re.fullmatch(r'a.*b', text))

def a3(text):
    return re.sub(r'[ ,.]', ':', text)

def a4(text):
    return ''.join(i.capitalize() for i in text.split('_'))

def a5(text):
    return re.split(r'(?=[A-Z])', text)

def a6(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

def a7(text):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower()

b = input()
print(a1(b))

b = input()
print(a2(b))

b = input()
print(a3(b))

b = input()
print(a4(b))

b = input()
print(a5(b))

b = input()
print(a6(b))

b = input()
print(a7(b))
