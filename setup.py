from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Python package for encode and decode strings'
LONG_DESCRIPTION = 'this package can be used to encode strings and decode strings'

setup(
    name="encodedecode",
    version=VERSION,
    author="Abipravi",
    author_email="darkparadise877@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'first package', 'encode_decode'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
