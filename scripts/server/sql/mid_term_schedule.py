from utils import *
from course import *
from course_section import *
import json

def get_mid_term_schedule(text):
    course = get_course(text)
    if not course:
        return "Sorry no matching courses found. valid courses are: " + str(get_all_course_names())

    (course_section, text) = get_course_section(text, course)
    if not course_section:
        return "Sorry no matching section found for " + course['name']
    
    course_section_name = course['name'] + "-" + str(course_section['section_no'])
    mid_term_schedules = _get_mid_term_schedules(course_section['id'])

    if not mid_term_schedules or len(mid_term_schedules) <= 0:
        return "Sorry no mid_term schedules found for " + course_section_name
    else:
        return course_section_name + " mid term exam will be held on " + str(mid_term_schedules[0]['due_date'])
        
def _get_mid_term_schedules(course_section_id):
    #get instructor now
    connection = get_mysql_connection()

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM course_schedules WHERE course_section_id = " + str(course_section_id) + " AND activity_type = 3"
            cursor.execute(sql)
            mid_term_schedules = cursor.fetchall()

            return mid_term_schedules
    finally:
        connection.close()

    return None