

USE RESUME;

CREATE TABLE resume (
  id INT NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE resume_0 (
  resume_id INT,
  id INT,
  coverLetter TEXT,
  enableSourceDataDownload BOOLEAN,
  PRIMARY KEY (id),
  FOREIGN KEY (resume_id) REFERENCES resume(id)
);

CREATE TABLE basics (
  resume_0_id INT,
  id INT,
  name TEXT,
  label TEXT,
  image TEXT,
  email TEXT,
  phone TEXT,
  url TEXT,
  summary TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (resume_0_id) REFERENCES resume_0(id)
);

CREATE TABLE basics_location (
  basics_id INT,
  id INT,
  address TEXT,
  postalCode TEXT,
  city TEXT,
  countryCode TEXT,
  region TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (basics_id) REFERENCES basics(id)
);

CREATE TABLE basics_profiles (
  basics_id INT,
  id INT,
  network TEXT,
  username TEXT,
  url TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (basics_id) REFERENCES basics(id)
);

CREATE TABLE work (
  resume_0_id INT,
  id INT,
  name TEXT,
  location TEXT,
  description TEXT,
  position TEXT,
  url TEXT,
  startDate TEXT,
  endDate TEXT,
  summary TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (resume_0_id) REFERENCES resume_0(id)
);

CREATE TABLE work_highlights (
  work_id INT,
  id INT,
  value TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (work_id) REFERENCES work(id)
);

CREATE TABLE work_keywords (
  work_id INT,
  id INT,
  value TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (work_id) REFERENCES work(id)
);

CREATE TABLE volunteer (
  resume_0_id INT,
  id INT,
  organization TEXT,
  position TEXT,
  url TEXT,
  startDate TEXT,
  endDate TEXT,
  summary TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (resume_0_id) REFERENCES resume_0(id)
);

CREATE TABLE volunteer_highlights (
  volunteer_id INT,
  id INT,
  value TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (volunteer_id) REFERENCES volunteer(id)
);

CREATE TABLE education (
  resume_0_id INT,
  id INT,
  institution TEXT,
  url TEXT,
  area TEXT,
  studyType TEXT,
  startDate TEXT,
  endDate TEXT,
  score TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (resume_0_id) REFERENCES resume_0(id)
);

CREATE TABLE education_courses (
  education_id INT,
  id INT,
  value TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (education_id) REFERENCES education(id)
);

CREATE TABLE awards (
  resume_0_id INT,
  id INT,
  title TEXT,
  date TEXT,
  awarder TEXT,
  summary TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (resume_0_id) REFERENCES resume_0(id)
);

CREATE TABLE certificates (
  resume_0_id INT,
  id INT,
  name TEXT,
  date TEXT,
  url TEXT,
  issuer TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (resume_0_id) REFERENCES resume_0(id)
);

CREATE TABLE publications (
  resume_0_id INT,
  id INT,
  name TEXT,
  publisher TEXT,
  releaseDate TEXT,
  url TEXT,
  summary TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (resume_0_id) REFERENCES resume_0(id)
);

CREATE TABLE skills (
  resume_0_id INT,
  id INT,
  name TEXT,
  level TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (resume_0_id) REFERENCES resume_0(id)
);

CREATE TABLE skills_keywords (
  skills_id INT,
  id INT,
  value TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (skills_id) REFERENCES skills(id)
);

CREATE TABLE languages (
  resume_0_id INT,
  id INT,
  language TEXT,
  fluency TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (resume_0_id) REFERENCES resume_0(id)
);

CREATE TABLE interests (
  resume_0_id INT,
  id INT,
  name TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (resume_0_id) REFERENCES resume_0(id)
);

CREATE TABLE interests_keywords (
  interests_id INT,
  id INT,
  value TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (interests_id) REFERENCES interests(id)
);

CREATE TABLE `references` (
  resume_0_id INT,
  id INT,
  name TEXT,
  reference TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (resume_0_id) REFERENCES resume_0(id)
);

CREATE TABLE projects (
  resume_0_id INT,
  id INT,
  name TEXT,
  description TEXT,
  startDate TEXT,
  endDate TEXT,
  url TEXT,
  entity TEXT,
  type TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (resume_0_id) REFERENCES resume_0(id)
);

CREATE TABLE projects_highlights (
  projects_id INT,
  id INT,
  value TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (projects_id) REFERENCES projects(id)
);

CREATE TABLE projects_keywords (
  projects_id INT,
  id INT,
  value TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (projects_id) REFERENCES projects(id)
);

CREATE TABLE projects_roles (
  projects_id INT,
  id INT,
  value TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (projects_id) REFERENCES projects(id)
);

CREATE TABLE meta (
  resume_0_id INT,
  id INT,
  canonical TEXT,
  version TEXT,
  lastModified TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (resume_0_id) REFERENCES resume_0(id)
);

CREATE TABLE __translation__ (
  resume_0_id INT,
  id INT,
  awards TEXT,
  volunteers TEXT,
  skills TEXT,
  `references` TEXT,
  publications TEXT,
  languages TEXT,
  interests TEXT,
  education TEXT,
  summary TEXT,
  experience TEXT,
  at TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (resume_0_id) REFERENCES resume_0(id)
);
