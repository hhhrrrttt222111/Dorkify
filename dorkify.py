#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import argparse

import core.search_url as search_url
import core.logo as logo
import core.colors as colors
import core.mods as mods
import Modules.wordpress as wp
import Modules.information as info
import Modules.userpass as up
import Modules.cameras as cam
import Modules.ftp as ftp


parser = argparse.ArgumentParser()
ap = parser.add_mutually_exclusive_group()
ap.add_argument('--cli', help='Run the Command Line version of Dorkify', action='store_true')
ap.add_argument('--wp', help='WordPress sites vulnerabilities', action='store_true')
ap.add_argument('--up', help='Find vulnerable Usernames and Passwords', action='store_true')
ap.add_argument('--cam', help='Find vulnerable CCTV cameras', action='store_true')
ap.add_argument('--ftp', help='Find open FTP Servers', action='store_true')
ap.add_argument('-v', '--version', help='Version', action="version", version='1.02')
ap.add_argument('-s', '--search', type=str, help='Do a Google search')
ap.add_argument('-b', '--book', type=str, help='Search for a book or author')
ap.add_argument('-mu', '--music', type=str, help='Search for songs or artists')
ap.add_argument('-m', '--maps', type=str, help='Find maps of a city')
ap.add_argument('-w', '--weather', type=str, help='Check weather of a city')
ap.add_argument('-i', '--info', type=str, help='Get Information')
ap.add_argument('-d', '--define', type=str, help='Define a term')
ap.add_argument('-st', '--stocks', type=str, help='Search for Stock of a company with Ticker value')
ap.add_argument('--intitle', type=str, help='Search for a keywords in website title')
ap.add_argument('--inurl', type=str, help='Search for a keywords in website URL')
ap.add_argument('--site', type=str, help='Search for a Site')
args = vars(parser.parse_args())



notice = f'''
    {colors.bcolors.OKBLUE}Please read the following information carefully before using this tool.
    The content of the this repository is for educational purposes and uses only.
    Do not use this tool excessively. Google Dorking might be legal but using the 
    functionality for cyber terrorism, cyber thefts and other malicious activities is illegal.
    Using this tool is not anonymous and one needs to be aware that Google knows who you are
    and from where and when you perform these searches.{colors.bcolors.ENDC} 
    
    
    {colors.bcolors.RED}DO YOU AGREE TO TO OUR TERMS AND CONDITIONS ?{colors.bcolors.ENDC}  (Y / N) :  
    '''



def url_menu():
    global ch2
    mods.clear_screen()
    logo.dorkify_logo()
    print(f'''
CHOOSE OPTION :

    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Find with specific terms in website titles  [1]
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Find with specific terms in website URL's   [2]
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Find Website                                [3]

    ''')

    ch2 = int(input("    --> "))
    print('\n\n')


def hacking_menu():
    global ch6
    mods.clear_screen()
    logo.dorkify_logo()
    print(f'''
CHOOSE OPTION :

    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Wordpress Site Dorks                                       [1]  
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Find WordPress websites that are running the Wordfence WAF [2]    
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Find vulnerable Usernames and Passwords                    [3]    
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Find vulnerable CCTV cameras                               [4]   
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Find vulnerable Web Servers                                [5] 
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Search for Log files                                       [6] 
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Find open FTP Servers                                      [7] 

    ''')

    ch6 = int(input("    --> "))
    print('\n\n')

def dorkify_menu():
    global ch
    mods.clear_screen()
    logo.dorkify_logo()
    print(f'''
CHOOSE OPTION :

    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Google Search   [1]
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} URL Search      [2]
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Books           [3]
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Music Downloads [4]
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Information     [5]
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Dork Hacks!     [6]    
    ''')

    ch = int(input("    --> "))
    print('\n\n')


# WordPress

if args['wp']:
    logo.dorkify_logo()
    print(notice)
    yn = input()
    if yn == 'y' or yn =='Y':
        wp.wordpress()
    else :
        print('YOU MUST AGREE TO THE TERMS')
        sys.exit()

# Username & Passwords

if args['up']:
    logo.dorkify_logo()
    print(notice)
    yn = input()
    if yn == 'y' or yn =='Y':
        up.userpass()
    else :
        print('YOU MUST AGREE TO THE TERMS')
        sys.exit()


