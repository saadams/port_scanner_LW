import socket,subprocess


subprocess.call('clear',shell=True)
target = input("Enter the target to scan: ")
ip = socket.gethostbyname(target)

print("Scanning host: ", ip)

for port in range(1, 65536):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    
    result = s.connect_ex((ip, port))
    
    if result == 0:
        print(f"Port {port} is open")
    
    s.close()
