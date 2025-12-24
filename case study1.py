students = {
    "Arya": [85, 90, 88],
    "Shruti": [92, 95, 94],
    "Raj": [70, 89, 65],
    "Riya": [45, 50, 48],
    "Sita": [60, 65, 62]
}


def cal_Avg(marks):
    return sum(marks) / len(marks)


def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "FAIL"


top = ""
highAverage = 0
print("----student details----")
for name, marks in students.items():
    avg = cal_Avg(marks)
    grade = assign_grade(avg)
    print(f"Name: {name}, marks: {marks}, grade: {grade}")
    if avg > highAverage:
        highAverage = avg
        top = name
print("\nTOP SCORER")
print(f"Name: {top}, Average: {highAverage}")


