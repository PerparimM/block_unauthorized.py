# block_unauthorized.py

This code is a simple firewall script in Python that blocks unauthorized access to a network. 
It creates a socket and binds it to a specified IP address and port, and then listens for incoming connections.
When a connection is received, the code checks the IP address of the incoming connection against a list of authorized IP addresses. 
If the IP address is not authorized, the connection is immediately closed. Otherwise, the connection is allowed to continue.
