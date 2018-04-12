from course import *
from course_section import *

def get_reference_material(text):
    course = get_course(text)
    if not course:
        return "Sorry no matching courses found. valid courses are: " + str(get_all_course_names())

    (course_section, text) = get_course_section(text, course)
    if not course_section:
        return "Sorry no matching section found for " + course['name']

    course_section_name = course['name'] + "-" + str(course_section['section_no'])

    course_section_details = get_course_section_details(course_section['id'])

    if not course_section_details:
        return "Sorry no reference material found for " + course_section_name

    return course_section_name + " references are " + course_section_details['reference_material']