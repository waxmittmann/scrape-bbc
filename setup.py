"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
# with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    name='bbc-scraper',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.0',

    description='A scraper / server to scrape the BBC website and serve up scraped data',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/waxmittmann/scrape-bbc',

    # Author details
    author='Max Wittmann',
    author_email='nein@nothere.com',

    # Choose your license
    license='MIT',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    #packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'cffi==1.2.1',
        'characteristic==14.3.0',
        'cryptography==1.0.1',
        'cssselect==0.9.1',
        'enum34==1.0.4',
        'idna==2.0',
        'ipaddress==1.0.14',
        'lxml==3.4.4',
        'pyasn1==0.1.8',
        'pyasn1-modules==0.0.7',
        'pycparser==2.14',
        'pymongo==3.0.3',
        'pyOpenSSL==0.15.1',
        'queuelib==1.3.0',
        'Scrapy==1.0.3',
        'service-identity==14.0.0',
        'six==1.9.0',
        'Twisted==15.4.0',
        'w3lib==1.12.0',
        'wheel==0.24.0',
        'zope.interface==4.1.2',
        'web.py==0.37',
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #     'sample': ['package_data.dat'],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)