from ast import Delete
from database_engine import engine
from sqlalchemy import Column, Integer, ForeignKey, Text, delete
from sqlalchemy.orm import declarative_base,relationship



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
    relation = relationship("basics_profiles", back_populates="basics_information", cascade="all, delete", passive_deletes=True)
    

class basics_profiles(table_base):
    __tablename__ = 'basics_profiles'
    profileId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId", ondelete="CASCADE"), nullable=False)
    profileNetwork = Column(Text)
    profileUsername= Column(Text)
    profileUrl = Column(Text)
    childrelation = relationship("baiscs_information", back_populates="basics_profiles")
    
class work(table_base):
    __tablename__ = 'work'
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId", ondelete="CASCADE"), nullable=False)
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
    childrelation = relationship("baiscs_information", back_populates="work")


class volunteer(table_base):
    __tablename__ = 'volunteer'
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId", ondelete="CASCADE"), nullable=False)
    volunteerId = Column(Integer,primary_key=True, nullable=False)
    volunteeredOrganization = Column(Text)
    volunteeredPosition = Column(Text)
    organizationUrl = Column(Text)
    volunteeringStartDate = Column(Text)
    volunteeringEndDate = Column(Text)
    volunteeringSummary = Column(Text)
    volunteeringHighlights = Column(Text)
    childrelation = relationship("baiscs_information", back_populates="volunteer")


class education(table_base):
    __tablename__ = 'education'
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId", ondelete="CASCADE"), nullable=False)
    educationId = Column(Integer,primary_key=True, nullable=False)
    educationInstitution = Column(Text)
    institutionUrl = Column(Text)
    educatedArea = Column(Text)
    educatedStudyType = Column(Text)
    educationStartDate = Column(Text)
    educationEndDate = Column(Text)
    educationScore = Column(Text)
    childrelation = relationship("baiscs_information", back_populates="education")
    eduactionprelation = relationship("education_courses", back_populates="education", cascade="all, delete", passive_deletes=True)


class education_courses(table_base):
    __tablename__ = 'education_courses'
    coursesId = Column(Integer, primary_key=True, autoincrement=True)
    educationId = Column(Integer, ForeignKey("education.educationId", ondelete="CASCADE"), nullable=False)
    educatedCourses = Column(Text)
    childrelation = relationship("education", back_populates="education_courses")


class awards(table_base):
    __tablename__ = 'awards'
    awardsId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId", ondelete="CASCADE"), nullable=False)
    awardTitle = Column(Text)
    awardedDate = Column(Text)
    awarder = Column(Text)
    awardSummary = Column(Text)
    childrelation = relationship("baiscs_information", back_populates="awards")

class certificates(table_base):
    __tablename__ = 'certificates'
    certificatesId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId", ondelete="CASCADE"), nullable=False)
    certificateName = Column(Text)
    certificateIssueDate = Column(Text)
    certificateUrl = Column(Text)
    certificateIssuer = Column(Text)
    childrelation = relationship("baiscs_information", back_populates="certificates")

class publications(table_base):
    __tablename__ = 'publications'
    publicationsId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId", ondelete="CASCADE"), nullable=False)
    publicationTitle = Column(Text)
    publisher = Column(Text)
    publishedDate = Column(Text)
    publishedUrl = Column(Text)
    publicationSummary = Column(Text)
    childrelation = relationship("baiscs_information", back_populates="publications")

class skills(table_base):
    __tablename__ = 'skills'
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId", ondelete="CASCADE"), nullable=False)
    skillsId = Column(Integer, primary_key=True, nullable=False)
    skillName = Column(Text)
    skillLevel = Column(Text)
    skillKeywords = Column(Text)
    childrelation = relationship("baiscs_information", back_populates="skills")

class languages(table_base):
    __tablename__ = 'languages'
    languagesId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId", ondelete="CASCADE"), nullable=False)
    language = Column(Text)
    languageFluency = Column(Text)
    childrelation = relationship("baiscs_information", back_populates="languages")

class interests(table_base):
    __tablename__ = 'interests'
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId", ondelete="CASCADE"), nullable=False)
    interestsId = Column(Integer, primary_key=True, nullable=False)
    interestName = Column(Text)
    interestKeywords = Column(Text)
    childrelation = relationship("baiscs_information", back_populates="interests")

class references(table_base):
    __tablename__ = 'references'
    referenecesId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId", ondelete="CASCADE"), nullable=False)
    referrerName = Column(Text)
    reference = Column(Text)
    childrelation = relationship("baiscs_information", back_populates="references")

class projects(table_base):
    __tablename__ = 'projects'
    resumeId = Column(Integer, ForeignKey("basics_information.resumeId", ondelete="CASCADE"), nullable=False)
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
    childrelation = relationship("baiscs_information", back_populates="projects")



table_base.metadata.create_all(engine)