from utils import *
from course import *
from course_section import *
import json

def get_course_grading_details(text):
    course = get_course(text)
    if not course:
        return "Sorry no matching courses found. valid courses are: " + str(get_all_course_names())

    (course_section, text) = get_course_section(text, course)
    if not course_section:
        return "Sorry no matching section found for " + course['name']

    course_section_name = course['name'] + "-" + str(course_section['section_no'])

    course_weights = _get_course_weights(course_section['id'])
    if not course_weights or len(course_weights) <= 0:
        return "Sorry no grading details found for " + course_section_name
    else:
        activity_type = _get_activity_type(text)

        if activity_type >= 0:
            for c_w in course_weights:
                if c_w['activity_type'] == activity_type:
                    return "As per the grading policy of " + course_section_name + ", the weightage for " + c_w['activity'].lower() + " will be " + c_w['weight']

            # if no matching activity found, return the grading policy for course
            weights = {}
            for c_w in course_weights:
                weights[c_w['activity']] = c_w['weight']

            return "Here is the grading policy for the course " + course_section_name + ": " + json.dumps(weights, cls=DateTimeEncoder)
        else:
            # if no matching activity found, return the grading policy for course
            weights = {}
            for c_w in course_weights:
                weights[c_w['activity']] = c_w['weight']

            return "Here is the grading policy for the course " + course_section_name + ": " + json.dumps(weights, cls=DateTimeEncoder)

def _get_course_weights(course_section_id):
    connection = get_mysql_connection()

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM course_grading where course_section_id = " + str(course_section_id)
            cursor.execute(sql)
            course_weights = cursor.fetchall()

            return course_weights
    finally:
        connection.close()

    return None

def _get_activity_type(text):
    if 'quiz' in text:
        return 0
    elif 'lab' in text:
        return 1
    elif 'assignment' in text:
        return 2
    elif 'project' in text:
        return 3
    elif 'mid' in text:
        return 4
    elif 'final' in text:
        return 5
    else:
        return -1