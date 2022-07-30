#This is a demo Python file for Git Tutorial
#Add some Python Code below!

#how to create a nested list in python?
#nested list is a list inside another list

ls1 = [23,45,51] #ls1 contains some data in the list format

newls = [] #creating a new list item wo any data

for i in range(1,10,2):
    newls.append(i)

newls.append(ls1)

print(newls)