# Cameras

if args['cam']:
    logo.dorkify_logo()
    print(notice)
    yn = input()
    if yn == 'y' or yn =='Y':
        cam.cameras()
    else :
        print('YOU MUST AGREE TO THE TERMS')
        sys.exit()

# FTP Server

if args['ftp']:
    logo.dorkify_logo()
    print(notice)
    yn = input()
    if yn == 'y' or yn =='Y':
        ftp.ftp()
    else :
        print('YOU MUST AGREE TO THE TERMS')
        sys.exit()


# Main Program

if args['cli']:
    logo.dorkify_logo()
    print(notice)
    yn = input()
    if yn == 'y' or yn =='Y':
        dorkify_menu()
    else :
        print('YOU MUST AGREE TO THE TERMS')
        sys.exit()

    if ch == 1:
        q = input('SEARCH : ')
        print('\n Performing Google Search\n')
        search_url.url_search(q)

    elif ch == 2:
        url_menu()
        if ch2 == 1:
            s = input('SEARCH : ')
            q = str('intitle:' + s)
            print('\nSearching... \n')
            search_url.url_search(q)

        elif ch2 == 2:
            s = input('SEARCH : ')
            q = str('inurl:' + s)
            print('\nSearching... \n')
            search_url.url_search(q)

        elif ch2 == 3:
            s = input('SEARCH : ')
            q = str('site:' + s)
            print('\nSearching... \n')
            search_url.url_search(q)

        else:
            print('INVALID OPTION  \n TRY AGAIN')
            sys.exit()


    elif ch == 3:
        s = input('SEARCH BOOKS/AUTHORS: ')
        q = str('book:' + s)
        print('\nSearching Books: \n')
        search_url.url_search(q)


    elif ch == 4:
        s = input('SEARCH SONGS/ARTISTS: ')
        q = str('?intitle:index.of?mp3 ' + s)
        print('\nSearching Songs: \n')
        search_url.url_search(q)


    elif ch == 5:
        info.information()


    elif ch == 6:
        hacking_menu()
        if ch6 == 1:
            wp.wordpress()

        elif ch6 == 2:
            q = str('filetype:ini “wordfence”')
            print('\nSearching... \n')
            search_url.url_search(q)

        elif ch6 == 3:
            up.userpass()

        elif ch6 == 4:
            cam.cameras()

        elif ch6 == 5:
            q = str('inurl:/proc/self/cwd')
            print('\nSearching... \n')
            search_url.url_search(q)

        elif ch6 == 6:
            q = str('allintext:username filetype:log')
            print('\nSearching... \n')
            search_url.url_search(q)

        elif ch6 == 7:
            ftp.ftp()

        else:
            print('INVALID OPTION : ')
            sys.exit()



    else:
        print('INVALID OPTION! \n EXITING ')
        sys.exit()


if args['search'] is not None:
    logo.dorkify_logo()
    search_url.url_search(args['search'])

if args['book'] is not None:
    logo.dorkify_logo()
    q = str('book:' + args['book'])
    search_url.url_search(q)

if args['intitle'] is not None:
    logo.dorkify_logo()
    q = str('intitle:' + args['intitle'])
    search_url.url_search(q)

if args['inurl'] is not None:
    logo.dorkify_logo()
    q = str('inurl:' + args['inurl'])
    search_url.url_search(q)

if args['site'] is not None:
    logo.dorkify_logo()
    q = str('site:' + args['site'])
    search_url.url_search(q)

if args['music'] is not None:
    logo.dorkify_logo()
    q = str('?intitle:index.of?mp3 ' + args['music'])
    search_url.url_search(q)

if args['stocks'] is not None:
    logo.dorkify_logo()
    q = str('stocks' + args['stocks'])
    search_url.url_search(q)

if args['maps'] is not None:
    logo.dorkify_logo()
    q = str('maps' + args['maps'])
    search_url.url_search(q)

if args['weather'] is not None:
    logo.dorkify_logo()
    q = str('weather' + args['weather'])
    search_url.url_search(q)

if args['info'] is not None:
    logo.dorkify_logo()
    q = str('info' + args['info'])
    search_url.url_search(q)

if args['define'] is not None:
    logo.dorkify_logo()
    q = str('define' + args['define'])
    search_url.url_search(q)