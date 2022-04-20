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

import socket

# 2 Вариант
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




from functools import reduce
from collections import Counter


stock = [[0, 6], [3, 4], [1, 4], [4, 5], [3, 5], [1, 2], [1, 3], [0, 1], [5, 6], [6, 6], [0, 4], [1, 1], [2, 3], [0, 3], [3, 3], [2, 4], [1, 5], [2, 6], [3, 6], [0, 2], [4, 4]]


new_stock = reduce(lambda x, y: x + y, stock)
print(new_stock)


new_new_stock = [item for sublist in stock for item in sublist]
print(new_new_stock)