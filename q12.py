#12. Write a python program that calculates the sum of the digits of a given number
n=int(input("Enter the number whose sum of digits you want to calculate:"))
num=n
sum=0
while n!=0:
    sum=sum+n%10
    n//=10
print("The sum of digits of",num,"is",sum)
