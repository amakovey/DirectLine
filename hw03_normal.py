# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
	a,b,c=1,1,0
	fib = [1,1]
	for i in range (1,m):
		c = a+b
		a,b = b,c
		fib.append(c)
	return (fib[n-1:m])

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
	b=[]
	for j in range (len(origin_list),0,-1):
		min = origin_list[0]
		for i in range(0,j):
			if origin_list[i] < min:
				min = origin_list[i]
		b.append(min)
		origin_list.remove(min)
	return b
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def filter (a,b):
	c=[]
	for i in b:
		if a(i) == True:
			c.append(i)
	return (c)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

if (abs(x2)+abs(x1)) == (abs(x4)+abs(x3)) and (abs(y2)+abs(y1)) == (abs(y4)+abs(y3)):
	print ('Является параллелограммом')
else:
	print ('Не является параллелограммом')