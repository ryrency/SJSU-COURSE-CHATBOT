from utils import *
from course import *
from course_section import *
import json

def get_program_outcomes(text):
    course = get_course(text)
    if not course:
        return "Sorry no matching courses found. valid courses are: " + str(get_all_course_names())

    (course_section, text) = get_course_section(text, course)
    if not course_section:
        return "Sorry no matching section found for " + course['name']

    course_section_name = course['name'] + "-" + str(course_section['section_no'])

    program_outcomes = _get_program_outcomes(course_section['id'])
    if not program_outcomes or len(program_outcomes) <= 0:
        return "Sorry no program outcomes found for " + course_section_name
    else:
        response = []
        for p_o in program_outcomes:
            response.append(p_o['description'])

        return "Here are the program outcomes for " + course_section_name + ':' + json.dumps(response, cls=DateTimeEncoder)


def _get_program_outcomes(course_section_id):
    #get instructor now
    connection = get_mysql_connection()

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM program_outcomes where course_section_id = " + str(course_section_id)
            cursor.execute(sql)
            program_outcomes = cursor.fetchall()

            return program_outcomes
    finally:
        connection.close()

    return None