__author__ = 'Маковей А.Н.'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)
#for a in range (999999, 9999999999999999):
a = float('inf')
print(a == a*2)
print(a == a**2)
print(a > 999999)