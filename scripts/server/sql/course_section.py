from utils import *
from course import *

last_course_section_in_context = None

import re

def get_course_section(text, course):
    global last_course_section_in_context
    connection = get_mysql_connection()

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM course_sections where course_id = " + str(course['id'])
            cursor.execute(sql)
            course_sections = cursor.fetchall()

            course_name = course['name']
            # extract digits from course name
            course_number = extract_digits(course_name)
            for course_section in course_sections:
                regex = course_number + "([0_.\- ]|section|sec)*" + str(course_section["section_no"]) + "($| )"
                p = re.compile(regex)
                m = p.search(text)
                if m:
                    last_course_section_in_context = course_section
                    return (course_section, text.replace(m.group(0), ""))

            if last_course_section_in_context:
                return last_course_section_in_context, text
    finally:
        connection.close()

    return (None, None)


def get_course_section_details(course_section_id):
    connection = get_mysql_connection()

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM course_section_details where course_section_id = " + str(course_section_id)
            cursor.execute(sql)
            course_section_details = cursor.fetchall()

            if len(course_section_details) > 0:
                return course_section_details[0]
    finally:
        connection.close()

    return None

