import json
from Notes import Note


def main():

    while True:
        #Отображение меню
        show_menu()

        choice = input("Введите номер пункта меню: ")

        if choice == "1":
            #Создание новой заметки
            Note.save_notes_to_json(Note.create_note())

        elif choice == "2":
            #Просмотр списка заметок
            Note.get_all_notes()
        elif choice == "3":
            #Просмотр заметки
            note_id = input("Введите ID заметки: ")
            Note.read_note(note_id)
        elif choice == "4":
            #Редактирование заметки
            note_id = input("Введите ID заметки: ")
            Note.edit_note(note_id)
        elif choice == "5":
            #Удаление  заметки
            note_id = input("Введите ID заметки: ")
            Note.delete_note(note_id)
        elif choice == "0":
            #Выход из приложения
            break
        else:
            #Неверный выбор
            print("Неверный номер пункта меню.")

def show_menu():
    print("### Приложение \"Заметки\" ###")
    print("1. Создать новую заметку")
    print("2. Просмотреть список заметок")
    print("3. Прочитать заметку")
    print("4. Редактировать заметку")
    print("5. Удалить заметку")
    print("0. Выход")


if __name__ == "__main__":
    main()
