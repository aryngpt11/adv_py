str1="AryaN"
str1=str1.lower()
vowels=['a','e','i','o','u']
# def vow(ch):
#     if ch in vowels:
#         return True
vow=lambda ch:ch in vowels

print(list(filter(vow,str1)))