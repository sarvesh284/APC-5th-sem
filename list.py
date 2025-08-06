students=["sarvesh","swarup","pratik","pranav"]
batches=list(('T1','T2','T3','T4'))
marks=[90,30,50,40,45,20]
subjects=list()

students.append("ishaan")
print(students)#['sarvesh', 'swarup', 'pratik', 'pranav', 'ishaan']

students.pop()
print(students)#['sarvesh', 'swarup', 'pratik', 'pranav']

students.insert(2,"vedant")#difference between insert is that insert will add item to the list at particular position
                        #and append will add item to the last position

print(students)#['sarvesh', 'swarup', 'pratik', 'pranav']

students.remove("vedant")
print(students)#['sarvesh', 'swarup', 'pratik', 'pranav']

print(students.count("sarvesh"))
print(students)#1

print(batches)
print(marks)

print(students[1:4])
print(students[-2])#pratik

students.extend(batches)
print(students)#['sarvesh', 'swarup', 'pratik', 'pranav', 'T1', 'T2', 'T3', 'T4']

for i in students:
    print(i)

marks.sort()
print(marks)#[20, 30, 40, 45, 50, 90]

students.clear()
print(students)