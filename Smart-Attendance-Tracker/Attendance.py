"""
Student Attendance Tracker CLI
Python Version: 3.14.7
"""

def display(j, subject, total, present):
    percentage = (present[j] / total[j]) * 100 if total[j] > 0 else 0
    
    if percentage >= 90:
        status = "Excellent - Keep Going"
    elif percentage >= 80:
        status = "Good - Try to Improve"
    elif percentage >= 75:
        status = "Satisfactory - Improvement Needed"
    else:
        status = "Critical - Attend Classes Strictly"
        
    print(f"{subject[j]}: {percentage:.2f}%  | Status: {status}")


def main():
    try:
        n = int(input("Enter the Number of students: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    student = []
    reg = []
    sub_num = []
    subject = []
    total = []
    present = []
    t = 0

    for i in range(n):
        print(f"\n--- Entry for Student {i+1} ---")
        student.append(input(f"Enter Name of Student {i+1}: "))
        reg.append(input(f"Enter Registration Number of Student {i+1}: "))
        
        x = int(input("Enter the Number of Subjects: "))
        sub_num.append(x)
        
        for j in range(t, x + t):
            sub_name = input(f"Enter Name of Subject {j+1}: ")
            subject.append(sub_name)
            
            p = int(input(f"Enter Total Working Days in {sub_name}: "))
            total.append(p)
            
            while True:
                q = int(input(f"Enter Days Present in {sub_name}: "))
                if 0 <= q <= p:
                    present.append(q)
                    break
                print(f"Invalid! Days present must be between 0 and {p}.")
        t += x

    print("\n\n" + "="*35)
    print("      ATTENDANCE REPORT      ")
    print("="*35)

    while True:
        print("\nMenu:")
        print("1. View Attendance Report Of All Students")
        print("2. View Attendance Report Of Specific Student")
        print("3. Exit")
        
        try:
            choice = int(input("Enter choice (1-3): "))
        except ValueError:
            print("Invalid option. Please enter a number.")
            continue

        if choice == 1:
            t = 0
            for i in range(n):
                print(f"\nName: {student[i]}")
                print(f"Registration No.: {reg[i]}")
                for j in range(t, sub_num[i] + t):
                    display(j, subject, total, present)
                t += sub_num[i]

        elif choice == 2:
            target_reg = input("\nEnter Student Registration Number: ")
            found_index = -1
            
            for i in range(n):
                if reg[i] == target_reg:
                    found_index = i
                    break
            
            if found_index == -1:
                print("Registration Number Not Found.")
            else:
                t = sum(sub_num[:found_index])
                print(f"\nName: {student[found_index]}")
                print(f"Registration No.: {reg[found_index]}")
                for j in range(t, sub_num[found_index] + t):
                    display(j, subject, total, present)

        elif choice == 3:
            print("Exiting Attendance Tracker. Goodbye!")
            break
        else:
            print("Enter a valid choice (1-3).")


if __name__ == "__main__":
    main()
