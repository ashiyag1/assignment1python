#3. Write a python program that calculates the factorial of a given number.
print("Enter the number whose factorial you want to calculate:")
f=int(input())
fact=1 #n*n-1*n-2*....*n-(n-1)
for i in range(f-1):
    factorial=fact*(f-i)
    fact=factorial
print("Your factorial is:",factorial)  