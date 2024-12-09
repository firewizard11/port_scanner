import socket
import argparse
import threading
from typing import Set, List

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
    # Check if port is an integer and is in the valid port number range
    if isinstance(port, int) and (1 <= port <= 65535):
        return True
    else:
        return False


def validate_ipv4(ip_addr: str) -> bool:
    # '.' Must be in a valid IPv4
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


def format_ports(i_ports: str) -> Set[int]:
    # I chose a set since there should be only unique port numbers
    f_ports = set()

    # Comma-Sep Format (E.g. 1,2,3,4)
    if ',' in i_ports:
        m_ports = i_ports.split(',')
        for port in m_ports:
            if port.isdecimal() and validate_port_number(int(port)):
                f_ports.add(int(port))
            else:
                raise ValueError(f'{i_ports} is invalid')
        
        return f_ports
    
    # Range Format (i.e. Start-End (inclusive))
    if '-' in i_ports:
        m_ports = i_ports.split('-')
        if len(m_ports) > 2:
            raise ValueError(f'{i_ports} is invalid')
        
        if not (m_ports[0].isdecimal() and validate_port_number(int(m_ports[0]))):
            raise ValueError(f'{i_ports} is invalid')
        
        if not (m_ports[1].isdecimal() and validate_port_number(int(m_ports[1]))):
            raise ValueError(f'{i_ports} is invalid')
        
        f_ports = set(range(int(m_ports[0]), int(m_ports[1]) + 1))
        
        return f_ports
    
    # Single Port
    if i_ports.isdecimal():
        port = int(i_ports)
        if validate_port_number(port):
            return {port}
        else:
            raise ValueError(f'{i_ports} is invalid')


def sequential_scan(host: str, ports: Set[int], verbose) -> None:
    for port in ports:
        test_port(host, port)


def threaded_scan(host: str, ports: Set[int], verbose) -> None:
    threads: List[threading.Thread] = []

    for port in ports:
        thread = threading.Thread(target=test_port, args=(host, port, verbose))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('host')
    parser.add_argument('ports')
    parser.add_argument('--threaded', '-t', action='store_true')
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()

    host = args.host
    if not validate_ipv4(host):
        raise ValueError(f'{host} is not a valid IPv4 address')

    ports = format_ports(args.ports)
    threaded = args.threaded
    verbose = args.verbose

    print(verbose, type(verbose))
    print(threaded, type(threaded))


    if threaded:
        print(f'Starting threaded scan on {host}')
        threaded_scan(host, ports, verbose)
    else:
        print(f'Starting sequential scan on {host}')
        sequential_scan(host, ports, verbose)