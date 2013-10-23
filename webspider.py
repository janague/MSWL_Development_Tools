#!/usr/bin/python

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

# Import standard modules
import sys
import pywebspider
import argparse
from bs4 import BeautifulSoup as Soup

# Import program modules
from pywebspider import settings as st

def main():
    """ Parse arguments and call principal function print_links"""
    
    # Set description and version of the program
    parser = argparse.ArgumentParser (description="Let is craaaawl the Internet",
                                      version="%(prog)s 0.1",
                                      epilog="The Birds are coming!!! Close your windows.")
     
    # Parse the target url
    parser.add_argument ("url" ,
                        nargs='?',
                        help="target URL")
    
    # Parse argument to show license
    parser.add_argument ("-l",
                        "--license",
                        help="show license",
                        action="store_true")

    # Parse argument to get the number of levels for scanning
    parser.add_argument ("-n",
                        "--number-of-levels",
                        type=int ,
                        default=1,
                        help="how deep the craaaawl will go")
    
    # Parse argument to set different bullet, default *
    parser.add_argument ("-b",
                        "--bullet",
                        default="*",
                        help="Set different bullet character to print levels of scanning")
    
    # Parse argument to do verbose of the program 
    parser.add_argument("--verbosity",
                        help="increase output verbosity",
                        action="store_true")

    args = parser.parse_args ()

    # Print license
    if args.license:
        print st.WS_LICENSE
        sys.exit(0) 
    
    # set verbosity value
    if args.verbosity:
        print "Info: Verbosity turned on"  
        
    # Change default character for bullet
    if args.bullet:
        st.WS_BULLET = args.bullet[0]
        bullet = args.bullet  

    # Limit of levels that will be explored
    depth = args.number_of_levels
    # Url to scan
    url = args.url
    if url == None:
        print "Warning: URL is required"
        print """usage: webspider.py [-h] [-v] [-l] [-n NUMBER_OF_LEVELS] [-b BULLET] 
                    [--verbosity]
                    [url]"""

        sys.exit(0)

    if args.verbosity:
        print "Info: depth=%s." % depth
        print "Info: url=%s." % url
        print "Info: Bullet: %s." % st.WS_BULLET
        
    # Print all links in recursive mode
    pywebspider.print_links(url, depth, bullet)

if __name__ == '__main__':
    main()
