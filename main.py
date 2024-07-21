from src.data_processing import process_excel_data, process_json_data, process_csv_data
from datetime import datetime


def main():
    """Основная логика проекта"""
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice == '1':
        print("Программа: Для обработки выбран JSON-файл.")
        data = process_json_data(r'C:\Users\Александр Побережный\Desktop\питон\course_2\data\operations.json')
    elif choice == '2':
        print("Программа: Для обработки выбран CSV-файл.")
        data = process_csv_data(r'C:\Users\Александр Побережный\Desktop\питон\course_2\data\transactions.csv')
    elif choice == '3':
        print("Программа: Для обработки выбран XLSX-файл.")
        data = process_excel_data(r'C:\Users\Александр Побережный\Desktop\питон\course_2\data\transactions_excel.xlsx')
    else:
        print("Программа: Выбор некорректен.")
        return

    statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    status = input("Программа: Введите статус, по которому необходимо выполнить фильтрацию. "
                   "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: ").upper()

    while status not in statuses:
        print(f"Программа: Статус операции \"{status}\" недоступен.")
        status = input("Введите корректный статус: EXECUTED, CANCELED, PENDING\nПользователь: ").upper()

    filtered_data = [item for item in data if item['state'] == status]

    if not filtered_data:
        print("Программа: Не найдено ни одной транзакции, подходящей под условия фильтрации.")
        return

    print(f"Программа: Операции отфильтрованы по статусу \"{status}\".")

    date_sort = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ").lower()
    if date_sort == 'да':
        sort_order = input("Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: ").lower()
        reverse_sort = sort_order == 'по убыванию'
        filtered_data = sorted(filtered_data, key=lambda x: datetime.strptime(x['date'], '%d.%m.%Y'),
                               reverse=reverse_sort)

    rubles_only = input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ").lower()
    if rubles_only == 'да':
        filtered_data = [item for item in filtered_data if item['currency'] == 'RUB']

    search_word = input(
        "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ").lower()
    if search_word == 'да':
        keyword = input("Программа: Введите ключевое слово для поиска\nПользователь: ")
        filtered_data = [item for item in filtered_data if keyword in item['description']]

    for idx, item in enumerate(filtered_data, start=1):
        if 'Перевод' in item['description']:
            print(f"{idx}. {item['date']} {item['description']}")
            print(f"История: {item['from']} -> Назначение: {item['to']}")
            print(f"Сумма: {item['amount']} {item['currency']}\n")
        else:
            print(f"{idx}. {item['date']} {item['description']}")
            print(f"Сумма: {item['amount']} {item['currency']}\n")
    print(f"Программа: Всего банковских операций: {len(filtered_data)}")


if __name__ == "__main__":
    main()
