<p align=center>

  <img src="https://raw.githubusercontent.com/hhhrrrttt222111/Dorkify/master/media/dorkify.png" style="border-radius:10px;"/>

  <br>
  <span>Perform Google Dork search with <b><i>Dorkify</i></b></span>
  <br><br>
    <a href="https://github.com/hhhrrrttt222111/Dorkify/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/hhhrrrttt222111/Dorkify"></a>
  <a href="https://github.com/hhhrrrttt222111/Dorkify/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/hhhrrrttt222111/Dorkify?color=orange"></a>
  <a href="https://github.com/hhhrrrttt222111/Dorkify/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/hhhrrrttt222111/Dorkify?color=red"></a>
  <a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.7-blue.svg"></a>
</p>


<br>

## Google Dorking

Google dorking is a hacker technique that uses Google Search to find security holes in the configuration and computer code that websites use. Google Dorking involves using advanced operators in the Google search engine to locate specific strings of text within search results such as finding specific versions of vulnerable Web applications. Users can utilize commands to get other specific search results.

<br>

### MENU  :page_with_curl:

* Google Search
* URL Search
* Books
* Music Downloads
* Information
* Dork Hacks!

## Features
  Dorkify can :
  - Perfom a (Google/URL) search
  - Find specific link with keywords in URL/Title/Website
  - Search for Books
  - Extract mp3/mp4 download links
  - Perform deep scan on definitions and informations
  - Get details on Stocks/Maps/Weather
  - Find vulnerable Wordpress sites
  - Search for Usernames and Password list
  - Find vulnerable Web servers
  - Find vulnerable CCTV's
  - Find open FTP Servers


#### More features with stronger results will come out in v 2.21

## INSTALLATION
**Python 3.6 or higher is required**  :snake:

```bash
git clone https://github.com/hhhrrrttt222111/Dorkify.git

cd Dorkify

python3 -m pip install -r requirements.txt
```

## USAGE

```bash
python3 dorkify.py --help
usage: dorkify.py [-h]
                  [--cli | --wp | --up | --cam |
                  --ftp |  -v | -s SEARCH | 
                  -b BOOK | -mu MUSIC | -m MAPS | 
                  -w WEATHER | -i INFO | -d DEFINE | 
                  -st STOCKS | --intitle INTITLE | 
                  --inurl INURL | --site SITE]

optional arguments:
  -h, --help            show this help message and exit
  --cli                 Run the Command Line version of Dorkify
  --wp                  WordPress sites vulnerabilities
  --up                  Find vulnerable Usernames and Passwords
  --cam                 Find vulnerable CCTV cameras
  --ftp                 Find open FTP Servers
  -v, --version         Version
  -s SEARCH, --search SEARCH
                        Do a Google search
  -b BOOK, --book BOOK  Search for a book or author
  -mu MUSIC, --music MUSIC
                        Search for songs or artists
  -m MAPS, --maps MAPS  Find maps of a city
  -w WEATHER, --weather WEATHER
                        Check weather of a city
  -i INFO, --info INFO  Get Information
  -d DEFINE, --define DEFINE
                        Define a term
  -st STOCKS, --stocks STOCKS
                        Search for Stock of a company with Ticker value
  --intitle INTITLE     Search for a keywords in website title
  --inurl INURL         Search for a keywords in website URL
  --site SITE           Search for a Site

```

### Run Dorkify
```bash
python3 dorkify.py --cli
```

<br>

## License  :heavy_check_mark:

[MIT Licence](https://github.com/hhhrrrttt222111/Dorkify/blob/master/LICENSE)



