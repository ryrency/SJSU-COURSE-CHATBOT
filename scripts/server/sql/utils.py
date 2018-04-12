import re
import pymysql.cursors
import json, datetime, os
from pattern.en import singularize

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)

def extract_digits(text):
    return str(filter(str.isdigit, text))

def get_mysql_connection():
    # connection = pymysql.connect(host='localhost',
    #                          user='root',
    #                          password='',
    #                          db='slackbot',
    #                          cursorclass=pymysql.cursors.DictCursor)
    # return connection
    connection = pymysql.connect(host=os.environ['DB_HOST'],
                             user=os.environ['DB_USER'],
                             password=os.environ['DB_PASS'],
                             db='slackbot',
                             cursorclass=pymysql.cursors.DictCursor)
    return connection

def get_sequence_number(text):
    if 'one' in text or 'first' in text or '1' in text:
        return 1
    elif 'two' in text or 'second' in text or '2' in text:
        return 2
    elif 'three' in text or 'third' in text or '3' in text:
        return 3
    elif 'four' in text or 'fourth' in text or '4' in text:
        return 4
    elif 'five' in text or 'fifth' in text or '5' in text:
        return 5
    elif 'six' in text or 'sixth' in text or '6' in text:
        return 6
    elif 'seven' in text or 'seventh' in text or '7' in text:
        return 7
    elif 'eight' in text or 'eighth' in text or '8' in text:
        return 8
    elif 'nine' in text or 'ninth' in text or '9' in text:
        return 9
    else:
        return -1

def map_words_to_digits_in_text(text):
    words = text.split(" ")
    mapped_words = []
    for word in words:
        mapped_words.append(map_word_to_digit(word))

    return " ".join(mapped_words)

def map_word_to_digit(word):
    if word == 'zero' or word == 'zeroth':
        return "0"
    if word == 'one' or word == 'first':
        return "1"
    if word == 'two' or word == 'second':
        return "2"
    if word == 'three' or word == 'third':
        return "3"
    if word == 'four' or word == 'fourth':
        return "4"
    if word == 'five' or word == 'fifth':
        return "5"
    if word == 'six' or word == 'sixth':
        return "6"
    if word == 'seven' or word == 'seventh':
        return "7"
    if word == 'eight' or word == 'eighth':
        return "8"
    if word == 'nine' or word == 'ninth':
        return "9"
    return word

def singularize_words(text):
    words = text.split(" ")
    mapped_words = []
    for word in words:
        if word == 'class':
            # singularize wrongly singularizes class to clas
            mapped_words.append(word)
        else:
            mapped_words.append(singularize(word))

    return " ".join(mapped_words)


