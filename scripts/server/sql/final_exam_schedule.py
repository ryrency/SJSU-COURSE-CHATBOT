from utils import *
from course import *
from course_section import *
import json

def get_final_exam_schedule(text):
    course = get_course(text)
    if not course:
        return "Sorry no matching courses found. valid courses are: " + str(get_all_course_names())

    (course_section, text) = get_course_section(text, course)
    if not course_section:
        return "Sorry no matching section found for " + course['name']
    
    course_section_name = course['name'] + "-" + str(course_section['section_no'])
    final_exam_schedules = _get_final_exam_schedules(course_section['id'])

    if not final_exam_schedules or len(final_exam_schedules) <= 0:
        return "Sorry no final_exam schedules found for " + course_section_name
    else:
        return course_section_name + " final exam will be held on " + str(final_exam_schedules[0]['due_date'])
        
def _get_final_exam_schedules(course_section_id):
    #get instructor now
    connection = get_mysql_connection()

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM course_schedules WHERE course_section_id = " + str(course_section_id) + " AND activity_type = 4"
            cursor.execute(sql)
            final_exam_schedules = cursor.fetchall()

            return final_exam_schedules
    finally:
        connection.close()

    return None