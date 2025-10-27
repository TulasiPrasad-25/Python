a = 3
b = 5
t1, t2 = a,b
while b > 0:
    r = a % b
    a =b
    b =r
gcd = a
print("gcd is", gcd)
lcm = (t1 * t2)/gcd
print("lcm is", lcm)