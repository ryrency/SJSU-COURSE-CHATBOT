use slackbot;


/*******************************************************************************************************************************************************************/
/*GREENSHEET - SITHU AUNG*/
/*******************************************************************************************************************************************************************/

INSERT INTO  courses(name, description, pre_requisites)
VALUES("cmpe273", "Enterprise Distributed Systems", "Strong in a OOP or functional programming language");


INSERT INTO instructors (name, office_location, email, office_start_time,
office_end_time, specific_instruction, preferred_contact_method, office_phone, about)
VALUES("Sithu Aung","ENG 281","Sithu.aung@sjsu.edu","Wednesday 5:00PM", "6:00PM" ,"Appointment necessary before meeting","e-mail","Office Phone No not shared","Professor at SJSU" );



INSERT INTO course_sections(course_id, section_no)
VALUES(1, "01");



INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(1, "2017-02-02 11:59:00","Lab1", 0);
INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(1, "2017-03-08 11:59:00","Assignment 1", 1);
INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(1, "2017-03-22 11:59:00","Lab 2", 0);
INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(1, "2017-03-29 11:59:00","Assignment 2", 1);
INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(1, "2017-04-12 11:59:00","Lab 3", 0);
INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(1, "2017-04-26 11:59:00","Assignment 3", 1);
INSERT INTO course_schedules (course_section_id, due_date, activity, activity_type)
VALUES(1, "2017-05-10 11:59:00","Lab 4", 0);
INSERT INTO course_schedules (course_section_id, due_date, activity, activity_type)
VALUES(1, "2017-05-10 11:59:00","Project", 2);
INSERT INTO course_schedules (course_section_id, due_date, activity, activity_type)
VALUES(1, "2017-05-10 17:00:00","Mid-term", 3);
INSERT INTO course_schedules (course_section_id, due_date, activity, activity_type)
VALUES(1, "2017-05-10 17:00:00","Final Exam", 4);




INSERT INTO course_topics(course_section_id, lecture_date, topic)
VALUES(1,"2017-02-01","Distributed Systems Overview");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(1,"2017-02-08","Integration Protocols");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(1,"2017-02-15","Remote Procedure calls");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(1,"2017-02-22","RESTful Web Services");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(1,"2017-02-22","RESTful Web Services");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(1,"2017-03-01","RESTful Web Services");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(1,"2017-03-08","Messaging");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(1,"2017-03-15","Consistency Models");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(1,"2017-03-22","Fault Tolerance(Replication)");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(1,"2017-03-29","Spring Break - NO CLASS");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(1,"2017-04-05","Mid Term");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(1,"2017-04-12","MessFault Tolerance(Sharding)");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(1,"2017-04-19","Consensus");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(1,"2017-04-26","Performance");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(1,"2017-05-03","Decentralised Application");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(1,"2017-05-10","Project Presentations");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(1,"2017-05-24","Final Exam");




INSERT INTO course_grading(course_section_id, activity, weight, activity_type)
VALUES(1, "Pop Quizzes","5%", 0);
INSERT INTO course_grading(course_section_id, activity, weight, activity_type)
VALUES(1, "Labs","5%", 1);
INSERT INTO course_grading(course_section_id,activity,weight, activity_type)
VALUES(1, "Assignment","30%", 2);
INSERT INTO course_grading(course_section_id,activity,weight, activity_type)
VALUES(1, "Class Project","20%", 3);
INSERT INTO course_grading(course_section_id,activity,weight, activity_type)
VALUES(1, "Mid-Term Exam","20%", 4);
INSERT INTO course_grading(course_section_id,activity,weight, activity_type)
VALUES(1, "Final Exam","20%", 5);



