import requests
from bs4 import BeautifulSoup,XMLParsedAsHTMLWarning
import warnings
from requests.exceptions import Timeout, RequestException

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
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


def get_print_links(html):
    if html is None:
        print("get_ptint_link: входной аргумент None")
        return None
    html_parser = BeautifulSoup(html, "html.parser")
    links = html_parser.find_all(
        "a", href=lambda href: href and "/epz/order/notice/printForm/view.html" in href
    )
    return links


def update_link(link, patern):
    href = link.get("href", "")
    if "view.html" not in href:
        return None
    new_href = "".join([patern, href.replace("view.html", "viewXml.html")])
    return new_href

def get_data(link, headers=None):
    try:
        response = requests.get(link, headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"Ошибка при получении страницы. Статус код: {response.status_code}")
            return None

        soup = BeautifulSoup(response.content, "lxml")

        publish_dt = soup.find("publishdtineis")
        if not publish_dt:
            print("Элемент 'publishdtineis' не найден на странице.")
            return None

        data = publish_dt.text.strip()
        return data

    except RequestException as e:
        print(f"Произошла ошибка при запросе к странице: {e}")
        return None
    except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}")
        return None

def process_page(page, headers, patern):
    html_form = get_print_form(requests, page, headers)
    if html_form is None:
        exit(1)

    links = get_print_links(html_form)
    if links is None:
        exit(1)

    updated_links = []
    for link in links:
        updated_link = update_link(link, patern)
        if updated_link is not None:
            updated_links.append(updated_link)

    results = {}
    for link in updated_links:
        data = get_data(link, headers)
        results[link] = data
    return results

def main():
    pages = [PAGE1,PAGE2]
    all_results = {}
    for page in pages:
        results = process_page(page, HEADERS, PATERN)
        all_results.update(results)
    for key, item in all_results.items():
        print(f'Ссылка:{key}, Дата:{item}')
if __name__ == "__main__":
    main()