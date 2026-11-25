assignments = ["Python", "DBMS", "Maths"]

print("Assignments:", assignments)

new_assignment = input("Enter new assignment: ")
assignments.append(new_assignment)

print("Updated List:", assignments)

completed = input("Enter completed assignment: ")

if completed in assignments:
    assignments.remove(completed)
    print("Assignment removed")
else:
    print("Assignment not found")

print("Final Assignment List:")

for item in assignments:
    print(item)