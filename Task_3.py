#   Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек 
#   в этой четверти (x и y).

print("Введите № координатной четверти: ")
n = int (input())
if(n == 1):
    print("Диапазонами возможных координат являются: x > 0, y > 0")
else:
    if(n == 2):
        print("Диапазонами возможных координат являются: x < 0, y > 0")
    else:
        if(n == 3):
            print("Диапазонами возможных координат являются: x < 0, y < 0")
        else: 
            if(n == 4):
                print("Диапазонами возможных координат являются: x > 0, y < 0")
            else:
                print("Заданное число НЕ соответствует НИ одной из четвертей")