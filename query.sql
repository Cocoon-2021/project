DROP DATABASE resumedata;

CREATE DATABASE resumedata;

USE resumedata;


CREATE TABLE resume (
  id INT,
  coverLetter TEXT,
  PRIMARY KEY (id)
);

CREATE TABLE basics (
  resume_id INT,
  name TEXT,
  label TEXT,
  image TEXT,
  email TEXT,
  phone TEXT,
  url TEXT,
  summary TEXT,
  PRIMARY KEY (resume_id),
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE basics_location (
  resume_id INT,
  address TEXT,
  postalCode TEXT,
  city TEXT,
  countryCode TEXT,
  region TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE basics_profiles (
  resume_id INT,
  network TEXT,
  username TEXT,
  url TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE work (
  resume_id INT,
  name TEXT,
  location TEXT,
  description TEXT,
  position TEXT,
  url TEXT,
  startDate TEXT,
  endDate TEXT,
  summary TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE work_highlights (
  resume_id INT,
  value TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE work_keywords (
  resume_id INT,
  value TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE volunteer (
  resume_id INT,
  organization TEXT,
  position TEXT,
  url TEXT,
  startDate TEXT,
  endDate TEXT,
  summary TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE volunteer_highlights (
  resume_id INT,
  value TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE education (
  resume_id INT,
  institution TEXT,
  url TEXT,
  area TEXT,
  studyType TEXT,
  startDate TEXT,
  endDate TEXT,
  score TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE education_courses (
  resume_id INT,
  value TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE awards (
  resume_id INT,
  title TEXT,
  date TEXT,
  awarder TEXT,
  summary TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE certificates (
  resume_id INT,
  name TEXT,
  date TEXT,
  url TEXT,
  issuer TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE publications (
  resume_id INT,
  name TEXT,
  publisher TEXT,
  releaseDate TEXT,
  url TEXT,
  summary TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE skills (
  resume_id INT,
  name TEXT,
  level TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE skills_keywords (
  resume_id INT,
  value TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE languages (
  resume_id INT,
  language TEXT,
  fluency TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE interests (
  resume_id INT,
  name TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE interests_keywords (
  resume_id INT,
  value TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE `references` (
  resume_id INT,
  name TEXT,
  reference TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE projects (
  resume_id INT,
  name TEXT,
  description TEXT,
  startDate TEXT,
  endDate TEXT,
  url TEXT,
  entity TEXT,
  type TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE projects_highlights (
  resume_id INT,
  value TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE projects_keywords (
  resume_id INT,
  value TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE projects_roles (
  resume_id INT,
  value TEXT,
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

