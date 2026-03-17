Students =[]
ai_tools = ["Grok"]
def add_student():
    name = input("Name: ")
    student_id = input("student ID: ")
    [print(f"{i+1}.{t}")for i,t in enumerate(ai_tools)]
    tool = ai_tools[int(input("pick AI tool (number): "))-1]
    Students.append({"name": name, "student_id": student_id, "fav_ai_tool": tool })
    print(f"{name} added!\n")
def show_students():
    print(f"\n{len(Students)} student(s):")
    for i, s in enumerate(students, 1):
        print(f"{i}. {s['name']}\nID: {s['student_id']}\nAI Tool: {s['fav_ai_tool']}\n\n")
def save_to_file():
    with open("students.txt", "w") as f:
        for i, s in enumerate(students, 1):
            f.write(f"student #{i} \nName:{s['name']}\nID: {s['student_id']}\nAI Tool: {s['fav_ai_tool']}\n\n")
    print("saved to students.txt")
print("=== student info system ===")
while True:
    choice = input("\n1. Add 2. view 3. save 4. Exit|nchoose: ")
    if  choice == "1": add_student()
    elif choice == "2": show_students()
    elif choice == "3": save_to_file() if students else print("No students yet.")
    elif choice == "4": print("Bye!"); break 