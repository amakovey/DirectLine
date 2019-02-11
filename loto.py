import random
import os


# Создаём класс игровой карточки
class GameCard:
    def __init__(self):
        a = [[0] * 9 for i in range(3)]  # Массив игровой карточки для заполнения
        # Создаем массив всех возможных номеров в карточке
        card_numbers = [[i for i in range(1, 10)],
                        [i for i in range(10, 20)],
                        [i for i in range(20, 30)],
                        [i for i in range(30, 40)],
                        [i for i in range(40, 50)],
                        [i for i in range(50, 60)],
                        [i for i in range(60, 70)],
                        [i for i in range(70, 80)],
                        [i for i in range(80, 91)]]
        # Заполняем карточку номерами
        for j in range(3):
            for i in range(9):
                n = random.choice(card_numbers[i])  # Выбираем число из соотвествующего подмассива
                a[j][i] = n
                card_numbers[i].pop(card_numbers[i].index(n))  # Избегаем повтора в карточке

        # Расставляем рандомно пустые клетки в карточку
        for j in range(3):
            i = 0
            while i < 4:  # Повторяем цикл 4 раза, пока в каждой из строк карточки не проставим 4 пустых клетки (9-5=4)
                c = random.randint(0, 8)
                if a[j][c] != 0:
                    a[j][c] = 0  # 0 - признак пустой ячейки
                    i += 1
        self.card = a

    # Выводим игровую карточку на экран
    def show(self):
        for i in self.card:
            for j in i:
                if j == 0:
                    print('  ', end='|')
                elif j == 99:
                    print('--', end='|')
                elif 0 < j < 10:
                    print(' ' + str(j), end='|')
                else:
                    print(j, end='|')
            print()

    # Поиск номера бочонка в карточке
    def search_num(self, n):
        s = 0
        for i in range(3):
            for j in range(9):
                if self.card[i][j] == n:
                    s = 1
                    self.card[i][j] = 99  # 99 - признак найденной и зачеркнутой ячейки
        return s

    # Обработка правильности ввода y/n
    def input_yn(n, turn):
        print('Новый бочонок:', n, '(осталось', str(90 - turn) + ')')
        a = input('зачеркнуть цифру? (y/n) ')
        if a == 'n' or a == 'y':
            return a
        else:
            print('Ошибка ввода')
            GameCard.input_yn(n, turn)


keg = [i for i in range(1, 91, 1)]  # Массив бочонков
my_card, comp_card = GameCard(), GameCard()
my_score, comp_score, turn = 0, 0, 1

# Запуск игрового цикла
while turn < 91:
    print('------ Ваша карточка ------')
    my_card.show()
    print('---------------------------')
    print('--- Карточка компьютера ---')
    comp_card.show()
    print('---------------------------')
    n = random.choice(keg)
    yn = GameCard.input_yn(n, turn)
    print()
    keg.pop(keg.index(n))  # Удаляем бочонок из массива
    turn += 1
    m = my_card.search_num(n)
    if m == 1 and yn == 'y':
        my_score += 1
    elif m == 1 and yn == 'n':
        print('Ты проиграл, в твоей карточке была такая цифра')
        turn = 91
    elif m == 0 and yn == 'y':
        print('Ты проиграл в твоей карточке нет такой цифры')
        turn = 91
    c = comp_card.search_num(n)
    if c == 1:
        comp_score += 1
    if comp_score == 15 and my_score < 15:
        print('Комп выиграл')
        turn = 91
    if my_score == 15 and comp_score < 15:
        print('Ты выиграл')
        turn = 91
    if comp_score == 15 and my_score == 15:
        print('Ничья')
