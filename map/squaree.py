nums=[2,3,4,5,6,7,8]
# def squaree(s):
#     return s**2
squaree=lambda n:n**2
mapped_obj=map(squaree,nums)
print(list(mapped_obj))