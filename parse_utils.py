from bs4 import BeautifulSoup

from course import Course
from constants import *


def parse_data( data ):

    # Parse the HTML
    soup = BeautifulSoup( data, 'lxml' )

    # Find the table with all the course data
    gdp_table = soup.find("table", attrs={"class": "tbrdr"})
    gdp_table_data = gdp_table.find_all("tr")

    # Unused for now
    """
    restrictions_idx = 0
    course_no_idx = 0
    section_id_idx = 0
    meeting_type_idx = 0
    days_idx = 0
    times_idx = 0
    room_idx = 0
    instructor_idx = 0
    available_idx = 0
    limit_idx = 0
    pre_reqs = ""
    """

    curr_dept = ""
    curr_course = None
    all_courses = []

    RESTRICTION_IDX = 0
    COURSE_NO_IDX = 1
    COURSE_NAME_IDX = 2

    CLASS_TYPE_IDX = 7 #col 8
    INSTRUCTOR_IDX = 9 #col 10
    FREE_SEATS_IDX = 10 #col 11
    LIMIT_IDX = 11 #col 12

    # Go through each table of course info
    for i, row in enumerate( gdp_table_data ):

        title = False
        # If there's a h2 AND a span class="centeralign" in the td, it's got
        # the dept acronym
        for td in row.find_all( "td" ):
            if td.find( "h2" ) and ("(" in td.find( "h2" ).text):
                s = td.text.strip()
                curr_dept = s[s.find("(")+1:s.find(")")].strip()
                title = True
                break

        if title == True:
            continue

        # Headings of a table
        # Unused for now - I just hardcoded index values
        """
        table_headers = row.find_all( "td", attrs={"class": "ubrdr"} )
        if table_headers:
            print( "Found table headers!" )
            for td in table_headers:
                print( td.text.strip() )

            continue
        """

        # Course name and pre reqs
        course_headers = row.find_all( "td", attrs={"class": "crsheader"} )
        if course_headers:
            parsed_headers = []
            for td in course_headers:
                tmp = td.text.strip().split("\t")
                # Get rid of empty strings and new lines
                tmp = [s.replace('\n', ' ').strip() for s in tmp if s != "" and s != "\n"]
                parsed_headers.append( " ".join(tmp) )

            # Should have (X Units) in their name
            name = parsed_headers[COURSE_NAME_IDX].split(" ( ")
            if len(name) > 1:
                name = name[0] + " (" + name[1]
                all_courses.append( Course( curr_dept, 
                                            parsed_headers[COURSE_NO_IDX],
                                            name,
                                            "https://www.google.com/",
                                            parsed_headers[RESTRICTION_IDX] ) )

            continue


        # Parse a section info
        if 'class' in row.attrs and len( row.attrs['class'] ) > 0:
            #and row.attrs['class'][0] == 'sectxt' )
            # nonenrtxt means final info

            section_info = row.find_all( "td", attrs={"class": "brdr"} )
            curr_course = all_courses[-1]

            curr_length = len( section_info )
            i = 0
            while i < curr_length:

                # This is a nasty calculation but it's because some rows have less tds
                # than others, so this keeps the table grid-like without "merged cells"
                td = section_info[i - (curr_length - len( section_info ))]
                if 'colspan' in td.attrs and len( td.attrs['colspan'] ) > 0:
                    colspan = int( td.attrs['colspan'][0] )
                    i += colspan
                    curr_length += colspan - 1
                    continue

                if i == CLASS_TYPE_IDX:
                    curr_course.update_type( td.text.strip() )

                if i == INSTRUCTOR_IDX:
                    curr_course.update_instructor( td.text.strip() )

                # It's either a number or FULL Waitlist(#)
                if i == FREE_SEATS_IDX:
                    seats = td.text.strip()
                    if seats != "":
                        if seats.isdigit():
                            curr_course.update_available_seats( 
                                        curr_course.get_available_seats() + int(seats) )
                        elif "FULL" in seats:
                            seats = seats[seats.find("(")+1:seats.find(")")]
                            curr_course.update_waitlist(
                                        curr_course.get_waitlist() + int(seats) )
                            curr_course.update_available_seats( 0 )

                if i == LIMIT_IDX:
                    seats = td.text.strip()
                    if seats != "" and seats.isdigit():
                        curr_course.update_limit( curr_course.get_limit() + int(seats) )

                i += 1
            # End while

    return soup, all_courses

