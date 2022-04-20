# DAY 9
# -> Start Hacker project
# -> Socket Module
# -> Custom Generators


'hello'.encode()
data = data.decode()

import socket


with socket.socket() as client_socket:

  hostname = '127.0.0.1'
  port = 5000
  
  client_socket.connect((hostname, port))
  
  data = 'Wake up Neo'
  
  client_socket.send(data.encode())
  
  buffer = 1024
  response = client_socket.recv(buffer)
  response = response.decode()
  
  print(response)


#Socket
import socket


with socket.socket() as client_socket:

  hostname = '127.0.0.1'  # str
  port = 5000  # int

  address = (hostname, port)
  
  client_socket.connect(address)  # one arg!!
  
  data = 'This is my test string'
  
  client_socket.send(data.encode())  # converting to bytes
  
  buffer = 1024  # response limit
  response = client_socket.recv(buffer)
  response = response.decode()  # converting back to rea

  print(response)