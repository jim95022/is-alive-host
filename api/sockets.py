import socket


def is_alive_host(hostname: str = 'None') -> bool:
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""

    hostname = str(hostname)

    target_port = 80 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    
    client.connect((hostname,target_port))  
    
    # request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % hostname
    # client.send(request.encode())  
    
    response = client.recv(4096)  
            
    return response
