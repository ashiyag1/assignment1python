#21. Write a python program that counts the occurrences of a specific element in a list.
number_of_inputs=int(input("Enter the count of words you would take as input:"))
list1=[]
for i in range(number_of_inputs):
    char=input("Enter the words:")
    list1.append(char)
print("The list you entered:",list1)    
specific_element=input("enter the specific element:")
count=0
for word in list1:
    if (word==specific_element):
      count=count+1
       
print("The value of specific element:",count)