import re

a = input()
c = r'^ab*$'
if re.fullmatch(c, a):
    print("yes")
else:
    print("no")