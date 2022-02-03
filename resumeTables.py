from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, ForeignKey, Text, insert
from sqlalchemy.orm import declarative_base

engine = create_engine(
    'mysql+mysqlconnector://root:password@localhost/resumedata', connect_args={'auth_plugin': 'mysql_native_password'} 
    )

connect_engine = engine.connect()
table_base = declarative_base()

class basics_information(table_base):
    __tablename__ = 'basics_information'
    id = Column(Integer, primary_key=True, autoincrement=True)
    coverLetter = Column(Text)
    name = Column(Text)
    label = Column(Text)
    image = Column(Text)
    email = Column(Text)
    phone = Column(Text)
    url = Column(Text)
    summary = Column(Text)

class basics_location(table_base):
    __tablename__ = 'basics_location'
    id = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey('basics_information.id'), nullable=False)
    address = Column(Text)
    postalCode = Column(Text)
    city = Column(Text)
    countryCode = Column(Text)
    region = Column(Text)

class basics_profiles(table_base):
    __tablename__ = 'basics_profiles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    network = Column(Text)
    username= Column(Text)
    url = Column(Text)
    
class work(table_base):
    __tablename__ = 'work'
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    workId = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text)
    location = Column(Text)
    description = Column(Text)
    position = Column(Text)
    url = Column(Text)
    startDate = Column(Text)
    endDate = Column( Text)
    summary = Column(Text)

class work_highlights(table_base):
    __tablename__ = 'work_highlights'
    id = Column(Integer, primary_key=True, autoincrement=True)
    workId = Column(Integer, ForeignKey("work.workId"), nullable=False)
    value = Column(Text)

class work_keywords(table_base):
    __tablename__ = 'work_keywords'
    id = Column(Integer, primary_key=True, autoincrement=True)
    workId = Column(Integer, ForeignKey("work.workId"), nullable=False)
    value = Column(Text)

class volunteer(table_base):
    __tablename__ = 'volunteer'
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    volunteerId = Column(Integer,primary_key=True, nullable=False)
    organization = Column(Text)
    position = Column(Text)
    url = Column(Text)
    startDate = Column(Text)
    endDate = Column(Text)
    summary = Column(Text)

class volunteer_highlights(table_base):
    __tablename__ = 'volunteer_highlights'
    id = Column(Integer, primary_key=True, autoincrement=True)
    volunteerId = Column(Integer,ForeignKey("volunteer.volunteerId"), nullable=False)
    value = Column(Text)

class education(table_base):
    __tablename__ = 'education'
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    educationId = Column(Integer,primary_key=True, nullable=False)
    institution = Column(Text)
    url = Column(Text)
    area = Column(Text)
    studyType = Column(Text)
    startDate = Column(Text)
    endDate = Column(Text)
    score = Column(Text)

class education_courses(table_base):
    __tablename__ = 'education_courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    educationId = Column(Integer, ForeignKey("education.educationId"), nullable=False)
    value = Column(Text)

class awards(table_base):
    __tablename__ = 'awards'
    id = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    title = Column(Text)
    date = Column(Text)
    awarder = Column(Text)
    summary = Column(Text)

class certificates(table_base):
    __tablename__ = 'certificates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    name = Column(Text)
    date = Column(Text)
    url = Column(Text)
    issuer = Column(Text)

class publications(table_base):
    __tablename__ = 'publications'
    id = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    name = Column(Text)
    publisher = Column(Text)
    releaseDate = Column(Text)
    url = Column(Text)
    summary = Column(Text)

class skills(table_base):
    __tablename__ = 'skills'
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    skillsId = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text)
    level = Column(Text)

class skills_keywords(table_base):
    __tablename__ = 'skills_keywords'
    id = Column(Integer, primary_key=True, autoincrement=True)
    skillsId = Column(Integer, ForeignKey("skills.skillsId"), nullable=False)
    value = Column(Text)

class languages(table_base):
    __tablename__ = 'languages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    language = Column(Text)
    fluency = Column(Text)

class interests(table_base):
    __tablename__ = 'interests'
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    interestsId = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text)

class interests_keywords(table_base):
    __tablename__ = 'interests_keywords'
    id = Column(Integer, primary_key=True, autoincrement=True)
    interestsId = Column(Integer, ForeignKey("interests.interestsId"), nullable=False)
    value = Column(Text)

class references(table_base):
    __tablename__ = 'references'
    id = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    name = Column(Text)
    reference = Column(Text)

class projects(table_base):
    __tablename__ = 'projects'
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    projectsId = Column(Integer, primary_key=True, nullable=False)
    name= Column(Text)
    description = Column(Text)
    startDate = Column(Text)
    endDate = Column(Text)
    url = Column(Text)
    entity = Column(Text)
    type = Column(Text)

class projects_highlights(table_base):
    __tablename__ = 'projects_highlights'
    id = Column(Integer, primary_key=True, autoincrement=True)
    projectsId = Column(Integer, ForeignKey("projects.projectsId"), nullable=False)
    value = Column(Text)

class projects_keywords(table_base):
    __tablename__ = 'projects_keywords'
    id = Column(Integer, primary_key=True, autoincrement=True)
    projectsId = Column(Integer, ForeignKey("projects.projectsId"), nullable=False)
    value = Column(Text)

class projects_roles(table_base):
    __tablename__ = 'projects_roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    projectsId = Column(Integer, ForeignKey("projects.projectsId"), nullable=False)
    value = Column(Text)


table_base.metadata.create_all(engine)




