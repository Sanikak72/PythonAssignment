def add_student(name, roll_number, course):
    student = {
        "name": name,
        "roll_number": roll_number,
        "course": course
    }
    return student

def get_student_info(student):
    return f"Name: {student['name']}, Roll No: {student['roll_number']}, Course: {student['course']}"
