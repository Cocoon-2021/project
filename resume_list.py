from resume_tables import *
from sqlalchemy.sql import select
import json


async def list_all_resume():
    stmt = """select 
     basics_information.*,
     (select json_arrayagg(json_object("network", basics_profiles.network, "username", basics_profiles.username, "url", basics_profiles.url)) from basics_profiles where basics_profiles.resumeId = basics_information.id) as profiles ,
     (select json_arrayagg(json_object("name", work.name, "location", work.location, "description", work.description, "position", work.position,"url", work.url, "startDate", work.startDate, "endDate", work.endDate, "summary", work.summary, "highlights", work.highlights, "keywords", work.keywords)) from work where basics_information.id = work.resumeId) as work,
     (select json_arrayagg(json_object("organization", volunteer.organization, "position", volunteer.position,"url", volunteer.url, "startDate", volunteer.startDate, "endDate", volunteer.endDate, "highlights", volunteer.highlights))from volunteer where basics_information.id = volunteer.resumeId) as volunteer,
     (select json_arrayagg(json_object("institution", education.institution, "url", education.url, "area", education.area,"studyType", education.studyType, "startDate", education.startDate, "endDate", education.endDate, "score", education.score)) from education where basics_information.id = education.resumeId) as education,
     (select json_arrayagg(json_object("title", awards.title, "date", awards.date, "awarder", awards.awarder, "summary", awards.summary)) from awards where basics_information.id = awards.resumeId) as awards,
     (select json_arrayagg(json_object("name", certificates.name, "date", certificates.date, "url", certificates.url, "issuer", certificates.issuer)) from certificates where basics_information.id = certificates.resumeId) as certificates,
     (select json_arrayagg(json_object("name", publications.name, "publisher", publications.publisher,"releaseDate", publications.releaseDate, "url", publications.url, "summary", publications.summary)) from publications where basics_information.id = publications.resumeId) as publications,
     (select json_arrayagg(json_object("name", skills.name, "level", skills.level, "keywords", skills.keywords)) from skills where basics_information.id = skills.resumeId) as skills,
     (select json_arrayagg(json_object("language", languages.language, "fluency", languages.fluency)) from languages where basics_information.id = languages.resumeId) as languages,
     (select json_arrayagg(json_object("name", interests.name, "keywords", interests.keywords)) from interests where basics_information.id = interests.resumeId) as interests,
     (select json_arrayagg(json_object("name", references.name, "refrenece", references.reference)) from `references` where basics_information.id = `references`.resumeId) as `references`,
     (select json_arrayagg(json_object("name", projects.name, "description", projects.description, "startDate", projects.startDate, "endDate", projects.endDate,"url", projects.url, "entity", projects.entity, "type", projects.type, "highlights", projects.highlights, "keywords", projects.keywords, "roles", projects.roles)) from projects where basics_information.id = projects.resumeId) as projects
                    from basics_information left join basics_profiles on basics_information.id = basics_profiles.resumeId 
                                             inner join work on basics_information.id = work.resumeId
                                             left join volunteer on basics_information.id = volunteer.resumeId
                                             left join education on basics_information.id = education.resumeId
                                             left join awards on basics_information.id = awards.resumeId
                                             left join certificates on basics_information.id = awards.resumeId
                                             left join publications on basics_information.id = publications.resumeId
                                             left join skills on basics_information.id = publications.resumeId
                                             left join languages on basics_information.id = languages.resumeId
                                             left join interests on basics_information.id = interests.resumeId
                                             left join `references` on basics_information.id = `references`.resumeId
                                             left join projects on basics_information.id = projects.resumeId group by basics_information.id"""

    query_results = connect_engine.execute(stmt)

    resume_list = [
        {
            "id": row.id,
            "coverLetter": row.coverLetter,
            "basics": {
                "name": row.name,
                "label": row.label,
                "image": row.image,
                "email": row.email,
                "phone": row.phone,
                "url": row.url,
                "summary": row.summary,
                "location": {
                    "address": row.address,
                    "postalCode": row.postalCode,
                    "city": row.city,
                    "countryCode": row.countryCode,
                    "region": row.region 
                },
                "profiles": json.loads(row.profiles)
            },
            "work": json.loads(row.work),
            "volunteer": json.loads(row.volunteer),
            "education": json.loads(row.education),
            "awards": json.loads(row.awards),
            "certificates": json.loads(row.certificates),
            "publications": json.loads(row.publications),
            "skills": json.loads(row.skills),
            "languages": json.loads(row.languages),
            "interests": json.loads(row.interests),
            "references": json.loads(row.references),
            "projects": json.loads(row.projects)
        } 
        for row in query_results
    ]
    return resume_list
