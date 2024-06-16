#26. Write a program in python that checks if a string starts with a given prefix or 
# ends with a given suffix.
str1=input("Enter a string:")
fix=input("Enter Prefix or Suffix:")
if (fix=="Prefix"or fix=="prefix"):
    prefix=input("enter a prefix:")
    gap=" "
    str2=prefix + gap+ str1
    print("your required answer:",str2)
elif (fix=="Suffix"or fix=="suffix"):
    suffix=input("Enter a suffix:")
    gap=" "
    str3= str1+gap+suffix
    print("your required answer:",str3)





