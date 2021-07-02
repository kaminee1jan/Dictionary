list1_keys=["one","two","three","four","five"]
list2_value=[1,2,3,4,5,]
empty_dict={}
for key in list1_keys:
    for value in list2_value:
        empty_dict[key] = value
        list2_value.remove(value)
        break 
print("dictiniory is",empty_dict)
