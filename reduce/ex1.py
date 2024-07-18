import functools
nums=[5,8,2,10,9]
def sum_of_all(a,b):
    return a+b
print(functools.reduce(sum_of_all,nums))