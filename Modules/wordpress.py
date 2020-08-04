import time
import sys

import core.search_url as search_url
import core.logo as logo
import core.colors as colors
import core.mods as mods


def wordpress():

    def wp_menu():
        global ch
        mods.clear_screen()
        logo.dorkify_logo()

        print(f'''
    CHOOSE OPTION :
    
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} WP sites that are running the Wordfence WAF         [1]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Search for WP configuration files                   [2]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Finds config files for MySQL, ABSPATH, WP           [3] 
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Search for backed-up database.sql files             [4]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Log information for vulnerable WP sites             [5]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Debug log in vulnerable WP sites                    [6]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} SQL dump files of WP sites                          [7]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Webshell Upload. WordPress Levo-Slideshow           [8]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} MAC OS X WP Information                             [9]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} wp-config Database password of vulnerable WP sites  [10]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Find vulnerable wp-config.php files                 [11]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Search for misconfigured WP sites                   [12]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Search for sensitive data, db in public folders     [13]  
    
        ''')

        ch = int(input("    --> "))
        print('\n\n')

    wp_menu()

    if ch == 1:
        q = 'filetype:ini "wordfence"'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 2:
        q = 'intext:DB_PASSWORD || intext:"MySQL hostname" ext:txt'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 3:
        q = 'inurl:"-wp13.txt"'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 4:
        q = 'inurl:"/wp-content/wpclone-temp/wpclone_backup/"'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 5:
        q = 'inurl:log -intext:log ext:log inurl:wp-'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 6:
        q = 'inurl:wp-content/debug.log'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 7:
        q = 'filetype:sql intext:wp_users phpmyadmin'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 8:
        q = 'inurl:"/wp-content/uploads/levoslideshow/"'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 9:
        q = 'intitle:Index of /__MACOSX'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 10:
        q = '''inurl:wp-config -intext:wp-config "'DB_PASSWORD'"'''
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 11:
        q = 'inurl:wp-admin/admin-ajax.php inurl:wp-config.php'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 12:
        q = 'inurl:wp-admin/ intext:css/'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 13:
        q = 'inurl:/wp-content/wpbackitup_backups'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    else:
        print('INVALID OPTION  \n TRY AGAIN')
        sys.exit()

