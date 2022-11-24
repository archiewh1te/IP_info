import requests
import folium

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[Provider]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Страна]': response.get('country'),
            '[Регион]': response.get('regionName'),
            '[Город]': response.get('city'),
            '[Почта]': response.get('zip'),
            '[Широта]': response.get('lat'),
            '[Долгота]': response.get('lon'),
        }

        for k, v, in data.items():
            print(f'{k}: {v}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'location/{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('[!] Проверьте ваше соединение')


def main():
    ip = input('Пожалуйста введите IP: ')

    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()
