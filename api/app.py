import requests


def is_alive_host(hostname: str = 'None') -> bool:
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""

    if 'http' not in hostname:
        hostname = 'https://' + hostname

    try:
        headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
        req = requests.get(hostname, headers=headers, timeout=5)
        response = req.status_code
    except Exception as e:
        response = -1

    return 100 <= response < 400

print(is_alive_host('semrush.com'))