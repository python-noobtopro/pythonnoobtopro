'''
Chapter 12
Exercise 2: Change your socket program so that it counts the number
of characters it has received and stops displaying any text after it has
shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count
of the number of characters at the end of the document.
'''

import socket
doc = ''            # blank, store all data here t
inp = input('Enter the complete url:\n>>>')
try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = inp.split('/')[2]
    mysock.connect((hostname, 80))
    print(hostname)
    tempcmd = 'GET ' +str(inp)+ ' HTTP/1.0\r\n\r\n'   # first make a temp string here
    #print(tempcmd)
    cmd = tempcmd.encode()                            # then encode in bytes here
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        doc = doc + data.decode()  #always decode after encode
        doc = doc
        print(doc[:3001])
        print('Length of data stream received:',len(doc))

    mysock.close()

except:
    print('The url is incorrect/invalid')
    quit()
