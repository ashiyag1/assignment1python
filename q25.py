#25. Write a program that copies the contents of one text file to another.
file_1=open("file1.txt","r")
file_2=open("file2.txt","r")
for i in file_1:
    file_2.write(i)

