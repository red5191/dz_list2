x = int(input('Введите конец первого списка: '))
y = int(input('Введите конец второго списка: '))

list1 = [i for i in range(0, x, 2)]
print(list1)
list2 = [j for j in range(1, y)]
print(list2)

list3 = []
for n in range(max(len(list1), len(list2))):
    try:
        list3.append(list1[n] + list2[n])
    except IndexError:
        if len(list1) > len(list2):
            list3.append(list1[n])
        if len(list1) < len(list2):
            list3.append(list2[n])

print(list3)