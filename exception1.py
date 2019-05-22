"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user_brak(answer = ''):
  while answer != 'Хорошо':
    try:
      print('Как дела?')
      answer = input()
    except KeyboardInterrupt:
      print('Пока!')
    finally:
      break

if __name__ == "__main__":
    ask_user()
