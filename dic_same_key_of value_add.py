d1={1:10,2:20}
d2={3:30,2:40}
d3={5:50,6:60}
empty={}
for i in d1:
    for j in d2:
        for k in d3:
            if i==j or j==k:
                empty[i]=d1[i]+d2[j]
            else:
                empty[i]=d1[i]
                empty[j]=d2[j]
                empty[k]=d3[k]
print(empty)