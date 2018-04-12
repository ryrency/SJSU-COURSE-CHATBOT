from course import *
from course_section import *

def get_description(text):
    course = get_course(text)
    if not course:
        return "Sorry no matching courses found. valid courses are: " + str(get_all_course_names())

    # just calling the get_course_function so that we can remember the course section from text
    (course_section, text) = get_course_section(text, course)

    return course['name'] + " is about " + course['description']