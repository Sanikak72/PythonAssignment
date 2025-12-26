def add_marks(student, marks):
    student['marks'] = marks

def calculate_total_marks(student):
    return sum(student.get('marks', []))

def calculate_grade(student):
    total_marks = calculate_total_marks(student)
    if total_marks >= 90:
        return "A"
    elif total_marks >= 70:
        return "B"
    elif total_marks >= 50:
        return "C"
    else:
        return "F"
