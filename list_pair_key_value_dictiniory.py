l=[1,2,3,4,5]
d={}
i=1
while i<len(l):
    j=1
    while j<l[i]:
        d[i]=l[j]
        j=j+1
    i=i+1
print(d)

l=[1,2,3,4,5]
d={}
i=1
while i<len(l):
    j=1
    while j<l[i]:
        # d[i]=l[j]
        d[i]=l[j]
        j=j+2
    i=i+2
print(d)
