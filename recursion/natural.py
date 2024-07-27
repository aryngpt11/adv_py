#Direct Recursion
def natural_num(n,stop):
    print(n)
    if n==stop:
        return n
    else:
        return natural_num(n+1,stop)
natural_num(1,50)