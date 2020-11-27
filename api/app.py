import requests


def is_alive_host(hostname: str = 'None') -> bool:
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""

    if 'http' not in hostname:
        hostname = 'http://' + hostname

    try:
        headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
        req = requests.get(hostname, headers=headers, timeout=5)
        response = req.status_code
    except Exception as e:
        response = -1

    return 100 <= response < 400

print(is_alive_host('semrush.com'))