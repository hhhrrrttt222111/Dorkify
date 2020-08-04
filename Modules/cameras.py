import sys
import time

import core.search_url as search_url
import core.logo as logo
import core.colors as colors
import core.mods as mods


def cameras():
    def camera_menu():
        global ch
        mods.clear_screen()
        logo.dorkify_logo()

        print(f'''
    CHOOSE OPTION :
    
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Camera 1               [1]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Camera 2               [2]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Liveapplet Cam         [3]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Public CCTV 1          [4]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Public CCTV 2          [5]  
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Public CCTV 3          [6] 
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Multiple CCTV gallery  [7]  '
    
        ''')

        ch = int(input("    --> "))
        print('\n\n')


    camera_menu()


    if ch == 1:
        q = 'inurl:view/view.shtml'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 2:
        q = 'intitle:”live view” intitle:axis'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 3:
        q = 'intitle:liveapplet inurl:LvAppl'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 4:
        q = 'inurl:ViewerFrame?Mode='
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 5:
        q = 'inurl:”CgiStart?page=”'
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 6:
        q = '''intitle:"webcamXP 5" inurl:8080 'Live' '''
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    elif ch == 7:
        q = '''intitle:"webcam 7" inurl:'/gallery.html' '''
        print('\n Searching...\n')
        time.sleep(1)
        search_url.url_search(q)

    else:
        print('INVALID OPTION  \n TRY AGAIN')
        sys.exit()
