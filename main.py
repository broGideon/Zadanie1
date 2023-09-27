import math
def prov():
    try:
        sum1 = int(input("Введите число 1 "))
        sum2 = int(input("Введите число 2 "))
        return sum1,sum2
    except:
        print("Введено неверное значение")
        return 0,0
def prov1():
    try:
        sum1 = int(input("Введите число 1 "))
        return sum1
    except:
        print("Введено неверное значение")
        return 0,0
def sum(sum1,sum2):
    return sum1+sum2
def vich(sum1,sum2):
    return sum1-sum2
def proiz(sum1,sum2):
    return sum1*sum2
def chast(sum1,sum2):
    if sum2 != 0:
        return sum1/sum2
    else:
        print("На ноль делить нельзя")
def pow(sum1,sum2):
    return math.pow(sum1,sum2)
def sqrt(sum1):
    return math.sqrt(sum1)
def factorial(sum1):
    return math.factorial(sum1)
def sin(sum1):
    return math.sin(sum1)
def cos(sum1):
    return math.cos(sum1)
def tan(sum1):
    return math.tan(sum1)
num = 0
while num!=11:
    print ("Выберети действие")
    print("1. Сложиь 2 числа")
    print("2. Вычесть первое из второго")
    print("3. Перемножить два числа")
    print("4. Разделить первое на второе")
    print("5. Возвести в степень N первое число")
    print("6. Найти квадратный корень из числа")
    print("7. Найти факториал из числа")
    print("8. Найти синус")
    print("9. Найти косинус")
    print("10. Найти тангенс")
    print("11. Выход")
    try:
        num= int(input())
    except:
        print("Введите действие")
    match num:
        case 1:
            sum1, sum2 = prov()
            print('Ответ:', sum(sum1, sum2))
        case 2:
            sum1, sum2 = prov()
            print('Ответ:', vich(sum1, sum2))
        case 3:
            sum1, sum2 = prov()
            print('Ответ:', proiz(sum1, sum2))
        case 4:
            sum1, sum2 = prov()
            print('Ответ:', chast(sum1, sum2))
        case 5:
            sum1, sum2 = prov()
            print('Ответ:', pow(sum1, sum2))
        case 6:
            sum1 = prov1()
            print('Ответ:', sqrt(sum1))
        case 7:
             sum1 = prov1()
             print('Ответ:', factorial(sum1))
        case 8:
            sum1 = prov1()
            print('Ответ:', sin(sum1))
        case 9:
            sum1 = prov1()
            print('Ответ:', cos(sum1))
        case 10:
            sum1 = prov1()
            print('Ответ:', tan(sum1))