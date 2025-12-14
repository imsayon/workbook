students = [] # List of tuples (roll, marks)

def add(roll, marks):
    students.append((roll, marks))

def update(roll, new_marks):
    for i, (r, m) in enumerate(students):
        if r == roll: students[i] = (r, new_marks); return

def delete(roll):
    global students
    students = [s for s in students if s[0] != roll]

def search(roll):
    for r, m in students:
        if r == roll: print(f"Found: Roll {r}, Marks {m}"); return
    print("Not found")

add(101, 85); add(102, 90)
update(101, 88); search(101)
delete(102); search(102)