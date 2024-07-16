import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_currency}&amount={amount}"


def convert_to_rubles(currency, amount):
    """Конвертирует указанное количество валюты в указанную сумму в рублях,
    спользуя API для получения актуального курса обмена"""
    if currency == "RUB":
        return amount

    url = BASE_URL.format(to="RUB", from_currency=currency, amount=amount)
    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("result", None)
    else:
        print(f"Ошибка при запросе к API: {response.status_code} - {response.text}")
        return None
