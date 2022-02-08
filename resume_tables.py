from ast import Delete
from database_engine import engine
from sqlalchemy import Column, Integer, ForeignKey, Text, delete
from sqlalchemy.orm import declarative_base



table_base = declarative_base()

class basics_information(table_base):
    __tablename__ = 'basics_information'
    resumeId = Column(Integer, primary_key=True, autoincrement=True)
    resumeCoverLetter = Column(Text)
    resumerName = Column(Text)
    position = Column(Text)
    profilePicture = Column(Text)
    resumerEmail = Column(Text)
    resumerPhone = Column(Text)
    resumerAddress = Column(Text)
    resumerPostalCode = Column(Text)
    resumerCity = Column(Text)
    resumerCountryCode = Column(Text)
    resumerRegion = Column(Text)
    resumerUrl = Column(Text)
    resumerSummary = Column(Text)
    

class basics_profiles(table_base):
    __tablename__ = 'basics_profiles'
    profileId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId"), nullable=False)
    profileNetwork = Column(Text)
    profileUsername= Column(Text)
    profileUrl = Column(Text)
    
class work(table_base):
    __tablename__ = 'work'
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId"), nullable=False)
    workId = Column(Integer, primary_key=True, nullable=False)
    companyName = Column(Text)
    companyLocation = Column(Text)
    workDescription = Column(Text)
    workPosition = Column(Text)
    companyUrl = Column(Text)
    workStartDate = Column(Text)
    workEndDate = Column( Text)
    workSummary = Column(Text)
    workHighlights = Column(Text)
    workKeywords = Column(Text)

class volunteer(table_base):
    __tablename__ = 'volunteer'
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId"), nullable=False)
    volunteerId = Column(Integer,primary_key=True, nullable=False)
    volunteeredOrganization = Column(Text)
    volunteeredPosition = Column(Text)
    organizationUrl = Column(Text)
    volunteeringStartDate = Column(Text)
    volunteeringEndDate = Column(Text)
    volunteeringSummary = Column(Text)
    volunteeringHighlights = Column(Text)

class education(table_base):
    __tablename__ = 'education'
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId"), nullable=False)
    educationId = Column(Integer,primary_key=True, nullable=False)
    educationInstitution = Column(Text)
    institutionUrl = Column(Text)
    educatedArea = Column(Text)
    educatedStudyType = Column(Text)
    educationStartDate = Column(Text)
    educationEndDate = Column(Text)
    educationScore = Column(Text)

class education_courses(table_base):
    __tablename__ = 'education_courses'
    coursesId = Column(Integer, primary_key=True, autoincrement=True)
    educationId = Column(Integer, ForeignKey("education.educationId"), nullable=False)
    educatedCourses = Column(Text)

class awards(table_base):
    __tablename__ = 'awards'
    awardsId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId"), nullable=False)
    awardTitle = Column(Text)
    awardedDate = Column(Text)
    awarder = Column(Text)
    awardSummary = Column(Text)

class certificates(table_base):
    __tablename__ = 'certificates'
    certificatesId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId"), nullable=False)
    certificateName = Column(Text)
    certificateIssueDate = Column(Text)
    certificateUrl = Column(Text)
    certificateIssuer = Column(Text)

class publications(table_base):
    __tablename__ = 'publications'
    publicationsId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId"), nullable=False)
    publicationTitle = Column(Text)
    publisher = Column(Text)
    publishedDate = Column(Text)
    publishedUrl = Column(Text)
    publicationSummary = Column(Text)

class skills(table_base):
    __tablename__ = 'skills'
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId"), nullable=False)
    skillsId = Column(Integer, primary_key=True, nullable=False)
    skillName = Column(Text)
    skillLevel = Column(Text)
    skillKeywords = Column(Text)

class languages(table_base):
    __tablename__ = 'languages'
    languagesId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId"), nullable=False)
    language = Column(Text)
    languageFluency = Column(Text)

class interests(table_base):
    __tablename__ = 'interests'
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId"), nullable=False)
    interestsId = Column(Integer, primary_key=True, nullable=False)
    interestName = Column(Text)
    interestKeywords = Column(Text)

class references(table_base):
    __tablename__ = 'references'
    referenecesId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId"), nullable=False)
    referrerName = Column(Text)
    reference = Column(Text)

class projects(table_base):
    __tablename__ = 'projects'
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId"), nullable=False)
    projectsId = Column(Integer, primary_key=True, nullable=False)
    projectName= Column(Text)
    projectDescription = Column(Text)
    projectStartDate = Column(Text)
    projectEndDate = Column(Text)
    projectUrl = Column(Text)
    projectEntity = Column(Text)
    projectType = Column(Text)
    projectHighlights = Column(Text)
    projectKeywords = Column(Text)
    projectRoles = Column(Text)



table_base.metadata.create_all(engine)