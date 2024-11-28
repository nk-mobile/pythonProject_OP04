def  sum_range(start, end):
    my_list = []
    for items in range(a,b + 1):
        my_list.append(items)
        pair_list = list(filter(lambda x: x % 2 == 0, my_list))
    print(my_list)
    print(pair_list)

    list_total = 0
    i = 0
    for i in range( len(pair_list)):
        list_total = list_total + pair_list[i]
    return list_total

a = int(input("Введите старт : "))
b = int(input("Введите финиш : "))

result = sum_range(a,b)
print(f"Сумма чётных значений в диапозоне от {a} до {b} : {result}")
