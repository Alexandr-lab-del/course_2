from home_1.src.masks import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(number: int | str) -> str:
    """Функция общей маскировки карты и счета"""
    numbers = ""
    words = ""
    for i in number:
        if i.isalpha() or i == " ":
            words += i
            continue
        else:
            numbers += i
    if words == "Счет ":
        return words.replace("    ", " ") + get_mask_account(numbers)
    else:
        return words.replace("    ", " ") + get_mask_card_number(numbers)


def get_data(data):
    """Функция преобразования даты"""
    date_part, time_part = data.split('T')
    date_obj = datetime.strptime(date_part, '%Y-%m-%d')
    formatted_date = date_obj.strftime('%d.%m.%Y')
    return formatted_date


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000 7922 8960 6361"))
    print(mask_account_card("Maestro 7000 7922 8960 6361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_data("2018-07-11T02:26:18.671407"))
    