import pandas as pd
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
}

def get_needed_properties(soup):
    tds = soup.find_all('td')
    data = {"IMO": "Нет", "MMSI": "Нет", "AIS тип": "Нет"}

    for i in range(len(tds) - 1):
        title = tds[i].get_text().strip()
        value = tds[i + 1].get_text().strip()

        if "IMO" in title and "MMSI" in title:
                parts = value.split("/")
                data["IMO"] = parts[0].strip()
                data["MMSI"] = parts[1].strip()
        elif "IMO" in title:
            data["IMO"] = value
        elif "MMSI" in title:
            data["MMSI"] = value
        elif "AIS тип" in title:
            data["AIS тип"] = value

    return data

def get_ship_data(url):
    print(f"Парсинг {url[45:]}...")
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print("ОШИБКА с кодом {response.status_code}")
            return None

        soup = BeautifulSoup(response.content, 'html.parser')
        found_ships = soup.find_all('a', class_='ship-link')

        if len(found_ships) != 1:
            print(f"Не ровно один корабль")
            return None

        response = requests.get(f"https://vesselfinder.com{found_ships[0]['href']}", headers=HEADERS)

        if response.status_code != 200:
            print(f"ОШИБКА с кодом {response.status_code}")
            return None

        soup = BeautifulSoup(response.content, 'html.parser')
        data = get_needed_properties(soup)
        name = soup.find('h1', class_='title').get_text().strip()
        data['Название'] = name

        return data
    except Exception as e:
        print(f"Возникло исключение: {e}")
        return None

df = pd.read_excel('Links.xlsx')
links = df['Ссылка'].tolist()
export_data = []

with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(get_ship_data, links))

export_data = [r for r in results if r is not None]

df_result = pd.DataFrame(export_data)
df_result = df_result[["Название", "IMO", "MMSI", "AIS тип"]]

df_result.to_excel('result.xlsx', index=False)
print(f"Файл result.xlsx успешно создан!")
