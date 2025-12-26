from student import add_student, get_student_info
from marks import add_marks, calculate_total_marks
from attendance import mark_attendance, get_attendance
from fees import add_fee, check_fee_status
from report import Report
import utils

student1 = add_student("John Doe", "A123", "Computer Science")
print(get_student_info(student1))

add_marks(student1, [90, 85, 78, 92])
print(f"Total Marks: {calculate_total_marks(student1)}")

mark_attendance(student1, 18, 20)
print(f"Attendance: {get_attendance(student1)}%")

add_fee(student1, 500)
print(f"Fee Status: {'Paid' if check_fee_status(student1) == 0 else 'Pending'}")

report = Report(student1)
print(report.generate_report())

print(f"Current Date and Time: {utils.get_current_date()}")

print(f"Generated Random ID: {utils.generate_random_id()}")

utils.print_math_properties()
