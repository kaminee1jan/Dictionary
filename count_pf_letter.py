st=input("enter the string")
dic={}
for x in st:
    if x in dic:
        dic[x]=dic[x]+1
    else:
        dic[x]=1
for key in dic:
    print(key,":",dic[key])


str=input("enter the string")
count={}
for i in str:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for i in count:
    print(i,":",count[i])