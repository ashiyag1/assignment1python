#19. Write a python program that removes all punctuation from a given string.

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str1 = input("Enter a string: ")
withoutpunct = ""
for ch in str1:
    if ch not in punctuations:
        withoutpunct = withoutpunct + ch

print(withoutpunct)
