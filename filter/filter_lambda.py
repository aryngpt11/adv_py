data=[60,67,86,45,66,54,31,98,63]
# def even_num(num):
#     if num%2==0:
#         return True
filtere_objs=filter(lambda num:num>=60,data)
print(list(filtere_objs))