import csv
from Models.Task import Task

def read(input_file):
    with open(input_file, newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
        return Task(data)