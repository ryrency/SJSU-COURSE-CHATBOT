from utils import *
import json

def get_university_policy(text):
    university_policy = _get_university_policies()
    if not university_policy or len(university_policy) <= 0:
        return "Sorry no university policies found "

    else:
        response = []
        for u_p in university_policy:
            response.append(u_p['description'])

        return "Here are the university policies: " + json.dumps(response, ensure_ascii=False)

def _get_university_policies():

    connection = get_mysql_connection()

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM university_policy"
            cursor.execute(sql)
            university_policies = cursor.fetchall()

            return university_policies
    finally:
        connection.close()

    return None