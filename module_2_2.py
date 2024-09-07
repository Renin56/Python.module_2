first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')

if first == second and first == third and second == third:
    print('3 - все числа равны')
elif first == second or first == third or second == third:
    print('2 - равны 2 числа')
else:
    print('0 - равных чисел нет')
