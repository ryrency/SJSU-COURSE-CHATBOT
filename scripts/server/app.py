from flask import Flask,request
import sys
sys.path.append('./scripts/classifier')
sys.path.append('./scripts/server/sql')
from classifier import Classifier
import utils, instructor, course, program_outcomes, learning_objectives, lab_schedule, \
    assignment_schedule, project_schedule, mid_term_schedule, final_exam_schedule, \
    course_grading

txt_clf = Classifier()
app = Flask(__name__)

# http://localhost:5000/classify?text=who is doing it
@app.route("/classify")
def classify():
    text = request.args.get('text')
    text = text.lower()
    text = utils.map_words_to_digits_in_text(text)
    question_type = txt_clf.classify(text)
    return _return_response_for_question(text, question_type)

def _return_response_for_question(text, label):
        if label == 'instructor':
            return instructor.get_instructor_details(text)
        elif label == 'course_name':
            return course.get_course_details(text)
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
        else:
            return "Sorry I don't understand your question"

if __name__ == "__main__":
    app.run(debug=True,host='localhost')
