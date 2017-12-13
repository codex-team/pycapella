# Pycapella

Python SDK for [capella.pics](https://capella.pics)

## Installation

This package is called [PyCapella](https://pypi.python.org/pypi/PyCapella/) on PyPI. Install using:

    $ pip install pycapella

## Usage

```python
import pycapella

api = CapellaApi({})

# Save local file 'image.jpg' to the Capella
response = api.uploadFile("image.jpg")
assert response['success'] == True
print("Success! Image URL is {}".format(response['url']))

# Save remote image by url to the Capella
response = api.uploadUrl("https://ifmo.su/public/app/img/products/capella.png")
assert response['success'] == True
print("Success! Image URL is {}".format(response['url']))
```

## API Documentation

Full documentation can be found on GitHub – [https://github.com/codex-team/capella](https://github.com/codex-team/capella)

## Issues and improvements

Ask a question or report a bug on the [create issue page](https://github.com/codex-team/pycapella/issues/new).

Know how to improve PyCapella? [Fork it](https://github.com/codex-team/pycapella) and send pull request.

You can also write questions and suggestions to the [CodeX Team's email](mailto:team@ifmo.su).

## License

MIT

Copyright (c) 2017 CodeX Team <team@ifmo.su>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
