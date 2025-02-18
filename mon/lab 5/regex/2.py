import re

a = input()
c = r'^ab{2, 3}$'
if re.fullmatch(c, a):
    print("yes")
else:
    print("no")