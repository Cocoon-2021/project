


CREATE TABLE basics_location 
(
  id INT AUTO_INCREMENT,
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
  workId INT,
  name TEXT,
  location TEXT,
  description TEXT,
  position TEXT,
  url TEXT,
  startDate TEXT,
  endDate TEXT,
  summary TEXT,
  PRIMARY KEY (workId),
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE work_highlights 
(
  workId INT,
  value TEXT,
  FOREIGN KEY (workId) REFERENCES work(workId)
);

CREATE TABLE work_keywords (
  workId INT,
  value TEXT,
  FOREIGN KEY (workId) REFERENCES work(workId)
);

CREATE TABLE volunteer 
(
  resumeId INT,
  volunteerId INT,
  organization TEXT,
  position TEXT,
  url TEXT,
  startDate TEXT,
  endDate TEXT,
  summary TEXT,
  PRIMARY KEY (volunteerId),
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE volunteer_highlights 
(
  volunteerId INT,
  value TEXT,
  FOREIGN KEY (volunteerId) REFERENCES volunteer(volunteerId))
);

CREATE TABLE education 
(
  resumeId INT,
  educationId INT,
  institution TEXT,
  url TEXT,
  area TEXT,
  studyType TEXT,
  startDate TEXT,
  endDate TEXT,
  score TEXT,
  PRIMARY KEY (educationId),
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE education_courses 
(
  educationId INT,
  value TEXT,
  FOREIGN KEY (educationId) REFERENCES education(educationId)
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
  skillsId INT,
  name TEXT,
  level TEXT,
  PRIMARY KEY (skillsId),
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE skills_keywords 
(
  skillsId INT,
  value TEXT,
  FOREIGN KEY (skillsId) REFERENCES skills(skillsId)
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
  interestsId INT,
  name TEXT,
  PRIMARY KEY (interestsId),
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE interests_keywords 
(
  interestsId INT,
  value TEXT,
  FOREIGN KEY (interestsId) REFERENCES interests(interestsId)
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
  projectsId INT,
  name TEXT,
  description TEXT,
  startDate TEXT,
  endDate TEXT,
  url TEXT,
  entity TEXT,
  type TEXT,
  PRIMARY KEY (projectsId),
  FOREIGN KEY (resumeId) REFERENCES resume(id)
);

CREATE TABLE projects_highlights 
(
  projectsId INT,
  value TEXT,
  FOREIGN KEY (projectsId) REFERENCES projects(projectsId)
);

CREATE TABLE projects_keywords 
(
  projectsId INT,
  value TEXT,
  FOREIGN KEY (projectsId) REFERENCES projects(projectsId)
);

CREATE TABLE projects_roles 
(
  projectsId INT,
  value TEXT,
  FOREIGN KEY (projectsId) REFERENCES projects(projectsId)
);

