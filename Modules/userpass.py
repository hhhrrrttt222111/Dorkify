import sys
import time

import core.search_url as search_url
import core.logo as logo
import core.colors as colors
import core.mods as mods


def userpass():
    def userpass_menu():
        global ch
        mods.clear_screen()
        logo.dorkify_logo()

        print(f'''
    CHOOSE OPTION :
    
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Vulnerable log files containing passwords     [1]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Less secured password files                   [2]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Vulnerable passwords list                     [3]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Vulnerable password DAT files                 [4]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} SQL files vulnerable passwords                [5]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Vulnerable password text files                [6]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Vulnerable password files                     [7]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Web pages with User lists                     [8]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Search for database password files            [9]  
    
        ''')

        ch = int(input("    --> "))
        print('\n\n')


    userpass_menu()

    if ch == 1:
        q = 'allintext:username,password filetype:log'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 2:
        q = 'allintext:password filetype:log'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 3:
        q = 'intitle:"index of " "*.passwords.txt"'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 4:
        q = 'filetype:dat "password.dat'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 5:
        q = 'filetype:sql password'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 6:
        q = 'intext:"Index of /" +password.txt'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 7:
        q = 'intitle:"index of" passwd'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 8:
        q = 'intitle: index.of people.lst'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 9:
        q = 'intitle: "Index of" pwd.db'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    else:
        print('INVALID OPTION  \n TRY AGAIN')
        sys.exit()