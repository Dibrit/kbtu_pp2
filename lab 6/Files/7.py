

fn = "example.txt" 
fn1 = "example1.txt" 
with open(fn, "r") as b, open(fn1, "w") as f:
    f.write(b.read())