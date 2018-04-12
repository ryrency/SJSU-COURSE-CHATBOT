#!/usr/bin/env python3
import os
import time
from slackclient import SlackClient
import sys

import speech_recognition as sr
import json

from gtts import gTTS


sys.path.append('./scripts/classifier')
sys.path.append('./scripts/server/sql')
from classifier import Classifier
import utils, course, course_section, program_outcomes, learning_objectives, lab_schedule, \
    assignment_schedule, greeting, project_schedule, mid_term_schedule, final_exam_schedule, \
    course_grading, course_name, class_location, course_prereq, course_timings, course_website, \
    instructor_contact, instructor_email, instructor_name, instructor_office_hours, instructor_office_location, \
    instructor_phone, university_policy , reference_materials


# jarvis's ID as an environment variable
BOT_ID = 'U55PR6EK1'
SLACK_BOT_TOKEN = 'xoxb-175807218647-HL9jcD2OAzBxgj5G0QBrwcfX'

# constants
AT_BOT = "<@" + BOT_ID + ">"

# instantiate slack
slack_client = SlackClient(SLACK_BOT_TOKEN)

channel = None
flag = 0
voice_text = None


#instantiate classifier
txt_clf = Classifier()

def reset():
    course.last_course_in_context = None
    course_section.last_course_section_in_context = None


def _get_answer(text):
    text = text.lower()
    text = utils.map_words_to_digits_in_text(text)
    text = utils.singularize_words(text)
    label = txt_clf.classify(text)

    if label == 'hello':
		return greeting.get_greeting(text)
    if label == 'bye':
        return greeting.get_goodbye(text)
    if label == 'instructor_contact':
        return instructor_contact.get_contact(text)
    if label == 'instructor_email':
        return instructor_email.get_email(text)
    if label == 'instructor_name':
        return instructor_name.get_name(text)
    if label == 'instructor_office_hours':
        return instructor_office_hours.get_hours(text)
    if label == 'instructor_office_location':
        return instructor_office_location.get_location(text)
    if label == 'instructor_phone':
        return instructor_phone.get_phone(text)
    elif label == 'course_name':
        return course_name.get_description(text)
    elif label == 'course_prereq':
        return course_prereq.get_prereq(text)
    elif label == 'course_timings':
        return course_timings.get_timings(text)
    elif label == 'course_website':
        return course_website.get_url(text)
    elif label == 'class_location':
        return class_location.get_location(text)
    elif label == 'course_learning_objectives':
        return learning_objectives.get_learning_objectives(text)
    elif label == 'program_outcome':
        return program_outcomes.get_program_outcomes(text)
    elif label == 'lab_schedule':
        return lab_schedule.get_lab_schedule(text)
    elif label == 'assignment_schedule':
        return assignment_schedule.get_assignment_schedule(text)
    elif label == 'project_schedule':
        return project_schedule.get_project_schedule(text)
    elif label == 'mid_term_schedule':
        return mid_term_schedule.get_mid_term_schedule(text)
    elif label == 'final_exam_schedule':
        return final_exam_schedule.get_final_exam_schedule(text)
    elif label == 'course_grading':
        return course_grading.get_course_grading_details(text)
    elif label == 'university_policy':
        return university_policy.get_university_policy(text)
    elif label == 'reference_materials':
        return reference_materials.get_reference_material(text)
    else:
        return label


def handle_command(command, channel):
    response = _get_answer(command)
    slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

    tts = gTTS(text=response, lang='en')
    tts.save("pcvoice.mp3")
    # this is for linux
    os.system("mpg321 pcvoice.mp3")

    response5 = "Enter \"voice\" if you want to speak up your question."
    slack_client.api_call("chat.postMessage", channel=channel, text=response5, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    channel = None
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:

                if flag==0:
                    print "flag is 0"
                    val_comm, val_cha = parse_slack_output(slack_client.rtm_read())
                    command = val_comm
                    channel = val_cha
                    if command == "voice":
                        flag = 1
                        r = sr.Recognizer()
                        r.energy_threshold = 300
                        r.pause_threshold = 0.8




                        try:
                            with sr.Microphone() as source:
                                print("Say something!")
                                response1 = "Jarvis is listening... Say something!"
                                slack_client.api_call("chat.postMessage", channel=channel, text=response1, as_user=True)
                                audio = r.listen(source)
                            print("Jarvis thinks you said " + r.recognize_google(audio))
                            response4 = "Jarvis thinks you said " + r.recognize_google(audio)
                            slack_client.api_call("chat.postMessage", channel=channel, text=response4, as_user=True)

                        except sr.UnknownValueError:
                            print("Jarvis could not understand audio. Please type your question or try saying again!")
                            response4 = "Jarvis could not understand audio. Please type your question or try saying again!"
                            slack_client.api_call("chat.postMessage", channel=channel, text=response4, as_user=True)
                            break

                        except sr.RequestError as e:
                            print("request could not reach Jarvis; {0}".format(e))
                            response4 = "Your request could not reach Jarvis!; {0}".format(e)
                            slack_client.api_call("chat.postMessage", channel=channel, text=response4, as_user=True)
                            break

                        if r.recognize_google(audio):
                            voice_text = r.recognize_google(audio)
                            command = voice_text
                            print "voice_text"
                            print voice_text
                            channel = val_cha
                            flag = 0

                if command == 'reset':
                    reset()

                if command:
                    print "flag"
                    print flag
                    print "command "
                    print command
                    print "channel"
                    print channel
                    handle_command(command, channel)

                time.sleep(READ_WEBSOCKET_DELAY)

    else:
        print("Connection failed. Invalid Slack token or bot ID?")
