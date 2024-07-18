data={'nitesh':78,'rahul':98,'raj':91,'amar':90,'abhi':81}
# print(data['rahul'])
# print(data.keys())
def toppers(stud):
    return data[stud]>=90
print(list(filter(toppers,data)))