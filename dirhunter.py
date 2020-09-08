'''
MIT License

Copyright (c) 2020 5skr0ll3r

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

#!/usr/bin/python3

import os
import sys 
import requests
from termcolor import colored



def main():
    codes = ['100','101','102','103','200','201','202','203','204','205','206','207','226','300','301','302','403']
    url = sys.argv[1]
    wordlist = sys.argv[2]
    exten = ('.html','.css','.js','.txt','.php','/')
    art()
    lch = requests.get(url)
    print('Url: ', url)
    print('WrL: ', wordlist, '\n')
    if str(lch.status_code) == '200':
        if os.path.exists(wordlist):
            with open(wordlist) as wl:
                for i in wl.readlines():
                    for x in exten: 
                        if not i.startswith('#'):
                            a = url + i.rstrip('\n') + x
                            r = requests.get(a)
                            status = str(r.status_code)
                            if status in codes:
                                arrow(a, status) # r
                                print('\n')        
        else:
            print("File Does Not Exist")
            
    else:
        print("Host Not Responding Check Url")    

def art():
    
    ar = """
 ##    # ###   #   # #       # ##      # ####### ###### ###
 # #   # #  #  #   # #       # # #     #    #    #      #  #
 #  #  # #   # #   # #       # #  #    #    #    #      #   #
 #   # # #  #  #####  #     #  #   #   #    #    ###### #  #
 #  #  # # #   #   #   #   #   #    #  #    #    #      # #
 # #   # #  #  #   #    # #    #     # #    #    #      #  #
 ##    # #   # #   #     #     #      #     #    ###### #   #\n"""
    print (colored(ar.replace(' ', '_'), 'yellow' ))
    
def arrow(ab, bb):

    print(colored("-->", 'red'), ab, colored('Responce: ', 'magenta'), bb, end="")


main()
