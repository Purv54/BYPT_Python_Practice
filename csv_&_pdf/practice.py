import csv

data = open("Greenhouse.csv")

csv_data = csv.reader(data)

data_lines = list(csv_data)
print(len(data_lines))
total = []
for line in data_lines[1:]:
    
    total.append(line[5])

print(total)

file_to_output = open("output.csv", "w", newline="")

csv_writer = csv.writer(file_to_output,delimiter=',')

csv_writer.writerow(['Name', 'Age', 'City'])

csv_writer.writerow([[ '1' , '2' , '3'] , ['4' , '5' , '6'] , ['7' , '8' , '9']])

file_to_output.close()
