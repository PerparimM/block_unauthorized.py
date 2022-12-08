# This is a simple firewall script in Python
# PerpaimM

import socket

# Define the IP address and port of the firewall
FIREWALL_IP = "192.168.0.1"
FIREWALL_PORT = 8080

# Create a socket for the firewall
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port of the firewall
sock.bind((FIREWALL_IP, FIREWALL_PORT))

# Start listening for incoming connections
sock.listen()

# Create a list of authorized IP addresses
AUTHORIZED_IPS = ["192.168.0.2", "192.168.0.3"]

# Continuously handle incoming connections
while True:
  # Accept an incoming connection
  conn, addr = sock.accept()

  # Check if the IP address of the incoming connection is authorized
  if addr[0] not in AUTHORIZED_IPS:
    # Close the connection if the IP is not authorized
    conn.close()
  else:
    # Allow the connection to continue if the IP is authorized
    pass
