students = ("sarvesh", "swarup", "pratik", "pranav")
batches = tuple(('T1', 'T2', 'T3', 'T4'))
marks = (90, 30, 50, 40, 45, 20)
subjects = tuple()



students = students[:-1]
print(students)  # ('sarvesh', 'swarup', 'pratik', 'pranav')





print(students.count("sarvesh"))  # 1
print(students)  # ('sarvesh', 'swarup', 'pratik', 'pranav')

print(batches)
print(marks)

print(students[1:4])
print(students[-2])  # 'pratik'

students = students + batches
print(students)  # ('sarvesh', 'swarup', 'pratik', 'pranav', 'T1', 'T2', 'T3', 'T4')

for i in students:
    print(i)

sorted_marks = tuple(sorted(marks))
print(sorted_marks)  # (20, 30, 40, 45, 50, 90)

students = tuple()
print(students)  # ()
