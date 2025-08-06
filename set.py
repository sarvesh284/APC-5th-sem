students = {"sarvesh", "swarup", "pratik", "pranav"}
batches = set(('T1', 'T2', 'T3', 'T4'))
marks = {90, 30, 50, 40, 45, 20}
subjects = set()

students.add("ishaan")
print("After adding ishaan:", students)

students.remove("ishaan")
print("After removing ishaan:", students)

students.add("vedant")
print("After adding vedant:", students)

students.remove("vedant")
print("After removing vedant:", students)

print("Is sarvesh present?", "sarvesh" in students)  # True or False

print("Batches:", batches)
print("Marks:", marks)

print("Subset (converted to list):", list(students)[1:4])  # slicing done via list

print("2nd last student (converted to list):", list(students)[-2])  # indexing done via list

students.update(batches)
print("After extending students with batches:", students)

for i in students:
    print(i)

sorted_marks = sorted(marks)
print("Sorted marks:", sorted_marks)  # [20, 30, 40, 45, 50, 90]

students.clear()
print("Students after clear:", students)  # set()
