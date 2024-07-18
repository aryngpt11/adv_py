import functools
nums=[5,8,2,10,9]

def max1(a,b):
    if a>b:
        return a
    else:
        return b
print(functools.reduce(max1,nums))