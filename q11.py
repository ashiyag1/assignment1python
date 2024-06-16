#11. Write a python program that generates the first n numbers in the Fibonacci sequence.
#fibonacci seq= 1,1,2,3,5,8....
#basically the sum of preceding two numbers 

a=0
b=1
n=int(input("Enter n upto which you would like to print fibonacci sequence:"))
for i in range(n):
    print(b,end=' ')   
    fibonacci=a+b
    a,b=b,fibonacci
