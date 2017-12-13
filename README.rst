Pycapella
=========

Python SDK for `capella.pics`_

Installation
------------

This package is called `PyCapella`_ on PyPI. Install using:

::

    $ pip install pycapella

Usage
-----

.. code:: python

    import pycapella

    api = pycapella.CapellaApi({})

    # Save local file 'image.jpg' to the Capella
    response = api.uploadFile("image.jpg")
    assert response['success'] == True
    print("Success! Image URL is {}".format(response['url']))

    # Save remote image by url to the Capella
    response = api.uploadUrl("https://ifmo.su/public/app/img/products/capella.png")
    assert response['success'] == True
    print("Success! Image URL is {}".format(response['url']))

API Documentation
-----------------

Full documentation can be found on GitHub –
https://github.com/codex-team/capella

Issues and improvements
-----------------------

Ask a question or report a bug on the `create issue page`_.

Know how to improve PyCapella? `Fork it`_ and send pull request.

You can also write questions and suggestions to the `CodeX Team’s
email`_.

License
-------

`MIT`_

.. _capella.pics: https://capella.pics
.. _PyCapella: https://pypi.python.org/pypi/PyCapella/
.. _create issue page: https://github.com/codex-team/pycapella/issues/new
.. _Fork it: https://github.com/codex-team/pycapella
.. _CodeX Team’s email: mailto:team@ifmo.su
.. _MIT: https://github.com/codex-team/codex.notes/blob/master/LICENSE