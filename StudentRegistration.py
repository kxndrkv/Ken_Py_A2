#   StudentRegistration.py 
#  This program processes student details to register them into courses and then
#  displays this information onto the screen. 
#  Author: Rachakhet Kwathai | Ken
#  Date: 3/06/2024

import tkinter as tk
import unittest
from tkinter import *
from tkinter import messagebox

# Function to print the column headings
def printHeadings():
    global root

    # Creating labels for headings
    label_heading = tk.Label(root, text="---Holmesglen Institute---")
    label_ID = tk.Label(root, text="ID")
    label_Name = tk.Label(root, text="Name")
    label_Course = tk.Label(root, text="Course")
    label_Fee = tk.Label(root, text="Fee")

    # Placing the labels using grid layout
    label_heading.grid(row=0, column=0, columnspan=6)
    label_ID.grid(row=1, column=0)
    label_Name.grid(row=1, column=1)
    label_Course.grid(row=1, column=2)
    label_Fee.grid(row=1, column=3)


# Function to create input fields for student details
def inputStudentDetails():
    global root, students, entry_ID, entry_Name, entry_Course, entry_Fee

    # Creating entry widgets for student details
    entry_ID = tk.Entry(root)
    entry_Name = tk.Entry(root)
    entry_Course = tk.Entry(root)
    entry_Fee = tk.Entry(root)

    # Placing the entry widgets using grid layout
    entry_ID.grid(row=2, column=0)
    entry_Name.grid(row=2, column=1)
    entry_Course.grid(row=2, column=2)
    entry_Fee.grid(row=2, column=3)

    # Function to handle the submit button click event
    def submit_button():
        # Collecting data from entry widgets
        student_data = {
            "id": entry_ID.get(),
            "name": entry_Name.get(),
            "course": entry_Course.get(),
            "fee": entry_Fee.get()
        }

        # Adding the collected data to the students list
        students.append(student_data)

        # Display the updated data
        display_data()

        # Clearing the entry widgets for new input
        entry_ID.delete(0, tk.END)
        entry_Name.delete(0, tk.END)
        entry_Course.delete(0, tk.END)
        entry_Fee.delete(0, tk.END)

    # Creating and placing the submit button using grid layout
    submit_button = tk.Button(root, text="Submit", command=submit_button)
    submit_button.grid(row=2, column=4)
    
    # Creating and placing the display button using grid layout
    display_button = tk.Button(root, text="Display", command=outputTotalFee)
    display_button.grid(row=2, column=5)

# Function to display student data in the main window
def display_data():
    # Clearing the previous data in the data frame
    for widget in data_frame.winfo_children():
        widget.destroy()

    # Displaying each student's data in the data frame
    for student in students:
        data_label = Label(data_frame, text=f"{student['id']} | {student['name']} | {student['course']} | {student['fee']}")
        data_label.pack()

# Function to display student data and total fee in a new window
def outputTotalFee():
    # Creating a new window
    new_window = tk.Toplevel(root)
    new_window.title("Student Information")

    # Displaying each student's data in the new window
    for i, student in enumerate(students, start=1):
        data_label = Label(new_window, text=f"Student {i}: {student['id']} | {student['name']} | {student['course']} | {student['fee']}")
        data_label.pack()

    # Calculating and displaying the total fee in the new window
    total_fee = sum(float(student['fee']) for student in students)
    total_fee_label = Label(new_window, text=f"Total Fee: {total_fee}")
    total_fee_label.pack()







# Main application setup
root = tk.Tk()
root.title("Student Registration")

# List to store student data
students = []

# Creating a frame to display student data
data_frame = tk.Frame(root)
data_frame.grid(row=3, column=0, columnspan=4)

# Calling functions to print headings and input fields
printHeadings()
inputStudentDetails()

# Running the main event loop
root.mainloop()

if __name__ == "__main__":
    unittest.main()

