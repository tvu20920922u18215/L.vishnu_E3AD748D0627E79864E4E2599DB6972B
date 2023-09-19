''' Implement a function called sort_students that takes a list of student objects as input and 
sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. 
Each student object has the following attributes: name (string), roll_number (string), and cgpa 
(float). Test the function with different input lists of students.'''


def sort_students(student_list):
    # Use the sorted() function with a custom key to sort by CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student["cgpa"], reverse=True)
    return sorted_students

# Define a list of student objects
students1 = [
    {"name": "Alice", "roll_number": "101", "cgpa": 3.9},
    {"name": "Bob", "roll_number": "102", "cgpa": 3.7},
    {"name": "Charlie", "roll_number": "103", "cgpa": 3.8},
]

students2 = [
    {"name": "Eve", "roll_number": "104", "cgpa": 3.5},
    {"name": "Frank", "roll_number": "105", "cgpa": 3.9},
    {"name": "Grace", "roll_number": "106", "cgpa": 3.6},
]

# Sort and print the first set of students
sorted_students1 = sort_students(students1)
print("Sorted Students 1:")
for student in sorted_students1:
    print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, CGPA: {student['cgpa']}")

# Sort and print the second set of students
sorted_students2 = sort_students(students2)
print("\nSorted Students 2:")
for student in sorted_students2:
    print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, CGPA: {student['cgpa']}")
