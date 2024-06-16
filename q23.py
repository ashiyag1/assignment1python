#23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
print("If your input choice is fahrenheit then it will be converted to celcius and vice versa")
user_input=input("Enter celcius or fahrenheit: ")
if (user_input=="celcius"or user_input=="Celcius"):
    temp=int(input("Enter temperature in celcius"))
    fahrenheit=(temp*1.8)+32
    print("temperature in fahrenheit:",fahrenheit)
elif(user_input=="fahrenheit"or user_input=="Fahrenheit"):
    temp1=int(input("Enter temperature in fahrenheit"))
    celcius=(temp1-32)*(5/9)
    print("temperature in celcius:",celcius)



