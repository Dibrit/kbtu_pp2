import re

a = input()
c = r'^[a-z]+_[a-z]+$'
if re.fullmatch(c, a):
    print("yes")
else:
    print("no")