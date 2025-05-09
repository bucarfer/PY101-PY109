# Original program to debug
# def process_student(student_data):
#     name = student_data.get('name')
#     grade = student_data.get('grade')
#     return (name, grade)

# def average_grade(grades):
#     total = sum(grades)
#     average = total / len(grades)
#     return average

# students = [
#     {'name': 'Alice', 'grade': 85},
#     {'name': 'Bob'}, {'name': 'Jack', 'grade': 72},
#     {'name': 'Jane', 'grade': 75},
# ]

# def collect_grades(students):
#     grades = []
#     for student in students:
#         name, grade = process_student(student)
#         grades.append(grade)
#     return grades

# grades = collect_grades(students)
# print(average_grade(grades))
# TypeError: unsupported operand type(s) for +: 'int'
# and 'NoneType'

# # TypeError: unsupported operand type(s) for +: 'int'
# and 'NoneType'

# Debugged solution

def process_student(student_data):
    name = student_data.get('name')
    grade = student_data.get('grade')
    return (name, grade)

def average_grade(grades):
    print (grades)
    total = sum(grades) # original error adding integers and NoneType
    average = total / len(grades)
    return average

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob'},
    {'name': 'Jack', 'grade': 72},
    {'name': 'Jane', 'grade': 75},
]

def collect_grades(students):
    grades = []
    for student in students:
        name, grade = process_student(student)
        if grade: # LS solution to only append grades with a Truthy value
            grades.append(grade)
    return grades

# my solution for line 57 to include value 0. BETTER SOLUTION
#       if grade is None:
#           continue
#       grades.append(grade)

# or
#       if grade =! None:
#           grades.append(grade)

grades = collect_grades(students)
print(average_grade(grades))

## Debugging Steps
# 1. Reproduce the ErrorEnsure the bug occurs consistently. Reproducibility is key to diagnosis.
# 2. Determine the BoundariesIsolate where the problem occurs. Change inputs or code to narrow it down. Use error messages (like TypeError) to get clues.
# 3. Trace the CodeRead through the code path. Use simplified test cases to find exactly when and where things break. Use print statements to inspect values.
# 4. Understand the Problem WellAnalyze the data and logic at the point of failure. Look for issues like unexpected types (None, wrong input, etc.).
# 5. Implement a FixFix only one thing at a time. Choose the most logical place in the code to apply the fix (ideally, close to the source of the problem).
# 6. Test the FixRe-run the program with the same inputs to confirm the bug is gone. Test other inputs to make sure nothing else broke.'''
