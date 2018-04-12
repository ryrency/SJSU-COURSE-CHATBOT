from utils import *
from course import *
from course_section import *
import json

def get_learning_objectives(text):
    course = get_course(text)
    if not course:
        return "Sorry no matching courses found. valid courses are: " + str(get_all_course_names())

    (course_section, text) = get_course_section(text, course)
    if not course_section:
        return "Sorry no matching section found for " + course['name']

    course_section_name = course['name'] + "-" + str(course_section['section_no'])

    learning_objectives = _get_learning_objectives(course_section['id'])

    if not learning_objectives or len(learning_objectives) <= 0:
        return "Sorry no objectives found for " + course_section_name
    else:
        response = []
        for l_o in learning_objectives:
            response.append(l_o['description'])

        return "Here are the learning objectives for " + course_section_name + ": " + json.dumps(response, cls=DateTimeEncoder)



def _get_learning_objectives(course_section_id):
    #get instructor now
    connection = get_mysql_connection()

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM learning_objectives where course_section_id = " + str(course_section_id)
            cursor.execute(sql)
            program_outcomes = cursor.fetchall()

            return program_outcomes
    finally:
        connection.close()

    return None