print('# Задание 1')
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

xxxx = {}

for std in students:
    if xxxx.get(std['first_name']) == None:
        xxxx[std['first_name']] = 1
    else:
        xxxx[std['first_name']] += 1

for key, value in xxxx.items():
    print(key, value)

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


print('# Задание 2')
# Дан список учеников, нужно вывести самое часто повторящееся имя.

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

xxxx = {}

for std in students:
    if xxxx.get(std['first_name']) == None:
        xxxx[std['first_name']] = 1
    else:
        xxxx[std['first_name']] += 1

print('Самое частое имя:', max(xxxx, key=lambda key: xxxx[key])) # этот вариант не понятен

s_name = [0]

for key, value in xxxx.items():
	if s_name[0] == value:
		s_name.append(key)
	if (s_name == []) or (s_name[0] < value):
		s_name = [value]
		s_name.append(key)
	
print('Самое частое имя:', ', '.join(s_name[1:]))	

# ???
# Пример вывода:
# Самое частое имя среди учеников: Маша


print('# Задание 3')

# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.

school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

class_nmb = 0

for class_students in school_students:
	class_nmb += 1
	each_class = {}
	for std in class_students:
		if each_class.get(std['first_name']) == None:
			each_class[std['first_name']] = 1
		else:
			each_class[std['first_name']] += 1

	print('Самое частое имя в классе ', class_nmb, ': ', max(each_class, key=lambda key: each_class[key]))


# ???
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


print ('# Задание 4')
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.

school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]

is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}


for each_class in school:
	m_count = 0
	f_count = 0

	for student in each_class['students']:
		if is_male.get(student['first_name']) == True:
			m_count += 1
		else:
			f_count += 1

	print('В классе', each_class['class'], f_count, 'девочки и', m_count, 'мальчика.')

# ???
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.





print('# Задание 5')
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.

school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]

is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

most_male = {}
most_female = {}


for each_class in school:
	m_count = 0
	f_count = 0

	for student in each_class['students']:
		if is_male.get(student['first_name']) == True:
			m_count += 1
		else:
			f_count += 1
	
	class_name = each_class['class']
	most_male[class_name] = m_count
	most_female[class_name] = f_count

print('Больше всего мальчиков в классе', max(most_male, key=lambda key: most_male[key]))
print('Больше всего девочек в классе', max(most_female, key=lambda key: most_female[key]))



# ???
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a