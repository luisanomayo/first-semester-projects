students = []

def add_student():
    """
    TODO: Prompt the user to enter student name, age, and grade.
    Append the student as a dictionary to the students list.
    """
    #collect user inputs of student info
    student_name = input("Enter student name: ").capitalize()
    
    #handle invalid inputs for age & grade
    try:
        student_age = int(input("Enter student age: "))
    except ValueError:
        print("Invalid input for age. Please enter a number.")
        return
    try:
        student_grade = float(input("Enter student grade: "))
    except ValueError:
        print("Invalid input for grade. Please enter a number.")
        return
    
     
    #pass to dictionary
    student = {
        "name": student_name.capitalize(),
        "age": int(student_age),
        "grade": int(student_grade)
    }
    
    #append to students list
    students.append(student)
    print("Student added successfully!")

    

def view_students():
    """
    TODO: Loop through the students list and print each student's info.
    """
    if students:
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    else:
        print("student list is empty")



def get_average_grade():
    """
    TODO: Return the average grade of all students.
    """
    if students:
        for student in students:
            if student:
                total_grade = sum(student['grade'] for student in students)
                average_grade = total_grade / len(students)
                return average_grade
    else:
        print("student list is empty")
        return 0