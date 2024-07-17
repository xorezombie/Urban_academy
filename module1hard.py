grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a_grade = [sum(grades[0])/len(grades[0]) , sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
print(a_grade)
students=list(students)
students.sort()
print(students)
students_grades = {students[0] : a_grade[0], students[1] : a_grade[1], students[2] : a_grade[2], students[3] : a_grade[3], students[4] : a_grade[4]}
print(students_grades)
