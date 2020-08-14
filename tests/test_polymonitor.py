import unittest
from polymonitor.polymonitor import get_status_code
from requests import codes


class TestPolyMonitor(unittest.TestCase):
    def test_good_get_status_code(self):
        """
        Test that it returns an OK status code for known working urls.
        """
        assert get_status_code('google.com') == codes.ok

    def test_bad_get_status_code(self):
        """
        Test that it returns a bad status code for known working urls.
        """
        assert get_status_code('google.com/404') != codes.ok

    def test_long_url_get_status_code(self):
        """
        Test that it returns an OK status code for known working urls.
        """
        assert get_status_code('https://google.com') == codes.ok


if __name__ == '__main__':
    unittest.main()
