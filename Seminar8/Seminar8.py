def write_name():
    name = input('Введите имя: ')
    return name

def write_surname():
    surname = input('Введите фамилию: ')
    return surname

def write_phone():
    phone = input('Введите номер телефона: ')
    return phone

def write_adress():
    adress = input('Введите адрес: ')
    return adress

def input_data(a=None):
    name = write_name()
    surname = write_surname()
    phone = write_phone()
    adress = write_adress()
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(f'{name} {surname}: {phone}\n{adress}\n\n')

def print_data():
    with open ('phonebook.txt', 'r', encoding='utf-8') as data:
        data_first = data.readlines()
        print(data_first)
        for line in data_first:
            print(line, end='')
            
            
def search_line():
    search = input('Введите данные для поиска: ')
    with open ('phonebook.txt', 'r', encoding='utf-8') as data:
        print(data)
        data_first = data.readlines()
        print(data_first)
        for line in data_first:
            if search in line: 
                print(line, end='')
                
def show_Contacts(phonebook):
    with open(phonebook, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
    input("\nДля выполнения следующих операций нажмите на Ввод\n")


def add_Contact(phonebook):         
    with open(phonebook, "a", encoding="UTF-8") as file:
        record_line = ""
        record_line += input("Введите Фамилию контакта: ") + " "
        record_line += input("Введите Имя контакта: \n") + ":\n"
        record_line += input("Введите номер телефона контакта:\n ") + "\n"
        record_line += input("Введите адрес контакта:\n ") + " "

        file.write(record_line + "\n")
    input("\nКонтакт добавлен!\nДля выполнения следующих операций нажмите на Ввод\n")


def find_Contact(phonebook):  
    target = input("Введите известные данные для поиска: ")
    result = []
    with open(phonebook, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if target in person:
                result.append(person)

    if len(result) != 0:
        printData(result)
    else:
        print(f"Контакта с такими данными в списках нет '{target}'.")

    input("\nДля выполнения следующих изменений нажмите на Ввод\n")


def change_Contact(phonebook):                    
    with open(phonebook, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите номер контакта для изменения или 0 для возврата: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newLastName = input("Введите новую фамилию: ")
            newName = input("Введите новое имя: ")
            newPhone = input("Введите новый номер: ")
            newcity = input("Введите новый адрес: ")
            data[numberContact - 1] = (
                newLastName + " " + newName + "," + newPhone + "," + newcity + "\n"
            )
            with open(phonebook, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nДанные контакта изменены!")
                input("\nДля выполнения следующих изменений нажмите на Ввод\n")
        else:
            return


def delete_Contact(phonebook): 
    with open(phonebook, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(input("Введите номер для удаления или 0 для возврата: "))
        if numberContact != 0:
            print(f"Данные {data[numberContact-1].rstrip().split(',')} удалены\n")
            data.pop(numberContact - 1)
            with open(phonebook, "w", encoding="UTF-8") as file:
                file.write("".join(data))
        else:
            return

    input("Для выполнения следующих изменений нажмите на Ввод")


def printData(data):
    phoneBook = []
    splitLine = "=" * 90
    print(splitLine)
    print(" Фамилия       Имя      Номер Телефона   Адрес")
    print(splitLine)
    personID = 1

    for contact in data:
        lastName, name, phone, adress = contact.rstrip().split(",")
        phoneBook.append(
            {   "ID": personID,
                "lastName": lastName,
                "name": name,
                "phone": phone,  
                "adress": adress,
                
            }
        )
        personID += 1

    for contact in phoneBook:
        personID, lastName, name, phone, adress = contact.values()
        print(f"{personID:>2}. {lastName:<15} {name:<10} - {phone:<16}  {adress:<18}")

    print(splitLine)


def main(file_name): 
    while True:
        phonebooksInterface()
        userChoice = int(input("Выберите пункт меню от 1 до 5 или для выхода 0: "))

        if userChoice == 1:
            show_Contacts(file_name)
        elif userChoice == 2:
            add_Contact(file_name)
        elif userChoice == 3:
            find_Contact(file_name)
        elif userChoice == 4:
            change_Contact(file_name)
        elif userChoice == 5:
            delete_Contact(file_name)
        elif userChoice == 0:
            return
        
def phonebooksInterface():
    print(" ТЕЛЕФОННАЯ КНИЖКА ")
    
    print(" [1]  Список контактов")
    print(" [2]  Добавить контакт")
    print(" [3]  Найти контакт")
    print(" [4]  Изменить данные контакта")
    print(" [5]  Удалить контакт")
    print("\n [0]  Выход")
   



main("phonebook.txt")

#input_data()
#print_data()
#search_line()