#!/usr/bin/python

################################################################################
# Copyright (c) 2013, janague <janague@gmail.com>
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met: 

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer. 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution. 

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
################################################################################

import sys
import pywebspider
import argparse
from bs4 import BeautifulSoup as Soup

def main():
    """ Main function: Argument are parsered"""
    
    parser = argparse.ArgumentParser (description = "Let is craaaawl the Internet",
                                    version = '0.1')

    parser.add_argument ('url' , nargs =1 , help = 'target URL')

    parser.add_argument ('-n',
                        '--number-of-levels',
                        type = int ,
                        default =1,
                        help = 'how deep the craaaawl will go')

    args = parser.parse_args ()

    # Limit of levels that will be explored
    depth = args.number_of_levels
    # Url to scan
    url = args.url[0]

    print 'depth=%s.' %depth
    print 'url=%s.' %url

    # Print all links in recursive mode
    pywebspider.print_links(url, depth)

if __name__ == '__main__':
    main()
