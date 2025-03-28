def calculate_average(line):
    try:
        parts = line.strip().split(":")
        if len(parts) != 2:
            raise ValueError("Line format is incorrect")
        student_name, grades = parts
        grades = list(map(int, grades.split(",")))
        if len(grades) != 3:
            raise ValueError("Incorrect number of grades")
    except ValueError as e:
        return f"Invalid data for {line.strip()} ({e})"

    average = sum(grades) / len(grades)
    if 90 <= average <= 100:
        letter = "AA"
    elif 80 <= average < 90:
        letter = "BA"
    elif 70 <= average < 80:
        letter = "BB"
    elif 60 <= average < 70:
        letter = "CB"
    elif 50 <= average < 60:
        letter = "CC"
    elif 40 <= average < 50:
        letter = "DC"
    elif 30 <= average < 40:
        letter = "DD"
    elif 20 <= average < 30:
        letter = "FD"
    else:
        letter = "FF"

    return f"{student_name} : {grades[0]} , {grades[1]} , {grades[2]} : {average:.2f} : {letter}"

def input_grades():
    name = input("Enter Student Name: ")
    surname = input("Enter Student Surname: ")
    try:
        grades = [int(input(f"Enter Grade {i+1}: ")) for i in range(3)]
    except ValueError:
        print("Invalid grade input. Please enter integers only.")
        return
    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(f"{name} {surname} : {','.join(map(str, grades))}\n")

def read_grades():
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No grades found. Please add grades first.")

def save_grades():
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            lines = [calculate_average(line) for line in file]
        with open("results.txt", "w", encoding="utf-8") as file:
            file.writelines(line + "\n" for line in lines)
        print("Grades saved to results.txt.")
    except FileNotFoundError:
        print("No grades found. Please add grades first.")

while True:
    choice = input("1 - Enter Grade\n2 - Read Grades\n3 - Save Grades\n4 - Exit\nYour choice:\n")
    if choice == "1":
        input_grades()
    elif choice == "2":
        read_grades()
    elif choice == "3":
        save_grades()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
def main_menu():
    while True:
        choice = input("1 - Enter Grade\n2 - Read Grades\n3 - Save Grades\n4 - Exit\nYour choice:\n")
        if choice == "1":
            input_grades()
        elif choice == "2":
            read_grades()
        elif choice == "3":
            save_grades()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
