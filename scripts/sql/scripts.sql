DROP DATABASE IF EXISTS slackbot;
CREATE DATABASE slackbot;
use slackbot;

create table instructors (
  id int auto_increment not null primary key,
  name varchar(255),
  office_location varchar(255),
  email varchar(255),
  office_start_time varchar(255),
  office_end_time varchar(255),
  specific_instruction varchar(255),
  preferred_contact_method varchar(255),
  office_phone varchar(255),
  about varchar(255)
);

create table courses(
    id int auto_increment not null primary key,
    name varchar(255),
    description varchar(255),
    pre_requisites varchar(255)
);

create table course_sections(
    id int auto_increment not null primary key,
    course_id int,
    section_no int,
    CONSTRAINT CRSE_SEC UNIQUE (course_id,section_no)
);

create table course_schedules(
    id int auto_increment not null primary key,
	course_section_id int not null,
    due_date timestamp ,
    activity_type int not null,
    activity varchar(255),
    foreign key (course_section_id) references course_sections(id)

    /* activity type 0=lab, 1=assignment, 3=project, 4= mid-term, 5=final*/
);

create table course_topics(
    id int auto_increment not null primary key,
    course_section_id int not null,
    lecture_date date,
    topic varchar(255),
    foreign key (course_section_id) references course_sections(id)
    );

create table course_grading (
    id int auto_increment not null primary key,
	course_section_id int not null,
    activity varchar(255),
    activity_type int not null,
    weight varchar(20),
    foreign key (course_section_id) references course_sections(id)

    /* 0=quiz, 1=lab, 2=assignment, 3=project, 4=mid-term, 5=final */
);		

create table program_outcomes(
    id int auto_increment not null primary key,
	course_section_id int not null,
    description varchar(255),
    foreign key (course_section_id) references course_sections(id)
);

create table learning_objectives(
    id int auto_increment not null primary key,
	course_section_id int not null,
    description varchar(255),
    foreign key (course_section_id) references course_sections(id)
);

create table course_section_details(
    id int auto_increment not null primary key,
    course_section_id int not null,
    instr_id int not null,
	day_of_week varchar(255),
    class_start_time varchar(20),
    class_end_time varchar(255),
    class_location varchar(255),
    course_website varchar(255),
    add_drop_detail varchar(255),
    reference_material varchar(255),
    grading_type varchar(30),
    classroom_protocol varchar(255),
    extra_details varchar(255),
	foreign key (course_section_id) references course_sections(id),
    foreign key (instr_id) references instructors(id)
);

create table university_policy(
    code int auto_increment not null primary key,
    name varchar(255),
    description text(60000)
);