INSERT INTO program_outcomes(course_section_id, description)
VALUES(1,"Be able to demonstrate an understanding of advanced knowledge of the practice of software engineering, from vision to analysis, design, validation and deployment. ");
INSERT INTO program_outcomes(course_section_id, description)
VALUES(1,"Be able to tackle complex engineering problems and tasks, using contemporary engineering principles, methodologies and tools. ");
INSERT INTO program_outcomes(course_section_id, description)
VALUES(1,"Be able to demonstrate leadership and the ability to participate in teamwork in an environment with different disciplines of engineering, science and business. ");
INSERT INTO program_outcomes(course_section_id, description)
VALUES(1,"Be aware of ethical, economic and environmental implications of their work, as appropriate.");
INSERT INTO program_outcomes(course_section_id, description)
VALUES(1,"Be able to advance successfully in the engineering profession, and sustain a process of life-long learning in engineer or other professional areas.");
INSERT INTO program_outcomes(course_section_id, description)
VALUES(1,"Be able to communicate effectively, in both oral and written forms.");



INSERT INTO course_section_details(course_section_id,instr_id,class_start_time, class_end_time, class_location,course_website,add_drop_detail,reference_material,day_of_week)
VALUES(1,1,"6:00PM","8.45PM","SH100",
"https://sjsu.instructure.com/courses",
"Please check college website for details",
"Web Services - by Gustavo Alonso, Fabio Casati, Harumi Kuno and Vijay Machiraju (2003), Enterprise Integration Patterns - by Gregor Hohpe and Bobby Woolf (2003), Restful Web Services, by Leonard Richardson, Sam Ruby and David Hansson (2007)" ,
"Wednesday");



INSERT INTO learning_objectives(course_section_id, description)
VALUES(1,"Ability to demonstrate an understanding of architecture principles in building distributed systems");
INSERT INTO learning_objectives(course_section_id,description)
VALUES(1,"Ability to create application services using Web Services. ");
INSERT INTO learning_objectives(course_section_id,description)
VALUES(1,"Ability to integrate application services using Java Messaging Services");
INSERT INTO learning_objectives(course_section_id,description)
VALUES(1,"Ability to design and implement distributed systems with a particular emphasis on how to deal with the shared state using distributed caching");
INSERT INTO learning_objectives(course_section_id,description)
VALUES(1,"Ability to identify and evaluate application protocols and integration patterns for distributed system");





/*******************************************************************************************************************************************************************/
/*GREENSHEET - RICHARD SINN*/
/*******************************************************************************************************************************************************************/

INSERT INTO  courses(name, description, pre_requisites)
VALUES("cmpe272", "Enterprise Software Platforms", "Classified graduate standing or instructor consent. Computer Engineering and Software Engineering majors only.");

INSERT INTO instructors (name, office_location, email, office_start_time,
office_end_time, specific_instruction, preferred_contact_method, office_phone, about)
VALUES("Richard Sinn","ENG 337","richardsinn@yahoo.com","Saturday 9:15AM", "12:00PM","Class meets every sat","e-mail","Office Phone No not shared","Richard Sinn is a Professor at SJSU and a Senior Software Development Manager at Adobe." );


INSERT INTO course_sections(course_id, section_no)
VALUES(2, "02");



INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(2, "2017-02-07 11:59:00","Lab- Mobile Ad Hoc Network", 0);
INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(2, "2017-03-01 11:59:00","Lab: TCP Plot Reading Exercise", 0);
INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(2, "2017-03-08 11:59:00","Homework Web Env Setup", 0);
INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(2, "2017-03-15 11:59:00","Lab: Create Basic Web Application / Page", 0);
INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(2, "2017-03-22 11:59:00","Lab: Secure Section with username and password verification", 0);
INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(2, "2017-04-12 11:59:00","Lab: Database for Users", 0);
INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(2, "2017-04-19 11:59:00","Lab: Cookie App", 0);
INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(2, "2017-04-26 11:59:00","Lab: CURL", 0);
INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(2, "2017-05-03 11:59:00","Lab: Youtube tryout", 0);
INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(2,"2017-05-20 09:10:00","Final Exam",4);
INSERT INTO course_schedules	(course_section_id, due_date, activity, activity_type)
VALUES(2,"2017-03-24 09:10:00","Mid Term",3);






