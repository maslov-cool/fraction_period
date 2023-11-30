# Для увеличения количества чисел после запятой в числе можно использовать модуль decimal
from decimal import Decimal, getcontext

# устанавливаем точность вычислений в 50000 знаков
getcontext().prec = 50000
n = str(Decimal(int(input())) / Decimal(int(input())))
if len(n) > 15:
    i = 0
    while n[i] != '.':
        i += 1
    i += 1
    while n[i] not in n[i + 99:]:
        i += 1
    period = [n[i]]
    i += 1
    while True:
        if len(period) == 1:
            if len(set(n[i - 1:i + 99])) == 1:
                break
            else:
                period.append(n[i])
                i += 1
        else:
            if period == list(n[i: i + len(period)]):
                break
            else:
                period.append(n[i])
                i += 1
    for i in period:
        print(i, end='')
else:
    print(0)

