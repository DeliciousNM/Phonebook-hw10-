# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# Показывает информацию в файле

#меню
def menu():
    print("1. Отобразить весь справочник\n"
          "2. Поиск по имени\n"
          "3. Поиск по фамилии\n"
          "4. Поиск по номеру телефона\n"
          "5. Добавить контакт\n"
          "6. Удалить контакт\n"
          "7. Изменить данные контакта\n"
          "8. Сохранить справочник\n"
          "9. Выход\n")
    choice = int(input())
    return choice

#Чтение txt файла
def read_txt(filename):
    result = []
    category = ["Фамилия", "Имя", "Номер", "Описание"]
    with open(filename, "r", encoding="utf-8") as data:
        for line in data:
            read = dict(zip(category, line.strip().split(",")))
            result.append(read)
        return result

#Использование меню
def menu_functional():
    choice = menu
    phonebook = read_txt("pb.txt")
    while (choice !=9):
        if choice == 1:
            show_phonebook(phonebook)
        elif choice == 2:
            show_phonebook(find_by_name(phonebook))
        elif choice == 3:
            show_phonebook(find_by_surname(phonebook))
        elif choice == 4:
            show_phonebook(find_by_number(phonebook))
        elif choice == 5:
            add_new_contact(phonebook)
            write_txt("pb.txt", phonebook)
        elif choice == 6:
            delete_contact(phonebook)
            rewrite_txt("pb.txt", phonebook)
        elif choice == 7:
            change_data_contact(phonebook)
            rewrite_txt("pb.txt", phonebook)
        elif choice == 8:
            save_txt()
        choice = menu()
        
#1. отобразить весь справочник
def show_phonebook(phonebook):
    for element in phonebook:
        for key in element:
            print(f"{key} : {element[key]}")
        print()

#2. Поиск по имени
def find_by_name(phonebook):
    name = input("Введите имя: ")
    result = []
    for element in phonebook:
        if element ["Имя"] == name:
            result.append(element)
        return(result)
            
#3. Поиск по фамилии
def find_by_surname(phonebook):
    surname = input("Введите фамилию: ")
    result = []
    for element in phonebook:
        if element ["Фамилия"] == surname:
            result.append(element)
        return(result)
    
#4. Поиск по номеру
def find_by_number(phonebook):
    number = input("Введите номер: ")
    result = []
    for element in phonebook:
        if element ["Номер"] == number:
            result.append(element)
        return(result)
    
#5. Добавить контакт
def add_new_contact(phonebook):
    record = dict()
    for k in phonebook[0].keys():
        record[k] = input(f"Введите {k}: ")
    phonebook.append(record)

def write_txt(filename, phonebook):
    with open(filename, "a", encoding="utf-8") as data:
        line = ""
        for i in phonebook[-1].values():
            line += i + ","
        data.write(f"{line[:-1]}\n")
        
#6. Удалить контакт
def delete_contact(phonebook):
    contact = input("Введите имя/фамилию/номер контакта: ")
    for element in phonebook:
        for i in element.values():
            if i == contact:
                phonebook.remvoe(element)
                
def rewrite_txt(filename, phonebook):
    with open(filename, "w", encoding="utf-8") as data:
        for i in range(len(phonebook)):
            line = ""
            for v in phonebook[i].values():
                line += v + ","
            data.write(f"{line[:-1]}\n")

#7. Изменить данные контакта
def change_data_contact(phonebook):
    contact = input("Введите фамилию/имя/номер контакта: ")
    changed_attribute = input("Введите название атрибута [имя | фамилия | номер | описание]: ")
    new_attribute = input("Введите новое значение атрибута: ")
    for element in phonebook:
        for v in element.values():
            if v in element == contact:
                element[changed_attribute] = element[changed_attribute].replace(element[changed_attribute], new_attribute)

#8. Сохранить справочник
def save_txt():
    filename = input("Введите название справочника: ")
    shutil.copyfile("pb.txt", f"{filename}.txt")

#9. Выход

import shutil
menu_functional()