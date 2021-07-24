name=input("enter the string")
i=0
empty_dict={}
while i<len(name):
    empty_dict[name[i]]=name
    i=i+1
print(empty_dict)