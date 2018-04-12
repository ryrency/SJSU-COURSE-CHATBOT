import os
import subprocess
import random

train_test_split_factor = 0.8
jsgfs_dir = './jsgfs'
raw_data_dir = "./data/raw"
train_data_dir = "./data/train"
test_data_dir = "./data/test"

jsgf_parser = "./scripts/JSGFTools/DeterministicGenerator.py"

def generate_train_test_data(filename):
    # split raw data into train/test
    raw_file_path = raw_data_dir + "/" + filename

    with open(raw_file_path, "rb") as f:
        data = f.read().split('\n')

    f.close()

    if len(data) <= 1:
        return

    random.shuffle(data)

    train_data_len = int(len(data) * train_test_split_factor)
    test_data_len = len(data) - train_data_len

    train_data = data[:train_data_len]
    test_data = data[-test_data_len:]

    test_file = test_data_dir + "/" + filename
    train_file = train_data_dir + "/" + filename

    # write test data file
    test_f= open(test_file, 'w')
    for item in test_data:
        test_f.write("%s\n" % item)
    test_f.close()

    #write train data file
    train_f= open(train_file, 'w')
    for item in train_data:
        train_f.write("%s\n" % item)
    train_f.close()

def clear_dir(dir):
    command = "rm -f " + dir + "/*"
    subprocess.call(command, shell=True)

#clean up raw, test, and train dirs
clear_dir(raw_data_dir)
clear_dir(train_data_dir)
clear_dir(test_data_dir)

# inflate jsgfs into raw folder
for  filename in os.listdir(jsgfs_dir):
    out_filename = filename.replace(".jsgf", ".txt")

    jsgf_file_path = jsgfs_dir + '/' + filename
    raw_file_path = raw_data_dir + "/" + out_filename

    command = "python " + jsgf_parser + " " + jsgf_file_path + " > " + raw_file_path
    process = subprocess.call(command, shell=True)
    generate_train_test_data(out_filename)

       

                
#print(os.getcwd())
