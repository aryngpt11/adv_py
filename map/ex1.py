names=['ayush','arya','aryan','arav']
def find_len(name):
    return name,len(name)
#print(list(map(find_len,names)))
mapped_obj=map(find_len,names)

for ele in mapped_obj:
    print(ele[0],'---->',ele[1])