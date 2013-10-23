MSWL_Development_Tools
======================

Requirements
======================

Spider to track the updates of a web page
-----------------------------------------
You will have to write a Python application that get the current version of a web page, compare
against a local cache of the page, and if changed, retrieve the new version of the page and write
in the standard output a summary of the changes.

The spider must visit all the links below the current page. The log of changes displayed in
the standard output will contain a list of all the links that have been changed, and the number
of lines of difference between the two versions.

The application must be easily installable using Python standard deployment methods, must
be properly document and must include a battery of tests to check that it is working as expected.

All the development will be done using Git version control, and all the code will be publicly
available in a Git repository, with frequent commits.

Supporting material
- Slides about advanced Python development
- Snippets of sample source code

NB: Actually, the basic requirements of the application only have to list all the links of a web page.

Possible Test cases
--------------------

webspider.py 

webspider.py -h 

webspider.py  -n 1 http://herraiz.org

webspider.py  -n 2 http://herraiz.org | tail -n 20

webspider.py  -n 3 http://herraiz.org | tail -n 30

First release
--------------
**Create your first release**

https://github.com/janague/MSWL_Development_Tools/wiki/Create-your-first-release

**Register your package with the Python Package Index (PyPI)**

https://github.com/janague/MSWL_Development_Tools/wiki/Register-your-package-with-the-Python-Package-Index-PyPI

https://pypi.python.org/pypi/WebSpider
