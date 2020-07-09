import urllib
import urllib.parse
import requests
from bs4 import BeautifulSoup

from course import find_available_courses, print_courses
from constants import *
from parse_utils import parse_data

def read_data_from_file( filename, available_only_flag, view_mode ):
    with open( filename, "r" ) as f:
        soup, all_courses = parse_data( f.read() )
        if available_only_flag:
            all_courses = find_available_courses( all_courses )
        print_courses( all_courses, view_mode )


def scrape_ucsd_webreg( query_params, extra_query_params, 
                        available_only_flag, view_mode ):
    data = urllib.parse.parse_qs( query_params + extra_query_params )
    resp = requests.post(SCHED_OF_CLASSES_URL, data).text

    # Just for testing/caching
    f = open( "cse_"+extra_query_params+".html", "w" )
    f.write(resp)
    f.close()

    soup, all_courses = parse_data( resp )

    if available_only_flag:
        all_courses = find_available_courses( all_courses )

    print_courses( all_courses, view_mode )

    # Finally, look for the Page (___ of ___).
    # If we need to request more, we will do that.
    footer_table = soup.find_all("table")[-1]
    table_data = footer_table.find_all("tr")
    # There should only be one row.. but just for formality
    for row in table_data:
        tds = row.find_all("td")
        tmp = tds[-1].text.split("\t")
        tmp = [s.replace('\n', ' ').strip() for s in tmp if s != "" and s != "\n"]
        tmp = [s for s in tmp if s != ""]
        tmp = tmp[0].replace(u'\xa0', u' ')
        page_str_list = tmp[tmp.find("(")+1:tmp.find(")")].split(' ')
        curr_page = int( page_str_list[0] )
        last_page = int( page_str_list[2] )

        if (curr_page != last_page):
            scrape_ucsd_webreg( query_params, "&page=" + str(curr_page + 1), 
                                available_only_flag, view_mode )

        break


# Sample usage of this program
# python scrape_webreg.py
#
#   QTR     FA20, WI21, etc.
#   --dept  space-separated list of departments to search for
#   --remote        online classes will be displayed
#   --in_person     in-person classes will be displayed
#   --hybrid        hybrid classes will be displayed
#   --all           all class types with given filters (this is same as running 
#                   --remote --in_person --hybrid
if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser(description='Process scraping params.')
    parser.add_argument('QTR', type=str,
                        help='what academic quarter to search in: FA20,WI21,etc.')
    parser.add_argument('--dept', metavar='CSE', type=str, nargs='+',
                        help='1 or more departments to search in')
    parser.add_argument('--available', action='store_true',
                        help='show classes with available seats only')
    parser.add_argument('--remote', action='store_true',
                        help='show only remote classes')
    parser.add_argument('--in_person', action='store_true',
                        help='show only in-person classes')
    parser.add_argument('--hybrid', action='store_true',
                        help='show only hybrid classes')
    parser.add_argument('--all_types', action='store_true',
                        help='show all types of classes - this is ON by default')
    parser.add_argument('--files', metavar='cse_.html', type=str, nargs='+',
                        help='1 or more files with info to parse (typically the '\
                        'output HTML of this program - MAKE SURE TO PUT QUOTES '\
                        'AROUND FILENAMES WITH SPECIAL CHARACTERS')
    args = parser.parse_args()

    query_params = "selectedTerm=" + args.QTR
    query_params += BROWSER_SETTINGS
    if args.dept:
        for dept in args.dept:
            if len(dept) < 4:
                dept += "+"
            query_params += "&selectedSubjects=" + dept
    else:
        query_params += DEFAULT_SUBJS

    view_mode = 0x0
    if args.remote:
        view_mode |= VIEW_REMOTE_BIT
    if args.in_person:
        view_mode |= VIEW_IN_PERSON_BIT
    if args.hybrid:
        view_mode |= VIEW_HYBRID_BIT

    # Set all if none are passed in
    if not args.remote and not args.in_person and not args.hybrid:
        view_mode = VIEW_REMOTE_BIT | VIEW_IN_PERSON_BIT | VIEW_HYBRID_BIT

    query_params += QUERY_PARAMS

    if args.files:
        for fname in args.files:
            read_data_from_file( fname, args.available, view_mode )
    else:
        scrape_ucsd_webreg( query_params, "", args.available, view_mode )

