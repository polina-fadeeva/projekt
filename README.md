Репозиторий проекта по программированию.
Программа, которая решает полиномы второго порядка.



Это программа, по сути решающая квадратные уравнения. Пользователь подает на вход уравнение в формате ввода данных:

      1) При вводе символов ".", "+", "=", "-", "*" или целого или рационального числа, вокруг них стоят пробелы, начало или конец строки;
      2) Если вводится символ "^", то слева должен стоять Х, а справа натуральное число;
      3) Справа от Х могут стоять либо "^", либо пробел, либо конец строки. Слева пробел, либо начало строки.

Далее программа выдает приведенный вид уравнения и максимальную степень полинома. Если максимальная степень больше 2, программа сообщает, что не умеет решать такие уравнения. Если максимальная степень <2, программа выдает корни уравнения, в том числе комплексные, и дает комментарий про график.

В программе также имеются флаги:

      1) -h - флаг, который показывает меню;
      2) -p - флаг, показывающий этапы решения;
      3) -P - флаг, рисующий график.

Таким образом, если ввести флаг -Р перед уравнением, программа нарисует график (необходимо предварительно скачать matplotlib). На macOS также есть цветная подсветка в терминале.


План работы:

      1) Научиться считывать информацию, которая подается на вход;
      2) Проверка полинома на валидность;
      3) Приведение полинома в нормальную форму;
      4) Решение уравнения;
      5) Дополнительные этапы: обработка ошибок, вывод сопутствующих сообщений;
      6) Добавление флагов, выводящих дополнительную информацию.


Выполнили: Фадеева П., Стойкович И.
