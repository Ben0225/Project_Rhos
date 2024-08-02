import csv

def count_lines(filename):
    count = 0
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            count += 1
    return count


count_lines(r"C:\Users\DELL\Downloads\data\-")

