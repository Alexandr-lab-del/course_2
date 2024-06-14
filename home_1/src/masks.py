def get_mask_card_number(number: str):
    """Функция маскировки номера карты"""
    return number[:4] + " " + number[4:6] + "** **** " + number[-4:]


def get_mask_account(number: str):
    """Функция маскировки номера счета"""
    return "*" * (len(number) - 18) + number[-4:]


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
