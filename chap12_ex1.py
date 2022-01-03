'''
Chapter 12
Exercise 1: Change the socket program socket1.py to prompt the user
for the URL so it can read any web page. You can use split('/') to
break the URL into its component parts so you can extract the host
name for the socket connect call. Add error checking using try and
except to handle the condition where the user enters an improperly
formatted or non-existent URL.
'''

import socket


inp = input('Enter the complete url:\n>>>')
try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = inp.split('/')[2]
    mysock.connect((hostname, 80))    
    print(hostname)
    tempcmd = 'GET ' +str(inp)+ ' HTTP/1.0\r\n\r\n'   # first make a temp string here
    #print(tempcmd)
    cmd = tempcmd.encode()                             # then encode in bytes here
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()

except:
    print('The url is incorrect/invalid')
    quit()
