def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def add_data() -> None:
    '''Добавляет информацию из справочника'''
    fio = input("Введите ФИО:  ")
    tel_number = input("Введите номер телефона: ")
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')
    print("Успешно!")

def find_data() -> None:
    '''Осуществляет поиск из справочника'''
    data = input("Введите данные для поиска: ")
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print('Результаты поиска: ')
    print(search(tel_book, data))

def search(book: str, info: str) -> str:
    ''' Находит в строке записи по определенному критерию поиска'''
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])

def change_data() -> None:
    '''Ищем по значению все данные из справочника и вносим изменения в нужное'''
    edited_data = input('Введите данные для поиска изменяемого контакта: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    result = search(tel_book, edited_data)
    print(result)

    tel_book = tel_book.split('\n')
    tel_book[tel_book.index(result)] = edited(result)
    with open('book.txt', 'w', encoding='utf-8') as f:
        for item in tel_book:
            f.write(f'\n{item}')

def edited(text: str) -> str:
    '''Вносит изменения'''
    fio = input("Введите новые данные ФИО: ")
    tel_number = input("Введите новый номер телефона: ")
    if len(fio) == 0:
        fio = text.split(' | ')[0]
    if len(tel_number) == 0:
        tel_num = text.split(' | ')[1]
    return (f'{fio} | {tel_number}')
def remove_data() -> None:
    data = input('Поиск контакта для удаления: ')

    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    result = search(tel_book, data)
    print(result)

    tel_book = tel_book.split('\n')
    tel_book.remove(result)

    with open('book.txt', 'w', encoding='utf-8') as f:
        for item in tel_book:
            f.write(f'\n{item}')