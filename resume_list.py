from database_engine import connect_engine
from resume_tables import *
from starlette.responses import JSONResponse
import json


async def list_all_resume(request): # --- function get list of resumes

    resume_list = []
    fetch_resumes_query = """select 
                                json_object("resumeId",basics_information.resumeId,"resumeCoverLetter",basics_information.resumeCoverLetter,"basics",json_object("resumerName",basics_information.resumerName,"position",basics_information.position,"profilePicture",basics_information.profilePicture,"resumerEmail",basics_information.resumerEmail,"resumerPhone",basics_information.resumerPhone,"resumerUrl",basics_information.resumerUrl,"resumerSummary",basics_information.resumerSummary,"location",json_object("resumerAddress",basics_information.resumerAddress,"resumerPostalCode",basics_information.resumerPostalCode,"resumerCity",basics_information.resumerCity,"resumerCountryCode",basics_information.resumerCountryCode,"resumerRegion",basics_information.resumerRegion),"profiles",(select json_arrayagg(json_object("profileNetwork", basics_profiles.profileNetwork, "profileUsername", basics_profiles.profileUsername, "profileUrl", basics_profiles.profileUrl)) from basics_profiles where basics_profiles.resumeId = basics_information.resumeId)),
                                "work",(select json_arrayagg(json_object("companyName", work.companyName, "companyLocation", work.companyLocation, "workDescription", work.workDescription, "workPosition", work.workPosition,"companyUrl", work.companyUrl, "workStartDate", work.workStartDate, "workEndDate", work.workEndDate, "workSummary", work.workSummary, "workHighlights", work.workHighlights, "workKeywords", work.workKeywords)) from work where basics_information.resumeId = work.resumeId),
                                "volunteer",(select json_arrayagg(json_object("volunteerdOrganization", volunteer.volunteeredOrganization, "volunteeredPosition", volunteer.volunteeredPosition,"organizationUrl", volunteer.organizationUrl, "volunteeringStartDate", volunteer.volunteeringStartDate, "volunteeringEndDate", volunteer.volunteeringEndDate, "volunteeringHighlights", volunteer.volunteeringHighlights, "volunteeringSummary", volunteer.volunteeringSummary))from volunteer where basics_information.resumeId = volunteer.resumeId),
                                "education",(select json_arrayagg(json_object("educationInstitution", education.educationInstitution, "institutionUrl", education.institutionUrl, "educatedArea", education.educatedArea,"educatedStudyType", education.educatedStudyType, "educationStartDate", education.educationStartDate, "educationEndDate", education.educationEndDate, "educationScore", education.educationScore,"educatedCourses",(select json_arrayagg(education_courses.educatedCourses) from education_courses where education.educationId = education_courses.educationId))) from education where basics_information.resumeId = education.resumeId),
                                "awards",(select json_arrayagg(json_object("awardTitle", awards.awardTitle, "awardedDate", awards.awardedDate, "awarder", awards.awarder, "awardSummary", awards.awardSummary)) from awards where basics_information.resumeId = awards.resumeId),
                                "certificates",(select json_arrayagg(json_object("certificateName", certificates.certificateName, "certificateIssueDate", certificates.certificateIssueDate, "certificateUrl", certificates.certificateUrl, "certificateIssuer", certificates.certificateIssuer)) from certificates where basics_information.resumeId = certificates.resumeId),
                                "publications",(select json_arrayagg(json_object("publicationTitle", publications.publicationTitle, "publisher", publications.publisher,"publishedDate", publications.publishedDate, "publishedUrl", publications.publishedUrl, "publicationSummary", publications.publicationSummary)) from publications where basics_information.resumeId = publications.resumeId),
                                "skills",(select json_arrayagg(json_object("skillName", skills.skillName, "skillLevel", skills.skillLevel, "skillKeywords", skills.skillKeywords)) from skills where basics_information.resumeId = skills.resumeId),
                                "languages",(select json_arrayagg(json_object("languageName", languages.language, "languagesFluency", languages.languageFluency)) from languages where basics_information.resumeId = languages.resumeId),
                                "interests",(select json_arrayagg(json_object("interestName", interests.interestName, "interestKeywords", interests.interestKeywords)) from interests where basics_information.resumeId = interests.resumeId),
                                "refreneces",(select json_arrayagg(json_object("referrerName", references.referrerName, "refrenece", references.reference)) from `references` where basics_information.resumeId = `references`.resumeId),
                                "projects",(select json_arrayagg(json_object("projectName", projects.projectName, "projectDescription", projects.projectDescription, "projectStartDate", projects.projectStartDate, "projectEndDate", projects.projectEndDate,"projectUrl", projects.projectUrl, "projectEntity", projects.projectEntity, "projectType", projects.projectType, "projectHighlights", projects.projectHighlights, "projectKeywords", projects.projectKeywords, "projectRoles", projects.projectRoles)) from projects where basics_information.resumeId = projects.resumeId)) as resume
                                                from basics_information left join basics_profiles on basics_information.resumeId = basics_profiles.resumeId 
                                                                        left join work on basics_information.resumeId = work.resumeId
                                                                        left join volunteer on basics_information.resumeId = volunteer.resumeId
                                                                        left join education on basics_information.resumeId = education.resumeId
                                                                        left join education_courses on education_courses.educationId = education.educationId
                                                                        left join awards on basics_information.resumeId = awards.resumeId
                                                                        left join certificates on basics_information.resumeId = awards.resumeId
                                                                        left join publications on basics_information.resumeId = publications.resumeId
                                                                        left join skills on basics_information.resumeId = publications.resumeId
                                                                        left join languages on basics_information.resumeId = languages.resumeId
                                                                        left join interests on basics_information.resumeId = interests.resumeId
                                                                        left join `references` on basics_information.resumeId = `references`.resumeId
                                                                        left join projects on basics_information.resumeId = projects.resumeId group by basics_information.resumeId"""
    fetch_resumes_result = connect_engine.execute(fetch_resumes_query)

    for i in fetch_resumes_result:
        resume_list.append(json.loads(i.resume))
    
    if resume_list:
        print(" ------- passing resumes ------- ")
    else:
        raise Exception
        print(" ------- nothing to pass ------- ")
        
        

    # fetch_resumes_query = f"""select 
    #                             basics_information.*,
    #                             (select json_arrayagg(json_object("network", basics_profiles.network, "username", basics_profiles.username, "url", basics_profiles.url)) from basics_profiles where basics_profiles.resumeId = basics_information.resumeId) as profiles ,
    #                             (select json_arrayagg(json_object("name", work.name, "location", work.location, "description", work.description, "position", work.position,"url", work.url, "startDate", work.startDate, "endDate", work.endDate, "summary", work.summary, "highlights", work.highlights, "keywords", work.keywords)) from work where basics_information.resumeId = work.resumeId) as work,
    #                             (select json_arrayagg(json_object("organization", volunteer.organization, "position", volunteer.position,"url", volunteer.url, "startDate", volunteer.startDate, "endDate", volunteer.endDate, "highlights", volunteer.highlights))from volunteer where basics_information.resumeId = volunteer.resumeId) as volunteer,
    #                             (select json_arrayagg(json_object("institution", education.institution, "url", education.url, "area", education.area,"studyType", education.studyType, "startDate", education.startDate, "endDate", education.endDate, "score", education.score, "courses", education.courses)) from education where basics_information.resumeId = education.resumeId) as education,
    #                             (select json_arrayagg(json_object("title", awards.title, "date", awards.date, "awarder", awards.awarder, "summary", awards.summary)) from awards where basics_information.resumeId = awards.resumeId) as awards,
    #                             (select json_arrayagg(json_object("name", certificates.name, "date", certificates.date, "url", certificates.url, "issuer", certificates.issuer)) from certificates where basics_information.resumeId = certificates.resumeId) as certificates,
    #                             (select json_arrayagg(json_object("name", publications.name, "publisher", publications.publisher,"releaseDate", publications.releaseDate, "url", publications.url, "summary", publications.summary)) from publications where basics_information.resumeId = publications.resumeId) as publications,
    #                             (select json_arrayagg(json_object("name", skills.name, "level", skills.level, "keywords", skills.keywords)) from skills where basics_information.resumeId = skills.resumeId) as skills,
    #                             (select json_arrayagg(json_object("language", languages.language, "fluency", languages.fluency)) from languages where basics_information.resumeId = languages.resumeId) as languages,
    #                             (select json_arrayagg(json_object("name", interests.name, "keywords", interests.keywords)) from interests where basics_information.resumeId = interests.resumeId) as interests,
    #                             (select json_arrayagg(json_object("name", references.name, "refrenece", references.reference)) from `references` where basics_information.resumeId = `references`.resumeId) as `references`,
    #                             (select json_arrayagg(json_object("name", projects.name, "description", projects.description, "startDate", projects.startDate, "endDate", projects.endDate,"url", projects.url, "entity", projects.entity, "type", projects.type, "highlights", projects.highlights, "keywords", projects.keywords, "roles", projects.roles)) from projects where basics_information.resumeId = projects.resumeId) as projects
    #                                             from basics_information left join basics_profiles on basics_information.resumeId = basics_profiles.resumeId 
    #                                                                     left join work on basics_information.resumeId = work.resumeId
    #                                                                     left join volunteer on basics_information.resumeId = volunteer.resumeId
    #                                                                     left join education on basics_information.resumeId = education.resumeId
    #                                                                     left join awards on basics_information.resumeId = awards.resumeId
    #                                                                     left join certificates on basics_information.resumeId = awards.resumeId
    #                                                                     left join publications on basics_information.resumeId = publications.resumeId
    #                                                                     left join skills on basics_information.resumeId = publications.resumeId
    #                                                                     left join languages on basics_information.resumeId = languages.resumeId
    #                                                                     left join interests on basics_information.resumeId = interests.resumeId
    #                                                                     left join `references` on basics_information.resumeId = `references`.resumeId
    #                                                                     left join projects on basics_information.resumeId = projects.resumeId group by basics_information.resumeId"""

    # fetch_resumes_results = connect_engine.execute(fetch_resumes_query)

    # #   ---   adding resumes to a List   ---   #
    # resume_list = [
    #     {
    #         "id": resume_row.resumeId,
    #         "coverLetter": resume_row.coverLetter,
    #         "basics": {
    #             "name": resume_row.name,
    #             "label": resume_row.label,
    #             "image": resume_row.image,
    #             "email": resume_row.email,
    #             "phone": resume_row.phone,
    #             "url": resume_row.url,
    #             "summary": resume_row.summary,
    #             "location": {
    #                 "address": resume_row.address,
    #                 "postalCode": resume_row.postalCode,
    #                 "city": resume_row.city,
    #                 "countryCode": resume_row.countryCode,
    #                 "region": resume_row.region 
    #             },
    #             "profiles": json.loads(resume_row.profiles)
    #         },
    #         "work": json.loads(resume_row.work),
    #         "volunteer": json.loads(resume_row.volunteer),
    #         "education": json.loads(resume_row.education),
    #         "awards": json.loads(resume_row.awards),
    #         "certificates": json.loads(resume_row.certificates),
    #         "publications": json.loads(resume_row.publications),
    #         "skills": json.loads(resume_row.skills),
    #         "languages": json.loads(resume_row.languages),
    #         "interests": json.loads(resume_row.interests),
    #         "references": json.loads(resume_row.references),
    #         "projects": json.loads(resume_row.projects)
    #     } 
    #     for resume_row in fetch_resumes_results
    # ]
    return JSONResponse( resume_list )



