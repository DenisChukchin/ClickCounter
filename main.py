import argparse
import os
from urllib.parse import urlparse
import requests
from dotenv import load_dotenv


def parsed_link(user_url):
    chopped_link = urlparse(user_url)
    parsed_url = f"{chopped_link.netloc}{chopped_link.path}"
    return parsed_url


def is_bitlink(token, parsed_url):
    assembled_link = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url}'
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(assembled_link, headers=headers)
    return response.ok


def check_full_url_scheme(full_url):
    if full_url.startswith(("https://", "http://")):
        long_url = full_url
    else:
        long_url = f"https://{full_url}"
    return long_url


def create_short_link(token, long_url):
    bitly_url = "https://api-ssl.bitly.com/v4/bitlinks"
    request_options = {
        "long_url": long_url
    }

    headers = {
        "Authorization": f"Bearer {token}",
    }

    response = requests.post(bitly_url, json=request_options, headers=headers)
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(token, parsed_url):
    bitly_url = "https://api-ssl.bitly.com/v4/bitlinks"
    assembled_link = f"{bitly_url}/{parsed_url}/clicks/summary"
    options = {
        "unit": "day",
        "units": -1
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(assembled_link, params=options, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def parse_args():
    parser = argparse.ArgumentParser(
        description="Создаёт ссылку типа Bit.ly или считает клики по ссылке"
    )
    parser.add_argument("user_url", type=str, help="Введите ссылку", metavar="URL")
    args = parser.parse_args()
    return args


def main():
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')
    user_url = parse_args().user_url
    parsed_url = parsed_link(user_url)
    try:
        if not is_bitlink(token, parsed_url):
            long_url = check_full_url_scheme(user_url)
            bitlink = create_short_link(token, long_url)
            return print(f"Битлинк: {bitlink}")
        else:
            clicks = count_clicks(token, parsed_url)
            return print(
                "По вашей ссылке прошли:",
                f"{clicks} раз(а)"
            )
    except requests.exceptions.HTTPError as error:
        return print("Ошибка ввода данных!\n"
                     "Проверь вводимый URL и(или) API токен.\n", error)


if __name__ == "__main__":
    main()
