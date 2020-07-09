from enum import IntEnum

from constants import *

class ClassType(IntEnum):
    TBA = -1
    IN_PERSON = 0
    REMOTE_ONLY = 1
    HYBRID = 2

def convert_str_to_type( new_type ):
    if new_type == 'RCLAS':
        return ClassType.REMOTE_ONLY
    if new_type == 'TBA':
        return ClassType.TBA
    return ClassType.IN_PERSON

def convert_type_to_str( class_type ):
    if class_type == ClassType.IN_PERSON:
        return "IN PERSON ONLY"
    elif class_type == ClassType.REMOTE_ONLY:
        return "REMOTE ONLY"
    elif class_type == ClassType.HYBRID:
        return "HYBRID"
    return "TBA"


class Course():

    def __init__( self, dept, course_no, name, link, restrict ):
        self._dept = dept
        self._c_no = course_no
        self._name = name
        self._link = link
        self._restrict = restrict
        self._free_count = -1
        self._waitlist = -1
        self._limit = -1
        self._type = ClassType.TBA
        self._days_time = ""
        self._instructor = ""

    def get_type( self ):
        return self._type

    def update_type( self, new_type ):
        class_type = convert_str_to_type( new_type )
        if class_type == ClassType.TBA:
            return

        if self._type == ClassType.TBA:
            self._type = class_type
        else:
            if self._type != class_type:
                self._type = ClassType.HYBRID

    def get_available_seats( self ):
        if self._free_count == -1:
            self._free_count = 0
        return self._free_count

    def update_available_seats( self, new_free_count ):
#        print( "New free seat count: %d, overriding %s" % (new_free_count, self._type) )
        if self._free_count == -1:
            self._free_count = 0
        self._free_count = new_free_count

    def get_limit( self ):
        if self._limit == -1:
            self._limit = 0
        return self._limit

    def update_limit( self, new_limit ):
        if self._limit == -1:
            self._limit = 0
        self._limit = new_limit

    def get_waitlist( self ):
        if self._waitlist == -1:
            self._waitlist = 0
        return self._waitlist

    def update_waitlist( self, new_waitlist ):
        if self._waitlist == -1:
            self._waitlist = 0
        self._waitlist = new_waitlist

    def update_days_time( self, new_days_time ):
        self._days_time = new_days_time

    def update_instructor( self, new_instructor ):
        if self._instructor == "":
            self._instructor = new_instructor

    def __str__( self ):
        return "%s %s: %s, Restrict: %s, Instructor:%s\n\t\tType: %s, Available Seats: %d,"\
                " Limit: %d\n" %\
                (self._dept, self._c_no, self._name, self._restrict, self._instructor,
                convert_type_to_str( self._type ), self._free_count, self._limit)


def find_available_courses( all_courses ):
    available_courses = []
    for course in all_courses:
        if course.get_available_seats() > 0:
            available_courses.append( course )

    return available_courses

def print_courses( all_courses, view_mode ):
    for course in all_courses:
        if course.get_type() == ClassType.IN_PERSON and\
            (view_mode & VIEW_IN_PERSON_BIT) != 0:
            print( course )

        elif course.get_type() == ClassType.REMOTE_ONLY and\
            (view_mode & VIEW_REMOTE_BIT) != 0:
            print( course )

        elif course.get_type() == ClassType.HYBRID and\
            (view_mode & VIEW_HYBRID_BIT) != 0:
            print( course )

