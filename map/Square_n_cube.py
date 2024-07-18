nums=[2,3,4,5,6,7,8,9]
def sq_n_cube(n):
    if n%2!=0:
        return n**2
    else:
        return n**3
mapped_obj=map(sq_n_cube,nums)
print(list(mapped_obj))