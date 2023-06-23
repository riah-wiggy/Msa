data_file = open("students.csv", "r")

#creat an empty dictionary
student = {}

#loop through data in the file
for line_of_data in data_file:
    key_values = line_of_data.split(", ")

#close file
data_file.close()

for student, info in student.items():
    print()