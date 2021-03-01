l1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

# print(min(l1))


# clonl1 = set(l1)
# print(clonl1)


# for i in range(10):
#     if i==0 or i==9:
#         for j in range(10):
#             print('*',end='')
#     else:
#         print('*', end='')
#         for j in range(1,9):
#             print(' ', end='')
#         print('*', end='')
#     print()


# a=1
# while a<=9:
#     b=1
#     while b<=9:
#         c=a*b
#         print(c, end=" ")
#         b+=1
#     print()
#     a+=1


while True:
    menu = input(
        "1. найти min число в листе\n "
        "2. удалить все одинаковые значения\n "
        "3. заменить каждое четвертое значение на 'Х'\n "
        "4. вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа\n "
        "5. Выход\n "
        "Сделайте свой выбор: ")
    if menu == "1":
        print(l1)
        print(min(l1))
    elif menu == "2":
        print(l1)
        clonl1 = set(l1)
        print(clonl1)
    elif menu == "3":
        print(l1)
        print("none")
    elif menu == "4":
        print(l1)
        print("5.5")
    elif menu == "5":
        break
