from database_engine import connect_engine
from resume_tables import *
from sqlalchemy.sql import select
from starlette.responses import JSONResponse
import json


async def list_all_resume(): # --- function get list of resumes

    stmt = """select 
     basics_information.*,
     (select json_arrayagg(json_object("network", basics_profiles.network, "username", basics_profiles.username, "url", basics_profiles.url)) from basics_profiles where basics_profiles.resumeId = basics_information.id) as profiles ,
     (select json_arrayagg(json_object("name", work.name, "location", work.location, "description", work.description, "position", work.position,"url", work.url, "startDate", work.startDate, "endDate", work.endDate, "summary", work.summary, "highlights", work.highlights, "keywords", work.keywords)) from work where basics_information.id = work.resumeId) as work,
     (select json_arrayagg(json_object("organization", volunteer.organization, "position", volunteer.position,"url", volunteer.url, "startDate", volunteer.startDate, "endDate", volunteer.endDate, "highlights", volunteer.highlights))from volunteer where basics_information.id = volunteer.resumeId) as volunteer,
     (select json_arrayagg(json_object("institution", education.institution, "url", education.url, "area", education.area,"studyType", education.studyType, "startDate", education.startDate, "endDate", education.endDate, "score", education.score, "courses", education.courses)) from education where basics_information.id = education.resumeId) as education,
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
            "id": resume_row.id,
            "coverLetter": resume_row.coverLetter,
            "basics": {
                "name": resume_row.name,
                "label": resume_row.label,
                "image": resume_row.image,
                "email": resume_row.email,
                "phone": resume_row.phone,
                "url": resume_row.url,
                "summary": resume_row.summary,
                "location": {
                    "address": resume_row.address,
                    "postalCode": resume_row.postalCode,
                    "city": resume_row.city,
                    "countryCode": resume_row.countryCode,
                    "region": resume_row.region 
                },
                "profiles": json.loads(resume_row.profiles)
            },
            "work": json.loads(resume_row.work),
            "volunteer": json.loads(resume_row.volunteer),
            "education": json.loads(resume_row.education),
            "awards": json.loads(resume_row.awards),
            "certificates": json.loads(resume_row.certificates),
            "publications": json.loads(resume_row.publications),
            "skills": json.loads(resume_row.skills),
            "languages": json.loads(resume_row.languages),
            "interests": json.loads(resume_row.interests),
            "references": json.loads(resume_row.references),
            "projects": json.loads(resume_row.projects)
        } 
        for resume_row in query_results
    ]
    return resume_list



async def requested_resume(request): # --- function to get requested resume

    user_requested_id = request.path_params['pid']
    passed_resume = {}
    basics = {}
    location = {}
    resume_request_query = f"""select 
                                    basics_information.*,
                                    (select json_arrayagg(json_object("network", basics_profiles.network, "username", basics_profiles.username, "url", basics_profiles.url)) from basics_profiles where basics_profiles.resumeId = basics_information.id) as profiles ,
                                    (select json_arrayagg(json_object("name", work.name, "location", work.location, "description", work.description, "position", work.position,"url", work.url, "startDate", work.startDate, "endDate", work.endDate, "summary", work.summary, "highlights", work.highlights, "keywords", work.keywords)) from work where basics_information.id = work.resumeId) as work,
                                    (select json_arrayagg(json_object("organization", volunteer.organization, "position", volunteer.position,"url", volunteer.url, "startDate", volunteer.startDate, "endDate", volunteer.endDate, "highlights", volunteer.highlights))from volunteer where basics_information.id = volunteer.resumeId) as volunteer,
                                    (select json_arrayagg(json_object("institution", education.institution, "url", education.url, "area", education.area,"studyType", education.studyType, "startDate", education.startDate, "endDate", education.endDate, "score", education.score, "courses", education.courses)) from education where basics_information.id = education.resumeId) as education,
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
                                                                            left join projects on basics_information.id = projects.resumeId where basics_information.id = {user_requested_id} group by basics_information.id """

    resume_result = connect_engine.execute(resume_request_query)

    for resume_values in resume_result:
        # --- adding values to location dict --- #
        location["address"] = resume_values.address
        location["postalCode"] = resume_values.postalCode
        location["city"] = resume_values.city
        location["countryCode"] = resume_values.countryCode
        location["region"] = resume_values.region

        # --- adding values to basics dict --- #
        basics["name"] = resume_values.name
        basics["label"] = resume_values.label
        basics["image"] = resume_values.image
        basics["email"] = resume_values.email
        basics["phone"] = resume_values.phone
        basics["url"] = resume_values.url
        basics["summary"] = resume_values.summary
        basics["location"] = location
        basics["profiles"] = json.loads(resume_values.profiles)

        # --- adding data to requested resume from query result --- #
        passed_resume["id"] = resume_values.id
        passed_resume["coverLetter"] = resume_values.coverLetter
        passed_resume["basics"] = basics
        passed_resume["work"] = json.loads(resume_values.work),
        passed_resume["volunteer"] = json.loads(resume_values.volunteer),
        passed_resume["education"] =  json.loads(resume_values.education),
        passed_resume["awards"] = json.loads(resume_values.awards),
        passed_resume["certificates"] = json.loads(resume_values.certificates),
        passed_resume["publications"] = json.loads(resume_values.publications),
        passed_resume["skills"] = json.loads(resume_values.skills),
        passed_resume["languages"] = json.loads(resume_values.languages),
        passed_resume["interests"] = json.loads(resume_values.interests),
        passed_resume["references"] = json.loads(resume_values.references),
        passed_resume["projects"] = json.loads(resume_values.projects)
        
    
    # --- checking if resume dict is empty or not --- #
    if passed_resume:
        print("passing resume")
    else:
        print("nothing to pass")

    return JSONResponse(passed_resume)
