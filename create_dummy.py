from mimesis import Person
import csv

nr_of_rows = 100000
nr_of_columns = 100

randomGenerator = Person()

with open('dummy.csv', 'w') as csv_file:
    file_writer = csv.writer(csv_file, delimiter=',',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    lines = []
    for row in range(nr_of_rows):
        line = []
        for column in range(nr_of_columns):
            line.append(randomGenerator.name())
        lines.append(line)
    file_writer.writerows(lines)