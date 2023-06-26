import Student
from datetime import datetime
#create 2 students

#student1 = Student.Student("Jess", "Hanes", "Math", 30 ,3.0, "1234")
#student2 = Student.Student("Harry", "Miller", "Ela", 98, 4.0, "23456")\
"""
function to write to error log file
input:error message
output: none
"""

def write_to_error_log(message):
    try:
        #open log file
        log_file = open("error_log.txt", "w")
        #write error message to log file
        log_file.write(f"{datetime.now()}: {message}\n")
        #close log file
        # log_file.close()err:
        log_file.close()
    except Exception as err:
        print(err)
        return
    return

"""
function to return list of student objects
input: none
output: list of student objects
"""
def load_students():
    students = []
    try:
        #open file
        data_file = open("students.csv", "r")
        #read the file line by line. create student  with each line of data
        line = 0
        for line_of_data in data_file:
            if line == 0:
                line += 1
                continue
            line += 1
                #split the line by the comma
            student_data = line_of_data.split(",")
            #handle errors in data format. line_of_data shouldhave 6 items
            #if error in format then write a messsage to a log file
            try:
                if len(student_data) != 6:
                    raise Exception(f"There is an error in your data file on line {line}")
            except Exception as err:
                write_to_error_log(str(err))
                continue
       
                #create a student with the split data
            new_student = Student.Student(student_data[0], student_data[1], student_data[2], int(student_data[3]), float(student_data[4]), student_data[5].strip())
                    #append student to student list
            students.append(new_student)
    except Exception as err:
        print(err, "See log file for details")
        
    return students
"""
Function to convert student object to student dictionaries
input: list of student objeccts
output: list of student dictionaries
"""
def student_to_dictionary(students):
    #create a list to store the dictionaries-[]= an empty dictionary
    student_dictionary_list = []
    #llop through student list amd write each student's data to a dictionary
    for student in students:
        student_dictionary = {}
        #set keys and values for first name, last name, id, major, gpa, class level
        student_dictionary['id'] = student.get_ID()
        student_dictionary['First_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class level'] = student.get_class_level()
        #apppend to student dictionary list
        student_dictionary_list.append(student_dictionary)
    return student_dictionary_list 

"""
function to get student dictionaries
input: none
output: list of student dictionaries
"""
def get_student_dictionaries():
    #get a list of students
    student_list = load_students()
    #get list of student dictionaries
    student_dictionaries = student_to_dictionary(student_list)
    return student_dictionaries




 #.strip gets rid of any extra piecesw in your printed data like \n
 #students.append(student1) students.append(student2)
#if there is an error iut will dshow in error_log.txt
    #for student in students:
        #student.print_data()