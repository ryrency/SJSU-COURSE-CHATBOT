from utils import *
from course import *
from course_section import *
import json

def get_lab_schedule(text):
    course = get_course(text)
    if not course:
        return "Sorry no matching courses found. valid courses are: " + str(get_all_course_names())

    (course_section, text) = get_course_section(text, course)
    if not course_section:
        return "Sorry no matching section found for " + course['name']
    course_section_name = course['name'] + "-" + str(course_section['section_no'])

    lab_schedules = _get_lab_schedules(course_section['id'])
    #print(lab_schedules)

    if not lab_schedules or len(lab_schedules) <= 0:
        return "Sorry no lab schedules found for " + course_section_name
    else:
        seq_no = get_sequence_number(text)
        if seq_no > 0 and seq_no <= len(lab_schedules):
            due_date = str(lab_schedules[seq_no - 1]['due_date'])
            activity = lab_schedules[seq_no - 1]['activity']
            return course_section_name + " " + activity + " is due at " + due_date
        else:
            all_labs_schedule = {}
            for l_s in lab_schedules:
                all_labs_schedule[l_s['activity']] = l_s['due_date']

            return "Sorry, don't know which lab schedule you're looking for. But here is a schedule for all labs of " + course_section_name + ": " + json.dumps(all_labs_schedule, cls=DateTimeEncoder)


def _get_lab_schedules(course_section_id):
    #get instructor now
    connection = get_mysql_connection()

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM course_schedules WHERE course_section_id = " + str(course_section_id) + " AND activity_type = 0"
            cursor.execute(sql)
            lab_schedules = cursor.fetchall()

            return lab_schedules
    finally:
        connection.close()

    return None