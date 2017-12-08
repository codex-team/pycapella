from setuptools import setup, find_packages
from os.path import join, dirname


setup(name='pycapella',
      packages=['pycapella'],
      version='0.1',
      description="Python SDK for capella.pics",
      long_description=open(join(dirname(__file__), 'README.rst')).read(),
      keywords='capella image upload crop resize filter transformation manipulation cdn ',
      author='CodeX Team',
      author_email='team@ifmo.su',
      url='https://github.com/codex-team/pycapella',
      license='MIT',
      python_requires='>=3.5',
      classifiers=[
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Topic :: Multimedia :: Graphics',
          'Topic :: Multimedia :: Graphics :: Graphics Conversion',
          'Environment :: Console',
          'Environment :: Web Environment',
      ],
      install_requires=[
          "requests"
      ],
      )