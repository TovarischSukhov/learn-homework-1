"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
classes = [
  {'school_class': '4a', 'scores': [3,4,4,5,2]},
  {'school_class': '4b', 'scores': [3,5,5,3,1]},
  {'school_class': '4c', 'scores': [4,2,3,3,1]},
  {'school_class': '4d', 'scores': [5,4,4,5,5]},
  ]

def main(classes):
  avgScore = []
  
  for dicts in classes:
    avgScore.append(sum(dicts['scores']) / float(len(dicts['scores'])))
    print(
      dicts['school_class'],
      ':',
      sum(dicts['scores']) / float(len(dicts['scores']))
    )

  print('All school avarage score:', sum(avgScore)/len(avgScore))
  # равно ли среднее средних, общемк среднему? [2,3,2,2,2] и [5]

if __name__ == "__main__":
    main()
