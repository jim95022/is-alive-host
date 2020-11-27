import requests


def is_alive_host(hostname: str = 'None') -> bool:
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""

    if 'http' not in hostname:
        hostname = 'http://' + hostname

    try:
        req = requests.get(hostname, timeout=5)
        response = req.status_code
    except Exception as e:
        response = -1
        print(e)

    return 100 <= response < 400
