#!/usr/bin/python3

import os
import sys 
import requests
from termcolor import colored



def main():
    url = sys.argv[1]
    wordlist = sys.argv[2]
    exten = ('.html','.css','.js','.txt','.php','/')
    art()
    lch = requests.get(url)
    print('Url: ', url)
    print('WrL: ', wordlist)
    if str(lch.status_code) == '200':
        if os.path.exists(wordlist):
            with open(wordlist) as wl:
                for i in wl.readlines():
                    for x in exten: 
                        if not i.startswith('#'):
                            a = url + i.rstrip('\n') + x
                            r = requests.get(a)
                            status = str(r.status_code)
                            if status == '200':
                                arrow(a, r, status)
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
 ##    # #   # #   #     #     #      #     #    ###### #   #"""
    print (colored(ar.replace(' ', '-'), 'blue' ))
    
def arrow(ab, bb, bc):

    print(colored("-->", 'red'), ab, bb, bc, end="")


main()
