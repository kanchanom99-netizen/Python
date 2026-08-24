# Program to manage assignments using a list

assignments = ["Python", "DBMS", "DSA"]

print("Assignments:", assignments)

new_assignment = input("Enter a new assignment: ")
assignments.append(new_assignment)

completed = input("Enter completed assignment: ")

if completed in assignments:
    assignments.remove(completed)
else:
    print("Assignment not found")

print("Updated assignments:", assignments)
