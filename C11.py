name = "Vladut"

#Difference between Tuples () and Arrays [] is, that Tuples are immutable! It is recommended to use them, when we don't want values from it modified

months = ("January","February","March")

students = ["John","Diana","George"]

print(students)
print(students[0])
students.append("Kate")
print(students[-1])
students.insert(2,"Vladut")
print(students)