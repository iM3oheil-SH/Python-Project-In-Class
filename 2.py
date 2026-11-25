Events = [
    ("Borrow", "S01", "Python", 1),
    ("Borrow", "S01", "Python", 2),
    ("Return", "S01", "Python", 1),
    ("Borrow", "S02", "Python", 1),
    ("Return", "S03", "Python", 2),
    ("Borrow", "S01", "Python", 1)
]

Current = {}
Students = {}
Rejected = []

for Event in Events:
    Action, Student, Title, Copy = Event
    
    Key = (Title, Copy)
    
    if Action == "Borrow":
        if Key not in Current:
            Current[Key] = Student
            if Title not in Students:
                Students[Title] = set()
            Students[Title].add(Student)
        else:
            Rejected.append(Event)
    elif Action == "Return":
        if Key in Current and Current[Key] == Student:
            del Current[Key]
        else:
            Rejected.append(Event)
print("Current Loans : ")
for Key, Student in Current.items():
    print(Key, ":", Student)

print("Students : ")
for Title, Names in Students.items():
    print(Title, ":", Names)
    
print("Rejected Events : ")
for Event in Rejected:
    print(Event)