import socket

try:
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # AF_INET is used for IPv4 addresses 
    #and SOCK_DGRAM is for UDP protocol
    print("Socket successfully created.")
    #receiver side

    ip_add="192.168.129.117"# ip address of the receiver
    port=33445
    complete_add=(ip_add, port)
    s.bind(complete_add)

    while True:
        message,sender_address=s.recvfrom(1024)

        print("Raw Message:", message)
        print("Sender Address:", sender_address)

        decoded_message = message.decode('ascii')
        print("Decoded Message:", decoded_message)

   
    #s.close()  # Close the socket connection
except Exception as e:
    print(f"An error occurred: {e}")
