from setuptools import setup
from str2date import __version__

setup(
    name = 'str2date',
    packages = [ 'str2date' ],
    version = __version__,
    description = 'Proper Parser of ISO 8601 Calendar Date and Time Strings',
    author = 'Avner Herskovits',
    author_email = 'avnr_ at outlook.com',
    url = 'https://github.com/avnr/str2date',
    download_url = 'https://github.com/avnr/str2date/tarball/' + __version__,
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
)
