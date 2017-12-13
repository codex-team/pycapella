from pycapella import CapellaApi

def test_default_url():
    """
    Check validity of default API URL argument
    """
    assert CapellaApi().API_URL == "https://capella.pics/upload"

def test_empty_get_url():
    """
    Check None result for getting url of empty image
    """
    api = CapellaApi()
    assert api.get_url() == None
