class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

def input_number_of_students():
    num_students = int(input("Enter the number of students in the class: "))
    return num_students

def input_student_information():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth: ")
    return Student(student_id, name, dob)

def input_number_of_courses():
    num_courses = int(input("Enter the number of courses: "))
    return num_courses

def input_course_information():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return Course(course_id, name)

def input_marks_for_course(students, course):
    print(f"Input marks for students in the course {course.name}:")
    marks = {}
    for student in students:
        mark = float(input(f"Enter mark for {student.name}: "))
        marks[student] = mark
    return marks


