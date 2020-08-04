import sys
import time

import core.search_url as search_url
import core.logo as logo
import core.colors as colors
import core.mods as mods


def ftp():
    def ftp_menu():
        global ch
        mods.clear_screen()
        logo.dorkify_logo()

        print(f'''
    CHOOSE OPTION :

        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Detect vulnerable FTP sites                  [1]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Finding potential log files in FTP servers   [2]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Find open FTP Servers                        [3]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Find admin folders on FTP servers            [4]  

        ''')

        ch = int(input("    --> "))
        print('\n\n')

    ftp_menu()

    if ch == 1:
        q = 'inurl:ftp://ftp'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 2:
        q = '"index of" /ftp/logs'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 3:
        q = 'intitle:"index of" inurl:ftp'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 4:
        q = 'intitle:"index of" inurl:ftp intext:admin'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    else:
        print('INVALID OPTION  \n TRY AGAIN')
        sys.exit()
