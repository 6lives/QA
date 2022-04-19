
enter_list = input("Введите числа через пробел: ").split()

work_list = []

ind_num = 0

try:
    enter_num = float(input("Введите число: "))
except ValueError:
    enter_num = -100000
    print("Это не число.")


for i in enter_list:
    try:
        i.replace(',','.')
        if '.' in i:
            if float(i):
                work_list.append(float(i))
                continue
        if int(i):
                work_list.append(int(i))
                continue

    except:
        continue

def sort_list (list):
    for i in range(1, len(list)):
        x = list[i]
        idx = i
        while idx > 0 and list[idx-1] > x:
            list[idx] = list[idx-1]
            idx -= 1
            list[idx] = x
    return list


def binary_search_min(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if element> array[middle-1] and element <= array[middle]:  # если элемент в середине,
        return middle -1  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search_min(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search_min(array, element, middle + 1, right)


work_list = sort_list (work_list)
if enter_num> work_list[0] and enter_num <= work_list[-1]:
    ind_num = binary_search_min(work_list, enter_num, 0, len(work_list) - 1)
    print("Массив чисел исходный : " , enter_list)
    print("Массив чисел отсортированный для работы : " , work_list)
    print("Число для поиска : " , enter_num)
    print("Требуемый индекс : " , ind_num)
