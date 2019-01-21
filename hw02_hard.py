# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
print (float(equation[equation.find('=')+2:equation.find('+')-2])*x+float(equation[equation.find('+')+2:(len(equation))]))

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

import re

date = re.split(r'\.', date)
try:
	day = date[0]
	month = date[1]
	year =date[2]
	if (len(day)!=2) or (len(month)!=2) or (int(year) > 9999) or (int(year) < 1):
		print ('Date is incorrect')
	if (int(month)<1) or (int(month)>12) or (int(day)>31) or (int(day)<1) or ((int(month) == 2 or int(month) == 4 or  int(month) == 6 or int(month) == 9 or int(month) == 11)  and int(day) >30):
		print ('Date is incorrect')
	

except BaseException:
	print ('Date is incorrect')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
import math
def find_room(tower,room):
	q = len (tower)
	for i in range(q):
		try:
			w = tower[i].index(room)
			print (i+1,w+1)
		except BaseException:
			continue
def make_tower(quad):
	b=[]
	a=[]
	i = 1
	j = 1
	for x in range(quad):
		i = i+1
		for z in range (1,i):
			for q in range (1,i):
				a.append(j)
				j=j+1
			b.append(a)
			a=[]
	return b
room = int(input())
quad = math.sqrt(room)
quad = math.floor(quad)
tower = make_tower(quad)
print ('This is tower:')
for i in range(len(tower)-1,0,-1):
	print (tower[i])
print ('This is coordinates of room:')
find_room(tower,room)