import random
# Задаем услови домашнего задания. На входе лист из 20 имен и число 100
list_name20 = ['Iliya','Dima','Kate','Anatoliy', 'Alexander','Nikita','Evgeniy','Tolya','Marina','Irina','Sasha','Denis','Natasha','Ivan','Sophia','Elena','Artem','Svetlana','Innokentiy','Semen']
n = 100
print(list_name20)

# Задаем функцию формиования списка из случайных имен из первоначального списка
def name_list(list_name,n):
    return random.choices(list_name, k=n)

list_name100 = name_list(list_name20,n)
print(list_name100)

# функция вывода имени, которое встречается в созданном списке чаще всего
def name_fr(list_name):
    f_name = 0
    name = []
    for i in range(len(list_name)):
        if f_name <=list_name.count(list_name[i]):
            f_name = list_name.count(list_name[i])
            name = list_name[i]
    return name,f_name

name_fr(list_name100)
print(name_fr(list_name100))

# функция вывода самой редкой первой буквы имен из списка имен через сортировку списка
def liter(name_list):
    lit_list = list(map(lambda x:x[0], name_list))
    # print(name_list)
    lit_fr = []
    lit_dic = {}
    for i in lit_list:
        lit_fr.append(lit_list.count(i))
    lit_dic = list(zip(lit_list, lit_fr))
    lit_dic.sort(key=lambda x:x[1])
    return lit_dic[1]

# функция вывода самой редкой первой буквы имен из списка имен через сравнение частот
def liter1(name_list):
    lit_list = list(map(lambda x:x[0], name_list))
    f_name = 100
    name = []
    for i in range(len(lit_list)):
        if f_name >= lit_list.count(lit_list[i]):
            f_name = lit_list.count(lit_list[i])
            name = lit_list[i]
    return name,f_name

print(liter(list_name100))
print(liter1(list_name100))

