# CMPE 273 Project - Team 8

# Slack API Chatbot

### Team Members:
Shefali Munjal, Rency Joseph, Narasa Kumar and Ritu Singh.

### Description: 

Using Slack channel as GUI for users, this chatbot uses Machine Learning models to answer user's questions and answers accurately. Our reference has been http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html.

### Advantages

#### Machine Learning
	The chatbot uses SVM Machine Learning algorithm in scikit library for classifying the questions. Our tests currently indicate an accuracy of around 98%.

#### Voice integration
	Users can use their laptop inbuilt microphone to ask chatbot as voice input. The server listens to microphone and processes in the server, replies back to slack channel. The server also converts the output response as voice and plays to user.

#### JSpeech Grammar Format
	The chatbot was trained by a model with questions were generated to JSpeech Grammar Format (JSGF).

	The JSpeech Grammar Format (JSGF) is a platform-independent, vendor-independent textual representation of grammars for use in speech recognition. 
	Grammars are used by speech recognizers to determine what the recognizer should listen for, and so describe the utterances a user may say. 
	JSGF adopts the style and conventions of the JavaTM Programming Language in addition to use of traditional grammar notations.

#### Conversational Bot
	Remembers the class, and user need not to specify course name each time. First time, the user asks any question, he needs to mention the course and section name. 
	Thereafter, the system remembers the context and he does not need to specify the same again unless he needs details for a different course/section. 

#### Support of more than one greensheet
	The input to this system is the greensheet data from MySQL database. User can train this system with any number of greensheets. 
	Currently the system has been trained for data from 2 greensheets -CMPE27301 and CMPE272-2.

#### Scalable
	The python server is deployed on EC2 and it is highly scalable. The database used was mySQL on Amazon RDS and is capable of serving millions of 
	requests concurrently.
	

### Required Libraries 
```json
sly
pymysql
slackclient
numpy
scipy
scikit-learn
pattern
```

#### Installation All above libraries with pip
```python
pip install sly pymysql slackclient numpy scipy scikit-learn pattern
```

or 

#### install python requirements (after cloning the git repo)
```python
pip install -r requirements.txt
```


#### set the following environments properly
The code uses database configuration from environment variables, make sure to add them
```bash
export DB_HOST='localhost'
export DB_USER=root
export DB_PASS=''
```

#### Set the slack bot id and token
```bash
export SLACK_BOT_TOKEN='xoxb-175807218647-HL9jcD2OAzBxgj5G0QBrwcfX'
export BOT_ID='U55PR6EK1'
```


#### Run the scripts to create database and push the required greensheet data to database
```bash
mysql -h $DB_HOST -u $DB_USER < scripts/sql/scripts.sql
mysql -h $DB_HOST -u $DB_USER < scripts/sql/insert.sql
```

#### Install libraries for voice based chat
##### 1. Packages to make bot listen:
```bash
pip install SpeechRecognition
sudo apt install linuxbrew-wrapper
brew install portaudio && sudo brew link portaudio
pip install pyaudio
```
			
##### 2. Packages to make bot talk:
```bash
sudo pip install gtts
sudo apt-get install mpg321
brew install portaudio && sudo brew link 
```

### Run the chatbot server

```python
python scripts/server/jarvis.py
```

Now, the chatbot is active and add the slack bot to any slack channel. To invoke the chatbot, use @jarvis (or @{chatbot_name} for a diffrent chatbot) to ask any question. The chatbot is completely conversational, meaning it remembers the course name for all next set of classes. Use reset keyword to reset the previous conversation.


##### Check a quick demo
https://www.youtube.com/watch?v=eHA4Is6DFzw