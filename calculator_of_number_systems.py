def transfer_from_any_to_10(num_in_any, base_num):
    return int(str(num_in_any), base_num)


def transfer_from_10_to_any(num_in_10, base_num):
    num_in_base = ''

    while num_in_10 >= base_num:
        ost = num_in_10 % base_num
        num_in_10 //= base_num
        if ost <= 9:
            num_in_base += str(ost)
        else:
            num_in_base += chr(ost + 55)

    if num_in_10 <= 9:
        num_in_base += str(num_in_10)
    else:
        num_in_base += chr(num_in_10 + 55)

    return num_in_base[::-1]


while True:
    initial_number_system = int(input('\nСистема счисления начального числа (2 - 36): '))
    initial_number = int(input('Число, которое хотите перевести: '))
    final_number_system = int(input('В какую систему счисления будем переводить (2 - 36): '))
    if (not str(initial_number_system).isdigit() or not str(initial_number).isdigit() or
            not str(final_number_system).isdigit()):
        print('\nВы ввели не число :(')
    elif (int(initial_number_system) < 2 or int(initial_number_system) > 36 or
          int(final_number_system) < 2 or int(final_number_system) > 36):
        print('\nСистема счисления должна находится в диапазоне (2 - 36).')
    else:
        break

num_10 = transfer_from_any_to_10(initial_number, initial_number_system)
final_number = transfer_from_10_to_any(num_10, final_number_system)

print(f'\n{initial_number_system} с.ч.: {initial_number} - {final_number_system} с.ч.: {final_number}')
