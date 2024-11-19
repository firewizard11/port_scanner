import unittest
from port_scanner import validate_port_number


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


if __name__ == '__main__':
    unittest.main()