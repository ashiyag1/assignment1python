#16. Write a program in python that counts the frequency of each character in a string
stringtobechecked=input("enter a string whose character's frequency you want to check:" )
frequency = {}
for ch in stringtobechecked:
    if ch in frequency:
        frequency[ch]= frequency[ch] + 1
    else:
        frequency[ch] = 1
print("Character frequencies:", frequency)

