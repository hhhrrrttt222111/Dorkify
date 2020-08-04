import sys

import core.search_url as search_url
import core.logo as logo
import core.colors as colors
import core.mods as mods

def information():
    def information_menu():
        global ch5
        mods.clear_screen()
        logo.dorkify_logo()
        print(f'''
    CHOOSE OPTION :
    
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Definition  [1]
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Information [2]
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Stocks      [3]
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Maps        [4]
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Weather     [5]
    
        ''')

        ch5 = int(input("    --> "))
        print('\n\n')

    information_menu()

    if ch5 == 1:
        s = input('SEARCH DEFINITION: ')
        q = str('define:' + s)
        print('\nSearching... \n')
        search_url.url_search(q)

    elif ch5 == 2:
        s = input('SEARCH : ')
        q = str('info:' + s)
        print('\nGathering Info... \n')
        search_url.url_search(q)

    elif ch5 == 3:
        s = input('SEARCH COMPANY WITH TICKER CODE: ')
        q = str('stocks:' + s)
        print('\nSearching Stocks \n')
        search_url.url_search(q)

    elif ch5 == 4:
        s = input('SEARCH CITY: ')
        q = str('maps:' + s)
        print('\nFinding Maps \n')
        search_url.url_search(q)

    elif ch5 == 5:
        s = input('ENTER CITY NAME: ')
        q = str('weather:' + s)
        print('\nChecking Weather \n')
        search_url.url_search(q)

    else:
        print('INVALID OPTION  \n TRY AGAIN')
        sys.exit()
