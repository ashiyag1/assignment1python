#24. Write a program that acts as a simple calculator. It should take two numbers and an 
# operator (+, -, *, /) as input and print the result.
print("Note:To get positive output a should be greater than b")
a=int(input("Enter a number#1:"))
b=int(input("Enter a number#2:"))
operator=input("Enter an operator:+,-,x,%:")
if (operator=="+"):
    sum=a+b
    print("Your answer is:",sum)
if (operator=="-"):
    sub=a-b
    print("Your answer is:",sub)
if(operator=="x"): 
    mult=a*b
    print("Your answer is:",mult)
if(operator=="%"):
    div=a/b
    print("Your answer is:",div)
    







