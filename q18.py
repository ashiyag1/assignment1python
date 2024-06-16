#18. Write a python program that checks if two strings are anagrams of each other.

def tocheck(str1, str2):

    if(sorted(str1)== sorted(str2)):
        print("The strings entered are anagrams.") 
    else:
        print("The strings entered are not anagrams.")         

str1=input("Enter string#1:")
str2=input("Enter string#2:")
print(tocheck(str1, str2))
