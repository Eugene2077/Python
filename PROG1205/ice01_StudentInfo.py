# Name : Hongju (Eugene) Shin
# Date : 15 Sep 2021
# App Name : student information
# App Description: Program that asks and display student information

from os import system

# Set the console title
system("title student information - Hongju(Eugene) Shin")

# Input Screen

# Ask for user's name
student_name = input("Enter your name: ")

# Ask for the course name
course_name = input("Enter your course name: ")

# Ask for the course duration
course_duration = input("Enter your course duration in semesters: ")

# Ask for the current semester
current_semester = input("Enter your current semester: ")

# Convert from string into an interger (whole number)
course_duration = int(course_duration)
current_semester = int(current_semester)

# Calculate how many semesters are left to complete the course
# Stores the result of the calculation in a variable
semesters_to_graduate = course_duration - current_semester

# Clear the console screem
system("cls || clear")

# Output screen

# Dispaly (print) the information to the user
print("Name: " + student_name)
print("Course Name: " + course_name)
print(f"Course Duration: {course_duration}")           # using formatter
print("Current Semeater: " + str(current_semester))    # using casting
print(f"Semester to completion: {semesters_to_graduate} semesters")

# Exit prompt
input("Press ENTER to exit: ")
