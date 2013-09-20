from setuptools import setup, find_packages

setup (name = 'WebSpider',
    version = '0.1',
    packages = find_packages(),
    scripts = ['myspider'],
    install_requires = ['bs4'],
    package_data = {},
    author = 'janague',
    author_email = "adfadsf@dfadsf.com",
    description = 'Spider for web pages',
    url = 'http://www.webspider.org'
    )
