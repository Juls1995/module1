grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
print(students)
dictionary = dict(zip(students, grades))
print(dictionary)
list = grades[0]
a = sum(list)/len(list)
list1 = grades[1]
b = sum(list1)/len(list1)
list2 = grades[2]
c = sum(list2)/len(list2)
list3 = grades[3]
d = sum(list3)/len(list3)
list4 = grades[4]
e = sum(list4)/len(list4)
grades = a, b, c, d, e
dictionary = dict(zip(students, grades))
print(dictionary)