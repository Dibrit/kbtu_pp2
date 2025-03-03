s = input()
s = s.lower().replace(" ", "") 
if s[::-1] == s:
    print("Yes")
else:
    print("No.")
