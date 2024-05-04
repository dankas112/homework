grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_grades = {}
students_list = list(students)
a = len(students_list) - 1

students_list.sort()
students_list.reverse()
grades.reverse()

while a > -1:
    grades[a] = sum(grades[a]) / len(grades[a])
    students_grades[students_list[a]] = grades[a]
    a -= 1

print(students_grades)
