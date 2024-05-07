grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average_grades = {}

for i in range(len(students)):
    average = sum(grades[i]) / len(grades[i])
    average_grades[list(students)[i]] = average

# Вывод списка студентов в алфавитном порядке
sorted_students = sorted(list(students))
print("Список студентов в алфавитном порядке:")
for student in sorted_students:
    print(student)

print("\nСредние оценки студентов:")
print(average_grades)
