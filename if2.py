"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
  #функция должна возврящать результат, а не выводить на экран
  # выводить лучше результат запуска
  print ('Ваши последние слова?')
  s1 = input()
  s2 = input()
  # из инпута всегда строки приходят, давай лучше функуия на вход будет принимать 2 переменные, запусти ее несколько раз
  # в коде, чтобы проверить, что все корректно работает
  if (isinstance(s1, str) == False or isinstance(s2, str) == False):
  # в питоне не принято сравнивать булевы операторы, if и так с ними работать умеет
  # для отрицания есть оператор not
    print(0)
  elif len(s1) == len(s2):
    print(1)
  elif len(s1) > len(s2):
    print(2)
  elif (len(s1) != len(s2) and s2 == 'learn'):
    print(3)
    
if __name__ == "__main__":
    main()
