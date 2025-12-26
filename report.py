from marks import calculate_grade, calculate_total_marks
from attendance import get_attendance
from fees import check_fee_status

class Report:
    def __init__(self, student):
        self.student = student

    def generate_report(self):
        total_marks = calculate_total_marks(self.student)
        grade = calculate_grade(self.student)
        attendance = get_attendance(self.student)
        fee_status = check_fee_status(self.student)

        report = (
            f"Student Report:\n"
            f"Name: {self.student['name']}\n"
            f"Roll No: {self.student['roll_number']}\n"
            f"Course: {self.student['course']}\n"
            f"Total Marks: {total_marks}\n"
            f"Grade: {grade}\n"
            f"Attendance: {attendance}%\n"
            f"Fee Status: {'Paid' if fee_status == 0 else 'Pending'}"
        )
        return report
