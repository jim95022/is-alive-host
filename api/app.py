import requests
from urllib.parse import urlparse


def is_alive_host(hostname: str = 'None') -> bool:
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""

    parsed_hostname = urlparse(hostname)

    if not parsed_hostname.scheme:
        parsed_hostname = parsed_hostname._replace(scheme='http')
        parsed_hostname = parsed_hostname._replace(netloc=parsed_hostname.path)
        parsed_hostname = parsed_hostname._replace(path='')
        
    try:
        response = requests.get(parsed_hostname.geturl(), timeout=2)
        response = response.status_code
    except:
        response = -1
     
    return 100 <= response < 400
