#!/usr/bin/python3

import os
import sys
import requests
import argparse
from termcolor import colored



def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--url",required=True)
    parser.add_argument("-l","--wlist",required=True)
    parser.add_argument("-c","--cert",default=False)
    args = parser.parse_args()

    art()

    codes = ['100','101','102','103','200','201','202','203','204','205','206','207','226','300','301','302','403']
    exten = ('.html','.css','.js','.txt','.php','/')


    discoverer(args.url, args.wlist, args.cert, codes, exten)



def discoverer(url, wlist, cert, codes, exten):
    num_tr = 0
    s = requests.Session()
    lch = s.get(url, verify=cert)
    print('Url: ', url)
    print('WordList: ', wlist, '\n')
    if str(lch.status_code) == '200':
        if os.path.exists(wlist):
            with open(wlist) as wl:
                for i in wl.readlines():
                    for x in exten: 
                        if not i.startswith('#') and not i == "\n": 
                            a = url + i.rstrip('\n') + x
                            r = s.get(a)
                            status = str(r.status_code)
                            num_tr += 1
                            sys.stdout.write("\rTry: " + str(num_tr))
                            sys.stdout.flush()
                            if status in codes:
                                arrow(a, status) # r       
        else:
            print("File Does Not Exist")
            
    else:
        print("Host Not Responding Check the Url")    


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

    print(colored("-->", 'red'), ab, colored('Responce: ', 'magenta'), bb, "\n" ,end="")


main()
