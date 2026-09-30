"""
Student Attendance Tracker CLI
Python 3.14.7
"""
def ask_int(msg, lo=None, hi=None):
    while True:
        try:
            v = int(input(msg).strip())
        except ValueError:
            print("Please enter a whole number.")
            continue
        if lo is not None and v < lo:
            print(f"Value must be at least {lo}.")
        elif hi is not None and v > hi:
            print(f"Value must be at most {hi}.")
        else:
            return v

def ask_text(msg):
    while True:
        s = input(msg).strip()
        if s:
            return s
        print("This field cannot be empty.")

def get_status(pct):
    if pct >= 90:
        return "Excellent - Keep Going"
    if pct >= 80:
        return "Good - Try to Improve"
    if pct >= 75:
        return "Satisfactory - Improvement Needed"
    return "Critical - Attend Classes Strictly"

def show(st):
    print(f"\nName: {st['name']}")
    print(f"Registration No.: {st['reg']}")
    for sub, tot, pre in st["subs"]:
        pct = (pre / tot) * 100
        print(f"{sub}: {pct:.2f}%  | Status: {get_status(pct)}")

def add_student(i, done):
    print(f"\n--- Entry for Student {i} ---")
    name = ask_text(f"Enter Name of Student {i}: ")

    while True:
        reg = ask_text(f"Enter Registration Number of Student {i}: ")
        if reg.lower() in done:
            print("This registration number already exists. Try again.")
        else:
            break

    k = ask_int("Enter the Number of Subjects: ", lo=1)
    subs = []
    for j in range(1, k + 1):
        sub = ask_text(f"Enter Name of Subject {j}: ")
        tot = ask_int(f"Enter Total Working Days in {sub}: ", lo=1)
        pre = ask_int(f"Enter Days Present in {sub}: ", lo=0, hi=tot)
        subs.append((sub, tot, pre))

    return {"name": name, "reg": reg, "subs": subs}

def main():
    n = ask_int("Enter the Number of students: ", lo=1)

    students = []
    done = set()
    for i in range(1, n + 1):
        st = add_student(i, done)
        students.append(st)
        done.add(st["reg"].lower())

    print("\n\n" + "=" * 35)
    print("      ATTENDANCE REPORT      ")
    print("=" * 35)

    while True:
        print("\nMenu:")
        print("1. View Attendance Report Of All Students")
        print("2. View Attendance Report Of Specific Student")
        print("3. Exit")

        c = ask_int("Enter choice (1-3): ")

        if c == 1:
            for st in students:
                show(st)
        elif c == 2:
            r = input("\nEnter Student Registration Number: ").strip().lower()
            found = next((s for s in students if s["reg"].lower() == r), None)
            if found:
                show(found)
            else:
                print("Registration Number Not Found.")
        elif c == 3:
            print("Exiting Attendance Tracker. Goodbye!")
            break
        else:
            print("Enter a valid choice (1-3).")
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram stopped. Goodbye!")
