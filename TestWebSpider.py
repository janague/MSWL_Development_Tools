#!/usr/bin/env python

################################################################################
'''
Copyright (c) 2013, janague <janague@gmail.com>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
################################################################################

import unittest

import sys
from StringIO import StringIO

import pywebspider

LENGTH_LEVEL1 = 407  # Length of output for first level (now)
LENGTH_LEVEL2 = 14004  # Length of output for second level (now)
LENGTH_LEVEL3 = 456575  # Length of output for third level (now)

class TestWebSpider (unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        
    # Test number of links in level 1
    def test_first_level (self):
        url = "http://herraiz.org"
        depth = 1
        pywebspider.print_links(url, depth)
        output = len(sys.stdout.getvalue())
        self.assertEqual(output, LENGTH_LEVEL1)

    # Test number of links in level 2
    def test_second_level (self):
        url = "http://herraiz.org"
        depth = 2
        pywebspider.print_links(url, depth)
        output = len(sys.stdout.getvalue())
        self.assertEqual(output, LENGTH_LEVEL2)
        
        
    # Test number of links in level 3
    def test_third_level (self):
        url = "http://herraiz.org"
        depth = 3
        pywebspider.print_links(url, depth)
        output = len(sys.stdout.getvalue())
        self.assertEqual(output, LENGTH_LEVEL3)

if __name__ == '__main__':
    unittest.main()
