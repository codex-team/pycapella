from setuptools import setup
from os.path import join, dirname


setup(name='pycapella',
      packages=['pycapella'],
      version='0.1.5',
      description="Python SDK for capella.pics",
      long_description=open(join(dirname(__file__), 'README.rst')).read(),
      keywords='capella image upload crop resize filter transformation manipulation cdn ',
      author='CodeX Team',
      author_email='team@ifmo.su',
      url='https://github.com/codex-team/pycapella',
      license='MIT',
      classifiers=[
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Multimedia :: Graphics',
          'Topic :: Multimedia :: Graphics :: Graphics Conversion',
          'Environment :: Console',
          'Environment :: Web Environment',
      ],
      install_requires=[
          "requests"
      ],
      )
