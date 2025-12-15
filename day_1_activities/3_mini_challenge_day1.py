# Project Prompt:

# You are hired to build a Student Lookup Tool for a school front office. The secretary must be able to:

    # Enter a student’s full name

    # Instantly see:

            # CPS ID

            # Homeroom

            # Grade Level

            # Primary Email

            # Students must:

            # Describe the search process

## be able to add new data
# Your program must allow the secretary to ADD a brand new student
# into the system while the program is running.

# Your job is to let the secretary type in a new student just like filling out a registration form.
# Once the form is complete, your program must turn that information into a dictionary and add it to the main list of students.
# If the student already exists (same CPS ID), your program must block the entry to prevent duplicates.

# The program should:
    # 1. Ask the user for the following information:
    #    - CPS ID
    #    - First Name
    #    - Last Name
    #    - Middle Name
    #    - Homeroom
    #    - Grade Level
    #    - Primary Email
    #    - Secondary Email
import student_data2
cps = input("Enter CPS ID: ")
first_name = input("Enter First name: ")
last_name = input("Enter Last name: ")
middle_name = input("Enter Middle name: ")
homeroom = input("Enter homeroom:")
grade_level = input("Enter Grade level: ")
primary_email = input("Enter Primary email: ")
secondary_email = input("Enter Secondary email: ")


# 2. Combine the First and Last name into this format:
    #    "Last, First" 

print(f"{last_name}, {first_name}")

# 3. Store all of the new information into ONE dictionary
    #    that matches the structure of the existing student data.

for student in student_data2.students:
    if student["CPSID"] == int(cps):
        print("Error: CPS ID already taken. Student not added.")
        break
else:
    new_student = {
        "CPSID": int(cps),
        "Combo,Name": f"{last_name}, {first_name}",
        "LName": last_name,
        "FName": first_name,
        "MName": middle_name,
        "HR": homeroom,
        "GL": int(grade_level),
        "Email": [primary_email, secondary_email]
    }
    student_data2.students.append(new_student)
    print("Student added successfully!")
    print(f"Total number of students: {len(student_data2.students)}")
    print("Newly added student record:")
    print(new_student)

# 4. Add (append) that new dictionary into the main students list.

# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record

# 6. The program must NOT delete or overwrite any existing students.

# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken



