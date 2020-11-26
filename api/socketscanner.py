import socket
for port in range(1,65535): 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    socket.setdefaulttimeout(1) 
      
    # returns an error indicator 
    result = s.connect_ex(('google.com',port)) 
    if result ==0: 
        print("Port {} is open".format(port)) 
    s.close() 