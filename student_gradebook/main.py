import json
import os
import time
from auth import login

logged = login()

data_file = "projects/student_gradebook/grades.json"
security_file = "projects/student_gradebook/security.json"
menu = """
📚 Student Gradebook Menu
────────────────────────────
1. ➕ Add New Student
   └─ 🧮 Add Grades
2. 🔍 Check Student Data (By name)
   └─ ✏️  Change Grades
3. 🏆 View Highest Ranked Student
4. ❌ Delete Student
5. 🚪 Exit
"""


class Gradebook:


    def add_student(self):
        subjects = ["English", "Arabic", "Math", "Science", "Social Studies", "Religion"]
        grades = {}
        if os.path.exists(data_file) and os.path.getsize(data_file) > 0:
            with open(data_file, "r") as f:
                students = json.load(f)
        else:
            students = {}
        
        self.student_fname = input("Enter new student first name: ").strip()
        self.student_lname = input("Enter surname: ").strip()
        self.full_name = f"{self.student_fname} {self.student_lname}"

        if self.full_name in students:
            print("Student already in gradebook.")
            return None
        
        for subject in subjects:
            try:
                grade = int(input(f"Enter {subject} grade: ").strip())
                grades[subject] = grade
            except ValueError:
                print("Enter valid grade!")
                return
        print(grades)
        Average_Grade = sum(grades.values()) / len(grades)
        grades["Average Grade"] = float(f"{Average_Grade:.2f}")

        students[self.full_name] = grades
        print("Succesfully added student!")
        with open(data_file, "w") as f:
            json.dump(students, f, indent=4)


    def check_student(self):
        with open(data_file, "r") as f:
            students = json.load(f)
        if os.path.getsize(data_file) == 0:
            print("Gradebook is empty.")
            return

        student_name = input("Enter full name of student: ").strip()
        if student_name in students:
            print("Found Student!")
            time.sleep(0.3)
            # print(json.dumps(students[student_name], indent=4))
            for subject, grade in students[student_name].items():
                print(f"{subject}: {grade}")
            time.sleep(0.3)
            change = input("Change Grades? (y, n): ").strip().lower()
            if change == "y":
                print("VERIFICATION")
                print("")
                verif = input("Enter verification code: ").strip()
                if verif == security_file["verification"]:
                    print("Correct, able to change grades now.")
                    time.sleep(1)
                    for subject, grade in students[student_name].items():
                        print(subject)
                    subject_changing = input("Pick a subject to change: ").strip()
                    if subject_changing in students[student_name]:
                        try:
                            new_grade = int(input("Enter new grade: ").strip())
                        except ValueError:
                            print("Enter Valid grade.")
                        students[student_name][subject_changing] = new_grade
                        total = 0
                        count = 0
                        for subject, grade in students[student_name].items():
                            if subject != "Average Grade":
                                total += grade
                                count += 1
                        average = f"{total / count:.2f}"
                        students[student_name]["Average Grade"] = float(average)
                    else:
                        print("Not a subject (make sure to have correct capitalization).")
                else:
                    print("Incorrect.")
            elif change == "n":
                
                total = 0
                count = 0
                for subject, grade in students[student_name].items():
                    if subject != "Average Grade":
                        total += grade
                        count += 1
                average = f"{total / count:.2f}"
                students[student_name]["Average Grade"] = float(average)
                print("Showing grades again...")
                for subject, grade in students[student_name].items():
                    print(f"{subject}: {grade}")

                time.sleep(5)
                close = input("Close? (y, n): ")
                if close == "y":
                    print("Closing...")
                    time.sleep(0.3)
                    return None
                elif close == "n":
                    print("")
            else:
                print("Invalid option.")
                time.sleep(0.5)
                return None
        else:
            print("Student not in gradebook.")
            return None
        
        with open(data_file, "w") as f:
            json.dump(students, f, indent=4)


def app_functionality():
    gradebook = Gradebook()
    while True:
        print(menu)
        choice = input("Choose (1-5) ")
        if choice == "5":
            print("Exiting...")
            time.sleep(0.3)
            break
        elif choice == "1":
            gradebook.add_student()
            time.sleep(1.5)
        elif choice == "2":
            gradebook.check_student()
            time.sleep(1.5)
        elif choice == "3":
            print("Feature coming soon!")
        elif choice == "4":
            print("Feature coming soon!")

        else:
            print("Invalid choice.")
            time.sleep(1)
            break

if logged:
    app_functionality()