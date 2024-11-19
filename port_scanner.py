import socket

host = '151.101.192.223'
port = 80

def test_port(host: str, port: int) -> None:
    """ Test whether a given port on a host is able to be connected to
    
    Args:
    - host (str): The IPv4 address of the target host
    - port (int): A valid port number

    Output:
    - Will Output the result of the connection
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        
        try:
            sock.connect((host, port))
            print(f'Connection Succeeded with {host}:{port}')
        except:
            print(f'Connection Failed with {host}:{port}')

def validate_port_number(port: int) -> bool:
    if isinstance(port, int) and (1 <= port <= 65535):
        return True
    else:
        return False