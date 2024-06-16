#14. Write a program that reads multiple lines of input from the user until they enter an empty line,
# then prints all the lines.
multilineinput = []
while True:
    lineinput= input("Kindly enter a line and if you want to exit just press enter: ")
    if not lineinput:
        break
    multilineinput.append(lineinput)

for everyline in multilineinput:
    print(everyline)

