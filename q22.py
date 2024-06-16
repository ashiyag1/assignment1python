#22. Write a python program that returns the minimum and maximum values in a list of numbers.
number_of_inputs=int(input("Enter the count of numbers you would take as input:"))
list1=[]
for i in range(number_of_inputs):
    num=int(input("Enter the numbers:"))
    list1.append(num)
print("The list you entered:",list1)    
print("The minimum value of list:", min(list1))
print("The maximum value of list:", max(list1))
