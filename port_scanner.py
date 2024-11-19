import socket


def test_port(host: str, port: int, verbose: bool = False) -> None:
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
            if verbose:
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

if __name__ == '__main__':
    host = '10.10.14.80'
    ports = [80, 443, 21, 22, 139, 445]

    if not validate_ipv4(host):
        raise ValueError(f'{host} is not a valid IPv4 address')

    for port in ports:
        if not validate_port_number(port):
            raise ValueError(f'{port} is not a valid Port Number')
        
    for port in ports:
        test_port(host, port)