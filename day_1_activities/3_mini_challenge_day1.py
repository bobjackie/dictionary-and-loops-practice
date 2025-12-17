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
full_name = f"{last_name}, {first_name}"
middle_name = input("Enter middle name, if applicable: ")
homeroom = input("Enter homeroom:")
grade_level = input("Enter Grade level: ")
primary_email = input("Enter main email: ")
secondary_email = input("Enter second email: ")
# this asks the coder to input the students information and then prints it out 
# 2. Combine the First and Last name into this format:
    #    "Last, First" 

print(f"{last_name}, {first_name}") #prints out the students full name in the program 

# 3. Store all of the new information into ONE dictionary
    #    that matches the structure of the existing student data.

new_student = {
    "CPS ID": cps,
    "First Name": first_name,
    "Last Name": last_name,
    "Middle Name": middle_name,
    "Full Name": f"{last_name}, {first_name}",
    "Homeroom": homeroom,
    "Grade Level": grade_level,
    "Primary Email": primary_email,
    "Secondary Email": secondary_email }
  
#This creates a dictonary with all the students information in on the dictonary
# 4. Add (append) that new dictionary into the main students list.

student_data2.students.append(new_student) #this adds the new stundet to the list of students 
# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record
print("your student was added ") #after student is added it prints out this message 

print(f"\nStudent {full_name} was added!")
print(f"number of stuents: {len(student_data2.students)}")
# 6. The program must NOT delete or overwrite any existing students.

for student in student_data2.students:
    if student["CPS ID"] == ["CPS ID"]:
        print("Error: CPS ID already exists.")
        break


# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken


        
    


