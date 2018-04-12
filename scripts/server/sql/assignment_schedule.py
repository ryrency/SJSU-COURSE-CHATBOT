from utils import *
from course import *
from course_section import *
import json

def get_assignment_schedule(text):
    course = get_course(text)
    if not course:
        return "Sorry no matching courses found. valid courses are: " + str(get_all_course_names())

    (course_section, text) = get_course_section(text, course)
    if not course_section:
        return "Sorry no matching section found for " + course['name']

    course_section_name = course['name'] + "-" + str(course_section['section_no'])
    assignment_schedules = _get_assignment_schedules(course_section['id'])

    if not assignment_schedules or len(assignment_schedules) <= 0:
        return "Sorry no assignment schedules found for " + course_section_name
    else:
        seq_no = get_sequence_number(text)
        if seq_no > 0 and seq_no <= len(assignment_schedules):
            due_date = str(assignment_schedules[seq_no - 1]['due_date'])
            activity = assignment_schedules[seq_no - 1]['activity']
            return course_section_name + " " + activity + " is due at " + due_date
        else:
            all_assignments_schedule = {}
            for l_s in assignment_schedules:
                all_assignments_schedule[l_s['activity']] = l_s['due_date']
            
            return "Sorry, don't know which assignment schedule you're looking for. But here is a schedule for all assignments of " + course_section_name + ": " + json.dumps(all_assignments_schedule, cls=DateTimeEncoder)


def _get_assignment_schedules(course_section_id):
    #get instructor now
    connection = get_mysql_connection()

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM course_schedules WHERE course_section_id = " + str(course_section_id) + " AND activity_type = 1"
            cursor.execute(sql)
            assignment_schedules = cursor.fetchall()

            return assignment_schedules
    finally:
        connection.close()

    return None