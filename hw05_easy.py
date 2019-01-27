# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
def make_dir(name):
	dir_path = os.path.join(os.getcwd(), name)
	try:
		os.mkdir(dir_path)
		print ('Папка', name, 'создана')
	except FileExistsError:
		print ('Папка уже существует')
	
def del_dir(name):
	dir_path = os.path.join(os.getcwd(), name)
	try:
		os.removedirs(dir_path)
		print ('Папка', name, 'удалена')
	except FileNotFoundError:
		print ('Папка', name,'не существует')
	except NotADirectoryError:
		print (name,'не является папкой')
	except OSError:
		print ('Папка не пуста')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def view_folder():
	tree = os.walk(os.getcwd(),topdown=True)
	a=[]
	for i in tree:
		a.append(i)
	if len(a[0][1]):
		for i in a[0][1]:
			print (i)
	else:
		print ('Папка пуста')

def view_all():
	a=os.listdir(os.getcwd())
	print ('Содержимое папки', os.getcwd())
	for i in a:
		print (i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file(name):
	copy_name = 'copy_'+name
	myfile = open (name, mode ='r', encoding='UTF-8')
	myfile1 = open (copy_name, mode ='w', encoding='UTF-8')
	for data in myfile:
		myfile1.write(data)
	myfile.close()
	myfile1.close()
	
