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

import urllib2
import settings as st
from bs4 import BeautifulSoup as Soup

def retrieve_url (url):
    """ This function retrieve all urls tagged by 'a' in the html source code.
    """
    opener = urllib2.build_opener()
    try:
	t = opener.open (url).read ()
	parser = Soup(t)
	return [x['href'] for x in parser.findAll ('a') if x.has_attr ('href')]
    except urllib2.URLError:
        # URL is not properly formed
	return []
    except ValueError:
        # URL has a error value
        return []

def print_links (url, depth, bullet=st.WS_BULLET):
    """ print links in recursive mode """
    if depth == 0:
        # Depth is overtaken then return to up level
        return

    links = retrieve_url (url)
    for l in links:
        d = depth - 1
        if l:
            print '%s %s' %(bullet,l)
        print_links (l,d,bullet+st.WS_BULLET)
