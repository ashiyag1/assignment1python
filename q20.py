#20. Write a python program that takes a list of numbers and returns their sum.
numberofinputs=int(input("Enter the count of numbers you would take as input:"))
list1=[]
for i in range(numberofinputs):
    num=int(input("Enter the numbers"))
    list1.append(num)
print("The list you entered:",list1)    
sum=0    
for j in list1:
    sum=sum+j
print(sum)    
