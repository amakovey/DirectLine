# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
class Triangle:
	def __init__(self, a,b,c):
		self.a = a
		self.b = b
		self.c = c
		self.o_a = math.sqrt((b[1]-a[1])*(b[1]-a[1]) + (b[0]-a[0])*(b[0]-a[0]))
		self.o_b = math.sqrt((c[1]-b[1])*(c[1]-b[1]) + (c[0]-b[0])*(c[0]-b[0]))
		self.o_c = math.sqrt((c[1]-a[1])*(c[1]-a[1]) + (c[0]-a[0])*(c[0]-a[0]))
		self.p = (self.o_a+self.o_b+self.o_c)/2
		self.pl = math.sqrt(self.p*(self.p-self.o_a)*(self.p-self.o_b)*(self.p-self.o_c))
	def ploshad(self):
		return self.pl
	def perimetr(self):
		return self.o_a+self.o_b+self.o_c
	def visota (self):
		v_a = 2*self.pl/self.o_a
		v_b = 2*self.pl/self.o_b
		v_c = 2*self.pl/self.o_c
		return max(v_a, v_b, v_c)

#t1= Triangle([0,0],[2,2],[4,0])
#print (t1.ploshad())
#print (t1.perimetr())
#print (t1.visota())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class Trapecia:
	def __init__(self, a,b,c,d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.o_a = math.sqrt((b[1]-a[1])*(b[1]-a[1]) + (b[0]-a[0])*(b[0]-a[0]))
		self.o_b = math.sqrt((c[1]-b[1])*(c[1]-b[1]) + (c[0]-b[0])*(c[0]-b[0]))
		self.o_c = math.sqrt((d[1]-c[1])*(d[1]-c[1]) + (d[0]-c[0])*(d[0]-c[0]))
		self.o_d = math.sqrt((d[1]-a[1])*(d[1]-a[1]) + (d[0]-a[0])*(d[0]-a[0]))
		self.oac = math.sqrt((c[1]-a[1])*(c[1]-a[1]) + (c[0]-a[0])*(c[0]-a[0]))
		self.odb = math.sqrt((d[1]-b[1])*(d[1]-b[1]) + (d[0]-b[0])*(d[0]-b[0]))
		self.h = math.sqrt(4*(self.o_a*self.o_a)-((self.o_d-self.o_b)*(self.o_d-self.o_b)))/2
	def is_trapecia(self):
		if self.oac == self.odb:
			return 'Равнобочная'
		else:
			return 'Неравнобочная'
	def ploshad(self):
		return (self.o_b+self.o_d)*self.h/2
	def dlini(self):
		return 'a=', self.o_b, 'b=', self.o_d, 'c=', self.o_a, 'd=', self.o_c
	def perimetr(self):
		return self.o_a+self.o_b+self.o_c+self.o_d
#t1= Trapecia([0,0],[2,2],[4,2],[6,0])	
#print (t1.is_trapecia())
#print (t1.perimetr())
		
		
		