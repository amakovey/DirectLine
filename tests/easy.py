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
