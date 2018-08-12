from pycapella import Capella


def test_default_url():
    """
    Check validity of default API URL argument
    """
    assert Capella().API_URL == "https://capella.pics/upload"


def test_empty_get_url():
    """
    Check None result for getting url of empty image
    """
    assert Capella().get_url() == None