INSERT INTO course_topics(course_section_id, lecture_date, topic)
VALUES(2,"2017-01-28","Enterprise Architecture");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(2,"2017-02-04","Wireless and Mobile Networks");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(2,"2017-02-11","HTTP");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(2,"2017-02-18","TCP / Networking");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(2,"2017-02-25","HTML 5 Programming");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(2,"2017-03-04","Security Overview ");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(2,"2017-03-12","PKI");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(2,"2017-03-19","Firewall and IDS");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(2,"2017-03-25","Midterm");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(2,"2017-04-01","Database / SQL");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(2,"2017-04-08","Big Data");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(2,"2017-04-15","Mobile Computing");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(2,"2017-04-22","Cloud Computing");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(2,"2017-04-29","RFID / IoT");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(2,"2017-05-06","Project Presentation");
INSERT INTO course_topics(course_section_id,lecture_date,topic)
VALUES(2,"2017-05-20","Final Exam");


INSERT INTO course_grading(course_section_id, activity, weight, activity_type)
VALUES(2, "Labs","35%", 1);
INSERT INTO course_grading(course_section_id,activity,weight, activity_type)
VALUES(2, "Team Project","20%", 2);
INSERT INTO course_grading(course_section_id,activity,weight, activity_type)
VALUES(2, "Team Presentation","20%", 3);
INSERT INTO course_grading(course_section_id,activity,weight, activity_type)
VALUES(2, "Mid-Term Exam","15%", 4);
INSERT INTO course_grading(course_section_id,activity,weight, activity_type)
VALUES(2, "Final Exam","20%", 5);




INSERT INTO program_outcomes(course_section_id, description)
VALUES(2,"Be able to demonstrate an understanding of advanced knowledge of the practice of software engineering, from vision to analysis, design, validation and deployment.");
INSERT INTO program_outcomes(course_section_id, description)
VALUES(2,"Be able to tackle complex engineering problems and tasks, using contemporary engineering principles, methodologies and tools.");
INSERT INTO program_outcomes(course_section_id, description)
VALUES(2,"Be able to demonstrate leadership and the ability to participate in teamwork in an environment with different disciplines of engineering, science and business.");
INSERT INTO program_outcomes(course_section_id, description)
VALUES(2,"Be aware of ethical, economic and environmental implications of their work, as appropriate.");
INSERT INTO program_outcomes(course_section_id, description)
VALUES(2,"Be able to advance successfully in the engineering profession, and sustain a process of life-long learning in engineer or other professional areas.");
INSERT INTO program_outcomes(course_section_id, description)
VALUES(2,"Be able to communicate effectively, in both oral and written forms.");




INSERT INTO learning_objectives(course_section_id, description)
VALUES(2,"Ability to identify and evaluate technologies and place them within a software platform.");
INSERT INTO learning_objectives(course_section_id, description)
VALUES(2,"Ability to understand where a technology fits within its maturity lifecycle.");
INSERT INTO learning_objectives(course_section_id, description)
VALUES(2,"Ability to understand the standardization process for enterprise class software technologies.");
INSERT INTO learning_objectives(course_section_id, description)
VALUES(2,"Ability to compose a software platform and system architecture solution using available technologies given a business problem.");
INSERT INTO learning_objectives(course_section_id, description)
VALUES(2,"Ability to analyze software technologies, standards, and architectures then communicate the outcome of the analysis.");





INSERT INTO course_section_details(course_section_id,instr_id,class_start_time, class_end_time, class_location,course_website,add_drop_detail,reference_material,day_of_week)
VALUES(2,2,"9:15AM","12.00PM","ENG 337",
"http://openloop.com/education/classes/sjsu_engr/engr_ent_swplatforms/",
"Please check college website for details.",
"HTTP 1.1 - RFC 2616" ,
"Saturday");


/*******************************************************************************************************************************************************************/
/*University policies*/
/*******************************************************************************************************************************************************************/


INSERT INTO  university_policy(name,description)
VALUES("ALl Policies","Per University Policy S16-9, university-wide policy information relevant to all courses, such as academic integrity, accommodations, etc. will be available on Office of Graduate and Undergraduate Programs’ Syllabus Information web page at http://www.sjsu.edu/gup/syllabusinfo/”
");


