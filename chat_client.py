from termcolor import colored
from Crypto.Cipher import AES
import socket
import os

banner = '''  __  __                                          
|  \/  | ___  ___ ___  ___ _ __   __ _  ___ _ __ 
| |\/| |/ _ \/ __/ __|/ _ \ '_ \ / _` |/ _ \ '__|
| |  | |  __/\__ \__ \  __/ | | | (_| |  __/ |   
|_|  |_|\___||___/___/\___|_| |_|\__, |\___|_|   
                                 |___/           
                                                                                                                             
                                                    * https://github.com/ProtectorHC
'''
print(banner)

#Receiving The Value Of IP and PORT From the User

SERVER_IP = input(colored("What Is Ip of the server running: ", "green"))
SERVER_PORT = int(input(colored("Enter Port No on which the server is running: ", "green")))

USER_NAME = input(colored("Please Choose a Username for Chat: "))

os.system('clear')

print(colored("<1>ONLINE..", "green", attrs=['reverse', 'blink']))

name = USER_NAME + ">> "
encoded_name = name.encode()

# chat Fucntion Initiates the Connection to the Server

def chat():
    s = socket.socket()
    #connecting to the chat server
    s.connect((str(SERVER_IP), SERVER_PORT))

    #infinite loop to recieve messages from the user till the server runs
    
    while True:
     #adding AES encryption
        magic = AES.new('EBC3D4C51C46801A7267AAB59A63551B', AES.MODE_CFB, 'This is an IV456')
        #YOU MUST REPLACE THIS AES KEY>>>FIND A AES KEY FOR YOURSELF ON GOOGLE>>>!!
        In_msg = s.recv(8192)
        recv_data_1 = magic.decrypt(In_msg)
        recv_data_unenc = recv_data_1.decode()
        print("\n" + recv_data_unenc)
        Out_msg = input(colored("\nSEND-> ", "red", attrs=['bold']))
        data = encoded_name + Out_msg.encode()
        send_data = magic.encrypt(data)
        #encrypting the data with AES
        s.send(send_data)

        #condition statement to close the chat incase server_user enters 'bye'

        if recv_data_unenc == 'bye':
            os.system('clear')
            print(colored("<0>OFFLINE", "red", attrs=['bold']))
            s.close()
            break

#Final Main function to run the Chat Program! 

def main():
    chat()
main()
