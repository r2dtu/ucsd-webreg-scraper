# ucsd_scrape_webreg
Command-line web scraper: scrapes UCSD's schedule of classes and filters based on user input

This program can be run as follows (requires Python 3.7+):
(this message is same as running the program with the -h or --help flag)

usage: scrape_webreg.py [-h] [--dept CSE [CSE ...]] [--available] [--remote]
                        [--in_person] [--hybrid] [--all_types]
                        [--files cse_.html [cse_.html ...]]
                        QTR

Process scraping params.

positional arguments:

  QTR                   what academic quarter to search in: FA20,WI21,etc.

optional arguments:

  -h, --help            show this help message and exit
  
  --dept CSE [CSE ...]  1 or more departments to search in
  
  --available           show classes with available seats only
  
  --remote              show only remote classes
  
  --in_person           show only in-person classes
  
  --hybrid              show only hybrid classes
  
  --all_types           show all types of classes - this is ON by default
  
  --files cse_.html [cse_.html ...]
                        1 or more files with info to parse (typically the
                        output HTML of this program - MAKE SURE TO PUT QUOTES
                        AROUND FILENAMES WITH SPECIAL CHARACTERS
