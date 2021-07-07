dict1 = {1:"kaminee",3:"rupali",2:"prgana"}
sorted_values = sorted(dict1.values()) 
sorted_dict = {}
for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            # break

print(sorted_dict)
