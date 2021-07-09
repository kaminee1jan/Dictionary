dict1={'a': 67, 'b': 23, 'c': 45,'d': 56, 'e': 12, 'f': 69}
max1=0
sec=0
third=0
for i in dict1:
    if dict1[i]>max1:
        max1=dict1[i]
print(max1)
for j in dict1:
    if sec<dict1[j]<max1:
        sec=dict1[j]
print(sec)
for k in dict1:                     
    if third<dict1[k]<sec:
        third=dict1[k]
print(third)

