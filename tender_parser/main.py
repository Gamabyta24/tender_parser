import requests
from requests.exceptions import Timeout
LINK = "https://zakupki.gov.ru/epz/order/extendedsearch/results.html"
FZ44 = "?fz44=on"
PATERN = "https://zakupki.gov.ru"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
PAGE1 = f"{LINK}{FZ44}&pageNumber=1"
PAGE2 = f"{LINK}{FZ44}&pageNumber=2"


def get_print_form(request, url, headers, timeout=5):
    try:
        response = request.get(url, headers=headers, timeout=timeout)

        if response.status_code == 200:
            return response.text
        else:
            print(f"Ошибка: Статус код {response.status_code}")
            return None
    except Timeout:
        print(f"Ошибка:Превышено время ожидания для {url}")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None