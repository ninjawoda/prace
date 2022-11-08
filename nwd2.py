def nwd_i(a, b):
    while b > 0:
        a, b = b, a%b
    return a
print(nwd_i(9,3))