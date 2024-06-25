from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция общей маскировки карты и счета"""
    numbers = ""
    words = ""
    for i in number:
        if i.isalpha() or i == " ":
            words += i
        else:
            numbers += i
    payment_name = words.rstrip()
    payment_number = get_mask_account(numbers) if payment_name.startswith("Счет") else get_mask_card_number(numbers)
    return f"{payment_name} {payment_number}"


def get_data(data: str) -> str:
    """Функция преобразования даты"""
    date_part, time_part = data.split("T")
    date_obj = datetime.strptime(date_part, "%Y-%m-%d")
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000 7922 8960 6361"))
    print(mask_account_card("Maestro 7000 7922 8960 6361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_data("2018-07-11T02:26:18.671407"))
