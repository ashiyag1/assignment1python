#15. Write a program that reads data from a CSV file and prints it to the console
import csv
with open('C:/Users/amit_/OneDrive/Desktop/pythonmlinternship/temperature.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
        
