totalmark = int(input("enter the total mark: "))
student = {
    "name": "anzil",
    "roll_number": "43",
    "register_number": "234123",
    "department": "Computer Science",
    "semester": 5
}


student["total_mark"] = totalmark


mark = student["total_mark"]

if mark >= 90:
    grade = 'A'
elif mark >= 82:
    grade = 'B'
elif mark >= 75:
    grade = 'C'
elif mark >= 60:
    grade = 'D'
elif mark >= 50:
    grade = 'P'
else:
    grade = 'F'

student["grade"] = grade


del student["roll_number"]


print(student)
