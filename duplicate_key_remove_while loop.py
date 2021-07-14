dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    } 
i=1
empty_dic=[]
while i<len(dic):
    if dic not in empty_dic:
        empty_dic.append(dic)
    i=i+1
print(empty_dic)