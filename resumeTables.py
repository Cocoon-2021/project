from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, MetaData, ForeignKey, Text

engine = create_engine(
    'mysql+mysqlconnector://root:password@localhost/resumedata', connect_args={'auth_plugin': 'mysql_native_password'} 
    )
connect_engine = engine.connect()

resume_metadata = MetaData()
basics_information = Table('basics_information', resume_metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('coverLetter', Text),
    Column('name', Text),
    Column('label', Text),
    Column('image', Text),
    Column('email', Text),
    Column('phone', Text),
    Column('url', Text),
    Column('summary', Text),
    )

basics_location = Table('basics_location', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('address', Text),
    Column('postalCode', Text),
    Column('city', Text),
    Column('countryCode', Text),
    Column('region', Text)
    )

basics_profiles = Table('basics_profiles', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('network', Text),
    Column('username', Text),
    Column('url', Text)
    )

work = Table('work', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('id', Integer, nullable=False),
    Column('name', Text),
    Column('location', Text),
    Column('description', Text),
    Column('position', Text),
    Column('url', Text),
    Column('startDate', Text),
    Column('endDate', Text),
    Column('summary', Text)
    )

work_highlights = Table('work_highlights', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('workId', Integer, nullable=False),
    Column('value', Text)
    )

work_keywords = Table('work_keywords', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('workId', Integer, nullable=False),
    Column('value', Text)
    )

volunteer = Table('volunteer', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('id', Integer, nullable=False),
    Column('organization', Text),
    Column('position', Text),
    Column('url', Text),
    Column('startDate', Text),
    Column('endDate', Text),
    Column('summary', Text)
    )

volunteer_highlights = Table('volunteer_highlights', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('volunteerId', Integer, nullable=False),
    Column('value', Text)
    )

education = Table('education', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('id', Integer, nullable=False),
    Column('institution', Text),
    Column('url', Text),
    Column('area', Text),
    Column('studyType', Text),
    Column('startDate', Text),
    Column('endDate', Text),
    Column('score', Text)
    )

education_courses = Table('education_courses', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('educationId', Integer, nullable=False),
    Column('value', Text)
    )

awards = Table('awards', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('title', Text),
    Column('date', Text),
    Column('awarder', Text),
    Column('summary', Text)
    )

certificates = Table('certificates', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('name', Text),
    Column('date', Text),
    Column('url', Text),
    Column('issuer', Text)
    )

publications = Table('publications', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('name', Text),
    Column('publisher', Text),
    Column('releaseDate', Text),
    Column('url', Text),
    Column('summary', Text)
    )

skills = Table('skills', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('id', Integer, nullable=False),
    Column('name', Text),
    Column('level', Text)
    )

skills_keywords = Table('skills_keywords', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('skillsId', Integer, nullable=False),
    Column('value', Text)
    )

languages = Table('languages', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('language', Text),
    Column('fluency', Text)
    )

interests = Table('interests', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('id', Integer, nullable=False),
    Column('name', Text)
    )

interests_keywords = Table('interests_keywords', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('interestsId', Integer, nullable=False),
    Column('value', Text)
    )

references = Table('references', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('name', Text),
    Column('reference', Text)
    )

projects = Table('projects', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('id', Integer, nullable=False),
    Column('name', Text),
    Column('description', Text),
    Column('startDate', Text),
    Column('endDate', Text),
    Column('url', Text),
    Column('entity', Text),
    Column('type', Text),
    )

projects_highlights = Table('projects_highlights', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('projectsId', Integer, nullable=False),
    Column('value', Text)
    )

projects_keywords = Table('projects_keywords', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('projectsId', Integer, nullable=False),
    Column('value', Text)
    )

projects_roles = Table('projects_roles', resume_metadata,
    Column('resumeId', Integer, ForeignKey("basics_information.id"), nullable=False),
    Column('projectsId', Integer, nullable=False),
    Column('value', Text)
    )


resume_metadata.create_all(engine)




