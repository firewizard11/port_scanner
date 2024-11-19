import unittest
from port_scanner import validate_port_number, validate_ipv4


class TestPortValidation(unittest.TestCase):
    def test_type(self):
        self.assertTrue(validate_port_number(1))
        self.assertTrue(validate_port_number(50))
        self.assertTrue(validate_port_number(50000))

        self.assertFalse(validate_port_number('hello'))
        self.assertFalse(validate_port_number([1, 2, 5000]))
        self.assertFalse(validate_port_number({1, 2, 3, 5000}))
        self.assertFalse(validate_port_number(1.2341))
        self.assertFalse(validate_port_number(4444.10238190))

    def test_range(self):
        self.assertTrue(validate_port_number(1))
        self.assertTrue(validate_port_number(65535))
        self.assertTrue(validate_port_number(50555))
        self.assertTrue(validate_port_number(80))
        self.assertTrue(validate_port_number(4444))

        self.assertFalse(validate_port_number(-20))
        self.assertFalse(validate_port_number(0))
        self.assertFalse(validate_port_number(65536))
        self.assertFalse(validate_port_number(100000))

class TestIPv4Validation(unittest.TestCase):
    def test_valid_ip(self):
        self.assertTrue(validate_ipv4('192.168.1.1'))
        self.assertTrue(validate_ipv4('10.0.0.1'))
        self.assertTrue(validate_ipv4('172.16.0.1'))
        self.assertTrue(validate_ipv4('8.8.8.8'))
        self.assertTrue(validate_ipv4('1.1.1.1'))
        self.assertTrue(validate_ipv4('123.45.67.89'))
        self.assertTrue(validate_ipv4('0.0.0.0'))
        self.assertTrue(validate_ipv4('255.255.255.255'))
        self.assertTrue(validate_ipv4('127.0.0.1'))

    def test_invalid_ip(self):
        self.assertFalse(validate_ipv4('256.256.256.256'))
        self.assertFalse(validate_ipv4('192.168.1.1.1'))
        self.assertFalse(validate_ipv4('192.168.01.1'))
        self.assertFalse(validate_ipv4('192.168.1.-1'))
        self.assertFalse(validate_ipv4('192.168.1.abc'))
        self.assertFalse(validate_ipv4('192.168.1.'))
        self.assertFalse(validate_ipv4('192..1.1'))
        self.assertFalse(validate_ipv4('192.168.1.256'))
        self.assertFalse(validate_ipv4('300.300.300.300'))
        self.assertFalse(validate_ipv4('1234.123.123.123'))

if __name__ == '__main__':
    unittest.main()