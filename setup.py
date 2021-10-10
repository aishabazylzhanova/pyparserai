#from distutils.core import setup
import setuptools

setuptools.setup(
    name='pyparserai',
    version='0.0.1',
    packages=['pyparserai',],
    license='MIT',
    description = 'A parser',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author = 'Aisha Bazylzhanova',
    author_email = 'abazylzanova@gmail.com',
    install_requires=['requests'],
    url = 'https://github.com/aishabazylzhanova/pyparserai',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    )
