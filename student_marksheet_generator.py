def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 40:
        return 'D'
    else:
        return 'F'

name = input("Enter student name: ")
subjects = ["Math", "Physics", "Chemistry", "English", "Computer"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter marks for {subject}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(subjects)
grade = calculate_grade(average)

report = f"""STUDENT MARKSHEET
--------------------
Name    : {name}
Subjects: {', '.join(subjects)}
Marks   : {', '.join(str(m) for m in marks)}
Total   : {total}
Average : {average:.2f}
Grade   : {grade}
"""

print("\n" + report)

with open("marksheet.txt", "w") as file:
    file.write(report)