import os

for i in range(65, 91): 
    fn = f"{chr(i)}.txt"
    with open(fn, "w") as f:
        f.write({fn})