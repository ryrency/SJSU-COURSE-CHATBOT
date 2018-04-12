import json
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.externals import joblib
import sys

class Classifier():
    def __init__(self):
        model_file = "./models/clf.model"
        categories_file = "./models/categories.txt"

        # load target name
        with open(categories_file,'r') as f:
            self.target_names = json.load(f)

        #load classifier
        self.txt_clf = joblib.load(model_file)

    def classify(self, text):
        predicted = self.txt_clf.predict([text])
        return self.target_names[predicted[0]]


if __name__ == '__main__':
    clf = Classifier()
    print(clf.classify(sys.argv[1]))