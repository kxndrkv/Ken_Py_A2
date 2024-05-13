def inputStudentDetails():
    """
    Obtain information about each student including their ID, name, 
    the course in which they are enrolled, as well as their course fee.
    """
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    course = input("Enter course name: ")
    course_fee = float(input("Enter course fee: "))

    # Return a dictionary to store the student details
    return {
        "id": student_id,
        "name": student_n12ame,
        "course": course,
        "fee": course_fee
    }
    
    
def main():
    total_fees = 0

    while True:
        student_details, course_fee = inputStudentDetails()

        # Display the student details
        print("\nStudent Details:")
        print(f"ID: {student_details['id']}")
        print(f"Name: {student_details['name']}")
        print(f"Course: {student_details['course']}")
        print(f"Fee: ${course_fee:.2f}")

        # Add the course fee to the total fees
        total_fees += course_fee

        # Ask the user if they want to enter another student's details
        response = input("\nDo you want to enter another student's details? (yes/no): ")
        if response.lower() != "yes":
            break

    # Display the total fees
    print(f"\nTotal Fees: ${total_fees:.2f}")

if __name__ == "__main__":
    main()