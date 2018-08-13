import unittest

from pycapella import Capella


class TestMain(unittest.TestCase):

    def test_default_url(self):
        """
        Check validity of default API URL argument
        """
        assert Capella().API_URL == "https://capella.pics/upload"

    def test_empty_get_url(self):
        """
        Check None result for getting url of empty image
        """
        assert Capella().get_url() == None


if __name__ == '__main__':
    unittest.main()
