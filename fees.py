def add_fee(student, fee_amount):
    student['fee'] = fee_amount

def check_fee_status(student):
    return student.get('fee', 0)
