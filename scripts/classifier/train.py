import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.externals import joblib
import json
from sklearn.linear_model import SGDClassifier

train_dir = "./data/train"
test_dir = "./data/test"
model_file = "./models/clf.model"
categories_file = "./models/categories.txt"
train_data = []
train_targets = []
target_names = []
test_data = []
test_targets = []

for filename in os.listdir(train_dir):
    target_name = filename.replace(".txt" , "")
    target_names.append(target_name)
    target_index = len(target_names) - 1

    with open(train_dir + '/' + filename, "rb") as f:
        lines = f.read().split('\n')
        for line in lines:
            train_data.append(line)
            train_targets.append(target_index)

for filename in os.listdir(test_dir):
    target_name = filename.replace(".txt" , "")
    target_index = target_names.index(target_name)

    with open(test_dir + '/' + filename, "rb") as f:
        lines = f.read().split('\n')
        for line in lines:
            test_data.append(line)
            test_targets.append(target_index)

text_clf = Pipeline([('vect', CountVectorizer(min_df = 0)),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5, random_state=42))])
text_clf = text_clf.fit(train_data,train_targets)

predicted = text_clf.predict(test_data)
print("Accuracy on test set: ")
print(np.mean(predicted == test_targets))

# dump trained models to file
joblib.dump(text_clf, model_file)

#dump categories
with open(categories_file, 'w') as outfile:
    json.dump(target_names, outfile)





