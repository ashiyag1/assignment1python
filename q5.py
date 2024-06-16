#5. Write a program that takes a string input from the user and writes it to a text File
str1=input("Type in whatever you want to print:")
samplefile=open('C:/Users/amit_/OneDrive/Desktop/pythonmlinternship/pythontxt.txt','w')
print(str1,sep=" ",end=".",file=samplefile)