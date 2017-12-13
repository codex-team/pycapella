from pycapella import Capella
from random import randint


def test_empty_pixelize():
    """
    Test valid filtering (pixelize) settings on empty image
    """
    api = Capella()
    assert api.pixelize(100).filters == [('pixelize', 100)]


def test_empty_random_pixelize():
    """
    Test valid filtering (pixelize) settings on empty image.
    Random sample of {3..100} pixelize filters with argument={0..100}
    :return:
    """
    api = Capella()
    valid = []
    for i in range(randint(3, 100)):
        pix = randint(0, 100)
        valid.append(('pixelize', pix))
        api.pixelize(pix)
    assert api.filters == valid