async def requested_resume(request): # --- function to get requested resume

    user_requested_id = request.path_params['pid']
    fetch_resume_query = f"""select 
                                json_object("resumeId",basics_information.resumeId,"resumeCoverLetter",basics_information.resumeCoverLetter,"basics",json_object("resumerName",basics_information.resumerName,"position",basics_information.position,"profilePicture",basics_information.profilePicture,"resumerEmail",basics_information.resumerEmail,"resumerPhone",basics_information.resumerPhone,"resumerUrl",basics_information.resumerUrl,"resumerSummary",basics_information.resumerSummary,"location",json_object("resumerAddress",basics_information.resumerAddress,"resumerPostalCode",basics_information.resumerPostalCode,"resumerCity",basics_information.resumerCity,"resumerCountryCode",basics_information.resumerCountryCode,"resumerRegion",basics_information.resumerRegion),"profiles",(select json_arrayagg(json_object("profileNetwork", basics_profiles.profileNetwork, "profileUsername", basics_profiles.profileUsername, "profileUrl", basics_profiles.profileUrl)) from basics_profiles where basics_profiles.resumeId = basics_information.resumeId)),
                                "work",(select json_arrayagg(json_object("companyName", work.companyName, "companyLocation", work.companyLocation, "workDescription", work.workDescription, "workPosition", work.workPosition,"companyUrl", work.companyUrl, "workStartDate", work.workStartDate, "workEndDate", work.workEndDate, "workSummary", work.workSummary, "workHighlights", work.workHighlights, "workKeywords", work.workKeywords)) from work where basics_information.resumeId = work.resumeId),
                                "volunteer",(select json_arrayagg(json_object("volunteerdOrganization", volunteer.volunteeredOrganization, "volunteeredPosition", volunteer.volunteeredPosition,"organizationUrl", volunteer.organizationUrl, "volunteeringStartDate", volunteer.volunteeringStartDate, "volunteeringEndDate", volunteer.volunteeringEndDate, "volunteeringHighlights", volunteer.volunteeringHighlights, "volunteeringSummary", volunteer.volunteeringSummary))from volunteer where basics_information.resumeId = volunteer.resumeId),
                                "education",(select json_arrayagg(json_object("educationInstitution", education.educationInstitution, "institutionUrl", education.institutionUrl, "educatedArea", education.educatedArea,"educatedStudyType", education.educatedStudyType, "educationStartDate", education.educationStartDate, "educationEndDate", education.educationEndDate, "educationScore", education.educationScore,"educatedCourses",(select json_arrayagg(education_courses.educatedCourses) from education_courses where education.educationId = education_courses.educationId))) from education where basics_information.resumeId = education.resumeId),
                                "awards",(select json_arrayagg(json_object("awardTitle", awards.awardTitle, "awardedDate", awards.awardedDate, "awarder", awards.awarder, "awardSummary", awards.awardSummary)) from awards where basics_information.resumeId = awards.resumeId),
                                "certificates",(select json_arrayagg(json_object("certificateName", certificates.certificateName, "certificateIssueDate", certificates.certificateIssueDate, "certificateUrl", certificates.certificateUrl, "certificateIssuer", certificates.certificateIssuer)) from certificates where basics_information.resumeId = certificates.resumeId),
                                "publications",(select json_arrayagg(json_object("publicationTitle", publications.publicationTitle, "publisher", publications.publisher,"publishedDate", publications.publishedDate, "publishedUrl", publications.publishedUrl, "publicationSummary", publications.publicationSummary)) from publications where basics_information.resumeId = publications.resumeId),
                                "skills",(select json_arrayagg(json_object("skillName", skills.skillName, "skillLevel", skills.skillLevel, "skillKeywords", skills.skillKeywords)) from skills where basics_information.resumeId = skills.resumeId),
                                "languages",(select json_arrayagg(json_object("languageName", languages.language, "languagesFluency", languages.languageFluency)) from languages where basics_information.resumeId = languages.resumeId),
                                "interests",(select json_arrayagg(json_object("interestName", interests.interestName, "interestKeywords", interests.interestKeywords)) from interests where basics_information.resumeId = interests.resumeId),
                                "refreneces",(select json_arrayagg(json_object("referrerName", references.referrerName, "refrenece", references.reference)) from `references` where basics_information.resumeId = `references`.resumeId),
                                "projects",(select json_arrayagg(json_object("projectName", projects.projectName, "projectDescription", projects.projectDescription, "projectStartDate", projects.projectStartDate, "projectEndDate", projects.projectEndDate,"projectUrl", projects.projectUrl, "projectEntity", projects.projectEntity, "projectType", projects.projectType, "projectHighlights", projects.projectHighlights, "projectKeywords", projects.projectKeywords, "projectRoles", projects.projectRoles)) from projects where basics_information.resumeId = projects.resumeId)) as resume
                                                from basics_information left join basics_profiles on basics_information.resumeId = basics_profiles.resumeId 
                                                                        left join work on basics_information.resumeId = work.resumeId
                                                                        left join volunteer on basics_information.resumeId = volunteer.resumeId
                                                                        left join education on basics_information.resumeId = education.resumeId
                                                                        left join education_courses on education_courses.educationId = education.educationId
                                                                        left join awards on basics_information.resumeId = awards.resumeId
                                                                        left join certificates on basics_information.resumeId = awards.resumeId
                                                                        left join publications on basics_information.resumeId = publications.resumeId
                                                                        left join skills on basics_information.resumeId = publications.resumeId
                                                                        left join languages on basics_information.resumeId = languages.resumeId
                                                                        left join interests on basics_information.resumeId = interests.resumeId
                                                                        left join `references` on basics_information.resumeId = `references`.resumeId
                                                                        left join projects 
                                                                                        on basics_information.resumeId = projects.resumeId 
                                                                                                        where basics_information.resumeId = {user_requested_id} 
                                                                                                                        group by basics_information.resumeId"""
    fetch_resume_result = connect_engine.execute(fetch_resume_query)

    for i in fetch_resume_result:
        passed_resume = json.loads(i.resume)
    
    



    # passed_resume = {}
    # basics = {}
    # location = {}
    # resume_request_query = f"""select 
    #                                 basics_information.*,
    #                                 (select json_arrayagg(json_object("network", basics_profiles.network, "username", basics_profiles.username, "url", basics_profiles.url)) from basics_profiles where basics_profiles.resumeId = basics_information.resumeId) as profiles ,
    #                                 (select json_arrayagg(json_object("name", work.name, "location", work.location, "description", work.description, "position", work.position,"url", work.url, "startDate", work.startDate, "endDate", work.endDate, "summary", work.summary, "highlights", work.highlights, "keywords", work.keywords)) from work where basics_information.resumeId = work.resumeId) as work,
    #                                 (select json_arrayagg(json_object("organization", volunteer.organization, "position", volunteer.position,"url", volunteer.url, "startDate", volunteer.startDate, "endDate", volunteer.endDate, "highlights", volunteer.highlights))from volunteer where basics_information.resumeId = volunteer.resumeId) as volunteer,
    #                                 (select json_arrayagg(json_object("institution", education.institution, "url", education.url, "area", education.area,"studyType", education.studyType, "startDate", education.startDate, "endDate", education.endDate, "score", education.score, "courses", education.courses)) from education where basics_information.resumeId = education.resumeId) as education,
    #                                 (select json_arrayagg(json_object("title", awards.title, "date", awards.date, "awarder", awards.awarder, "summary", awards.summary)) from awards where basics_information.resumeId = awards.resumeId) as awards,
    #                                 (select json_arrayagg(json_object("name", certificates.name, "date", certificates.date, "url", certificates.url, "issuer", certificates.issuer)) from certificates where basics_information.resumeId = certificates.resumeId) as certificates,
    #                                 (select json_arrayagg(json_object("name", publications.name, "publisher", publications.publisher,"releaseDate", publications.releaseDate, "url", publications.url, "summary", publications.summary)) from publications where basics_information.resumeId = publications.resumeId) as publications,
    #                                 (select json_arrayagg(json_object("name", skills.name, "level", skills.level, "keywords", skills.keywords)) from skills where basics_information.resumeId = skills.resumeId) as skills,
    #                                 (select json_arrayagg(json_object("language", languages.language, "fluency", languages.fluency)) from languages where basics_information.resumeId = languages.resumeId) as languages,
    #                                 (select json_arrayagg(json_object("name", interests.name, "keywords", interests.keywords)) from interests where basics_information.resumeId = interests.resumeId) as interests,
    #                                 (select json_arrayagg(json_object("name", references.name, "refrenece", references.reference)) from `references` where basics_information.resumeId = `references`.resumeId) as `references`,
    #                                 (select json_arrayagg(json_object("name", projects.name, "description", projects.description, "startDate", projects.startDate, "endDate", projects.endDate,"url", projects.url, "entity", projects.entity, "type", projects.type, "highlights", projects.highlights, "keywords", projects.keywords, "roles", projects.roles)) from projects where basics_information.resumeId = projects.resumeId) as projects
    #                                                 from basics_information left join basics_profiles on basics_information.resumeId = basics_profiles.resumeId 
    #                                                                         left join work on basics_information.resumeId = work.resumeId
    #                                                                         left join volunteer on basics_information.resumeId = volunteer.resumeId
    #                                                                         left join education on basics_information.resumeId = education.resumeId
    #                                                                         left join awards on basics_information.resumeId = awards.resumeId
    #                                                                         left join certificates on basics_information.resumeId = awards.resumeId
    #                                                                         left join publications on basics_information.resumeId = publications.resumeId
    #                                                                         left join skills on basics_information.resumeId = publications.resumeId
    #                                                                         left join languages on basics_information.resumeId = languages.resumeId
    #                                                                         left join interests on basics_information.resumeId = interests.resumeId
    #                                                                         left join `references` on basics_information.resumeId = `references`.resumeId
    #                                                                         left join projects on basics_information.resumeId = projects.resumeId where basics_information.resumeId = {user_requested_id} group by basics_information.resumeId """

    # resume_result = connect_engine.execute(resume_request_query)

    # for resume_values in resume_result:
    #     # --- adding values to location dict --- #
    #     location["address"] = resume_values.address
    #     location["postalCode"] = resume_values.postalCode
    #     location["city"] = resume_values.city
    #     location["countryCode"] = resume_values.countryCode
    #     location["region"] = resume_values.region

    #     # --- adding values to basics dict --- #
    #     basics["name"] = resume_values.name
    #     basics["label"] = resume_values.label
    #     basics["image"] = resume_values.image
    #     basics["email"] = resume_values.email
    #     basics["phone"] = resume_values.phone
    #     basics["url"] = resume_values.url
    #     basics["summary"] = resume_values.summary
    #     basics["location"] = location
    #     basics["profiles"] = json.loads(resume_values.profiles)

    #     # --- adding data to requested resume from query result --- #
    #     passed_resume["id"] = resume_values.resumeId
    #     passed_resume["coverLetter"] = resume_values.coverLetter
    #     passed_resume["basics"] = basics
    #     passed_resume["work"] = json.loads(resume_values.work),
    #     passed_resume["volunteer"] = json.loads(resume_values.volunteer),
    #     passed_resume["education"] =  json.loads(resume_values.education),
    #     passed_resume["awards"] = json.loads(resume_values.awards),
    #     passed_resume["certificates"] = json.loads(resume_values.certificates),
    #     passed_resume["publications"] = json.loads(resume_values.publications),
    #     passed_resume["skills"] = json.loads(resume_values.skills),
    #     passed_resume["languages"] = json.loads(resume_values.languages),
    #     passed_resume["interests"] = json.loads(resume_values.interests),
    #     passed_resume["references"] = json.loads(resume_values.references),
    #     passed_resume["projects"] = json.loads(resume_values.projects)
        


    return JSONResponse( passed_resume )
