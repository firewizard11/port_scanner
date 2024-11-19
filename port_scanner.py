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


def validate_ipv4(ip_addr: str) -> bool:
    if not isinstance(ip_addr, str) or ('.' not in ip_addr):
        return False
    
    octets = ip_addr.split('.')

    if len(octets) != 4:
        return False
    
    for octet in octets:
        if len(octet) > 3:
            return False

        if not octet.isdecimal():
            return False
        
        if not (0 <= int(octet) <= 255):
            return False
        
        if octet[0] == '0' and len(octet) > 1:
            return False
        
    return True