import socket

def is_alive_host(hostname: str = 'None') -> bool:
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""

    hostname = hostname.replace('https://','').replace('http://','').split('/')[0].split(':')[0]
    PORT = 80
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    client.settimeout(1)

    try: 
        client.connect((hostname, PORT))  
        request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % hostname
        client.send(request.encode())  
        response = client.recv(4096).split()[1]
    except:
        response = -1 
    finally:
        return 100 <= int(response) < 400
