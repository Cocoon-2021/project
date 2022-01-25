DROP DATABASE IF EXISTS resumedata;

CREATE DATABASE resumedata;

USE resumedata;


CREATE TABLE resume 
(
  id INT,
  coverLetter TEXT,
  name TEXT,
  label TEXT,
  image TEXT,
  email TEXT,
  phone TEXT,
  url TEXT,
  summary TEXT,
  PRIMARY KEY (id)
);

CREATE TABLE basics_location 
(
  resumeId INT,
  address TEXT,
  postalCode TEXT,
  city TEXT,
  countryCode TEXT,
  region TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE basics_profiles 
(
  resumeId INT,
  network TEXT,
  username TEXT,
  url TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE work 
(
  resumeId INT,
  id INT,
  name TEXT,
  location TEXT,
  description TEXT,
  position TEXT,
  url TEXT,
  startDate TEXT,
  endDate TEXT,
  summary TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE work_highlights 
(
  resumeId INT,
  workId INT,
  value TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE work_keywords (
  resumeId INT,
  workId INT,
  value TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE volunteer 
(
  resumeId INT,
  id INT,
  organization TEXT,
  position TEXT,
  url TEXT,
  startDate TEXT,
  endDate TEXT,
  summary TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE volunteer_highlights 
(
  resumeId INT,
  volId INT,
  value TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE education 
(
  resumeId INT,
  id INT,
  institution TEXT,
  url TEXT,
  area TEXT,
  studyType TEXT,
  startDate TEXT,
  endDate TEXT,
  score TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE education_courses 
(
  resumeId INT,
  eduId INT,
  value TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE awards 
(
  resumeId INT,
  title TEXT,
  date TEXT,
  awarder TEXT,
  summary TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)  
);

CREATE TABLE certificates 
(
  resumeId INT,
  name TEXT,
  date TEXT,
  url TEXT,
  issuer TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE publications 
(
  resumeId INT,
  name TEXT,
  publisher TEXT,
  releaseDate TEXT,
  url TEXT,
  summary TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE skills 
(
  resumeId INT,
  id INT,
  name TEXT,
  level TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE skills_keywords 
(
  resumeId INT,
  skillId INT,
  value TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE languages 
(
  resumeId INT,
  language TEXT,
  fluency TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE interests 
(
  resumeId INT,
  id INT,
  name TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE interests_keywords 
(
  resumeId INT,
  intrId INT,
  value TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE `references` 
(
  resumeId INT,
  name TEXT,
  reference TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE projects 
(
  resumeId INT,
  id INT,
  name TEXT,
  description TEXT,
  startDate TEXT,
  endDate TEXT,
  url TEXT,
  entity TEXT,
  type TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE projects_highlights 
(
  resumeId INT,
  proId INT,
  value TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE projects_keywords 
(
  resumeId INT,
  proId INT,
  value TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE projects_roles 
(
  resumeId INT,
  proId INT,
  value TEXT,
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

