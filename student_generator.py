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


def main():
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
        
        
    #.strip gets rid of any extra piecesw in your printed data like \n

    for the_student in students:
        the_student.print_data()

    #students.append(student1) students.append(student2)
#if there is an error iut will dshow in error_log.txt
    #for student in students:
        #student.print_data()
main()