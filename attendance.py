def mark_attendance(student, present_days, total_days):
    attendance_percentage = (present_days / total_days) * 100
    student['attendance'] = attendance_percentage

def get_attendance(student):
    return student.get('attendance', 0)
