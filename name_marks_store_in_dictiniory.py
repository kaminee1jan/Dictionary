dictionary = {}
count = 0
while count<10:
   name = input("Enter your name")
   mark = int(input("Enter your mark out of 100"))
   if name not in dictionary:
       dictionary[name] = mark
       count = count + 1
#    else:
#        name = raw_input("Enter a unique name: ")
#        mark = input("Enter the mark out of 100: ")
#        if name not in dictionary:
#           dictionary[name] = mark
#           count = count + 1
print(dictionary)

