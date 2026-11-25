n = int(input("Enter number of students: "))

class_total = 0

for i in range(1, n + 1):
    total = 0

    print("Student", i)

    for j in range(1, 6):
        marks = float(input("Enter test marks: "))
        total += marks

    average = total / 5

    print("Student Average:", average)

    class_total += average

class_average = class_total / n

print("Overall Class Average:", class_average)