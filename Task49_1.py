# Задача 38: 
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

import os, sys

def main_import_contacts():
    with open(os.path.join(sys.path[0], 'phonebook.txt'), 'r', encoding='utf-8') as data: 
        s = data.readlines()
        for i in range(len(s)):
            phonebook[i] = s[i].split()

def import_contacts(some_string):
    finded_contacts = list()
    for i in phonebook:
        if some_string in phonebook[i]:
            finded_contacts.append(phonebook[i])
    return finded_contacts

def export_contact(new_contact):
    with open(os.path.join(sys.path[0],'phonebook.txt'), 'a+', encoding='utf-8') as data:
        data.writelines(' '.join(new_contact) +'\n')
        phonebook[len(phonebook)+1] = new_contact

def input_contact():
    new_contact = [input('surname: ')]
    new_contact.append(input('name: '))
    new_contact.append(input('given name: '))
    new_contact.append(input('phonenumber: '))
    export_contact(new_contact)

def find_contact():
    s = import_contacts(input('wadda we search?: '))
    print(*s)
    
def delete_contact(el):
    with open(os.path.join(sys.path[0], 'phonebook.txt'), 'r', encoding='utf-8') as data:
        lines = data.readlines()
        with open (os.path.join(sys.path[0], 'phonebook.txt'), 'r', encoding='utf-8') as data:
            for line in lines:
                if el not in line:
                    data.write(line)
    delete_contact()

def replace_contact(el):
    with open(os.path.join(sys.path[0], 'phonebook.txt'), 'r', encoding='utf-8') as data:
        lines = data.readlines()
        with open (os.path.join(sys.path[0], 'phonebook.txt'), 'w', encoding='utf-8') as data:
            for line in lines:
                if el not in line:
                    line = line.split()
                    for part in line:
                        new_note = part.replace(part, input(f'Введите новую информацию вместо {part} => '))
                        data.writelines(new_note + '')
                        print('Done')
                else:
                    data.write(str(line))
    replace_contact()

def user_interface():
    main_import_contacts()
    print('Phonebook\nwhadda want?\n1 - add contact\n2 - find contact\n3 - delete contact\n4 - replace contact\n5 - print whole book\nany other input - end program')
    user_input = input('your choise: ')
    while user_input in ('1', '2', '3', '4', '5'):
        if user_input == '1':
            input_contact()
        elif user_input == '2':
            find_contact()
        elif user_input == '3':
            delete_contact()
        elif user_input == '4':
            replace_contact
        elif user_input == '5':
            print()
            for i in phonebook:
                print(*phonebook[i])
        user_input = input('\nyour choise: ')
            
    print('bye')

phonebook = dict()
user_interface()
