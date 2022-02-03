
from resumeTables import *
from sqlalchemy import schema
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from jsonschema import Draft7Validator
import json

with open('validationSchema.json') as sc:
    schema = json.load(sc)

# ------------------- RESUME INSERTION --------------------------- #

async def resume_insertion(resume):
    with connect_engine.connect() as session:
        with session.begin() as transaction:
            try:
                # --------- SECTION : BASICS --------- #
                
                basics_dict = {}
                basics_information_data = resume["basics"]
                for i in basics_information_data:
                    basics_dict[i] = basics_information_data[i]
                basics_dict["coverLetter"] = resume["coverLetter"]
                basics_dict.pop("location")
                basics_dict.pop("profiles")
                basics_query = insert(basics_information).values(**basics_dict)
                session.execute(basics_query)

                max_id = session.execute(f"select max(id) from basics_information").fetchall()
                for i in max_id:
                    resumeId = i[0]

                basics_location_dict = {}
                basics_location_dict["resumeId"] = resumeId
                basics_location_data = resume["basics"]["location"]
                for i in basics_location_data:
                    basics_location_dict[i] = basics_location_data[i]
                basics_location_query = insert(basics_location).values( **basics_location_dict)
                session.execute(basics_location_query)

                basics_profiles_dict = {}
                basics_profiles_dict["resumeId"] = resumeId
                basics_profiles_data = resume["basics"]["profiles"]
                for i in basics_profiles_data:
                    for n in i:
                        basics_profiles_dict[n] = i[n]
                    basics_profiles_query = insert(basics_profiles).values( **basics_profiles_dict)
                    session.execute(basics_profiles_query)

                # --------- SECTION : WORK --------- #
                work_dict = {}
                work_highlights_dict = {}
                work_keywords_dict = {}
                work_dict["resumeId"] = resumeId
                work_data = resume["work"]
                for i in work_data:
                    for n in i:
                        if n != "highlights":
                            if n != "keywords":
                                work_dict[n] = i[n]
                    work_query = insert(work).values(**work_dict)
                    session.execute(work_query)

                    work_max_id = session.execute(f"select max(workId) from work").fetchall()
                    for i in work_max_id:
                        work_id = i[0]

                    for i in work_data:
                        for n in i:
                            if n == "highlights":
                                work_highlights_data = i[n]
                    work_highlights_dict["workId"] = work_id
                    for whd in work_highlights_data:
                        work_highlights_dict["value"] = whd
                        work_highlights_query = insert(work_highlights).values(**work_highlights_dict)
                        session.execute(work_highlights_query)
                    
                    for i in work_data:
                        for n in i:
                            if n == "keywords":
                                work_keywords_data = i[n]
                    work_keywords_dict["workId"] = work_id
                    for wkd in work_keywords_data:
                        work_keywords_dict["value"] = wkd
                        work_keywords_query = insert(work_keywords).values(**work_keywords_dict)
                        session.execute(work_keywords_query)


                try:
                    # ---------- SECTION : VOLUNTEER --------- #
                    volunteer_data = resume["volunteer"]
                    volunteer_dict = {}
                    volunteer_highlights_dict = {}
                    volunteer_id = 1
                    volunteer_dict["resumeId"] = resumeId
                    for i in volunteer_data:
                        for n in i:
                            if n != "highlights":
                                volunteer_dict[n] = i[n]
                        volunteer_query = insert(volunteer).values(**volunteer_dict)
                        session.execute(volunteer_query)

                        volunteer_max_id = session.execute(f"select max(volunteerId) from volunteer").fetchall()
                        for i in volunteer_max_id:
                            volunteer_id = i[0]

                        for i in volunteer_data:
                            for n in i:
                                if n == "highlights":
                                    volunteer_highlights_data = i[n]
                        volunteer_highlights_dict["volunteerId"] = volunteer_id
                        for vhd in volunteer_highlights_data:
                            volunteer_highlights_dict["value"] = vhd
                            volunteer_highlights_query = insert(volunteer_highlights).values(**volunteer_highlights_dict)
                            session.execute(volunteer_highlights_query)

                except:
                    print("No volunteer datas. ")


                # ---------- SECTION : EDUCATION ---------- #
                education_data = resume["education"]
                education_dict = {}
                education_courses_dict = {}
                education_dict["resumeId"] = resumeId
                for i in education_data:
                    for n in i:
                        if n != "courses":        
                            education_dict[n] = i[n]
                    education_query = insert(education).values(**education_dict)
                    session.execute(education_query)

                    education_max_id = session.execute(f"select max(educationId) from education").fetchall()
                    for i in education_max_id:
                        education_id = i[0]

                    for i in education_data:
                            for n in i:
                                if n == "courses":
                                    education_courses_data = i[n]
                    education_courses_dict["educationId"] = education_id
                    for ecd in education_courses_data:
                        education_courses_dict["value"] = ecd
                        education_courses_query = insert(education_courses).values(**education_courses_dict)
                        session.execute(education_courses_query)
                
                # --------- SECTION : AWARDS ---------- #
                try:
                    awards_data = resume["awards"]
                    awards_dict = {}
                    awards_dict["resumeId"] = resumeId
                    for i in awards_data:
                        for n in i:
                            awards_dict[n] = i[n]
                        awards_query = insert(awards).values(**awards_dict)
                        session.execute(awards_query)

                except:
                    print("No awards datas. ")

                # --------- SECTION : CERTIFICATES --------- #
                try:
                    certificates_data = resume["certificates"]
                    certificates_dict = {}
                    certificates_dict["resumeId"] = resumeId
                    for i in certificates_data:
                        for n in i:
                            certificates_dict[n] = i[n]
                        certificates_query = insert(certificates).values(**certificates_dict)
                        session.execute(certificates_query)
                except:
                    print("No certificates datas.")

                # --------- SECTION : PUBLICATIONS --------- #
                try:
                    publications_data = resume["publications"]
                    publications_dict = {}
                    publications_dict["resumeId"] = resumeId
                    for i in publications_data:
                        for n in i:
                            publications_dict[n] = i[n]
                        publications_query = insert(publications).values(**publications_dict)
                        session.execute(publications_query)
                except:
                    print("Publications Data Missing")

                # --------- SECTION : SKILLS --------- #
                skills_data = resume["skills"]
                skills_dict = {}
                skills_keywords_dict = {}
                skills_dict["resumeId"] = resumeId
                for i in skills_data:
                    for n in i:
                        if n != "keywords":        
                            skills_dict[n] = i[n]
                    skills_query = insert(skills).values(**skills_dict)
                    session.execute(skills_query)

                    skills_max_id = session.execute(f"select max(skillsId) from skills").fetchall()
                    for i in skills_max_id:
                        skills_id = i[0]

                    for i in skills_data:
                            for n in i:
                                if n == "keywords":
                                    skills_keywords_data = i[n]
                    skills_keywords_dict["skillsId"] = skills_id
                    for skd in skills_keywords_data:
                        skills_keywords_dict["value"] = skd
                        skills_keywords_query = insert(skills_keywords).values(**skills_keywords_dict)
                        session.execute(skills_keywords_query)

                # --------- SECTION : LANGUAGES --------- #
                languages_data = resume["languages"]
                languages_dict = {}
                languages_dict["resumeId"] = resumeId
                for i in languages_data:
                    for n in i:
                        languages_dict[n] = i[n]
                    languages_query = insert(languages).values( **languages_dict)
                    session.execute(languages_query)

                # --------- SECTION : INTERESTS --------- #
                interests_data = resume["interests"]
                interests_dict = {}
                interests_keywords_dict = {}
                interests_dict["resumeId"] = resumeId
                for i in interests_data:
                    for n in i:
                        if n != "keywords":        
                            interests_dict[n] = i[n]
                    interests_query = insert(interests).values( **interests_dict)
                    session.execute(interests_query)

                    interests_max_id = session.execute(f"select max(interestsId) from interests").fetchall()
                    for i in interests_max_id:
                        interests_id = i[0]

                    for i in skills_data:
                            for n in i:
                                if n == "keywords":
                                    interests_keywords_data = i[n]
                    interests_keywords_dict["interestsId"] = interests_id
                    for ikd in interests_keywords_data:
                        interests_keywords_dict["value"] = ikd
                        interests_keywords_query = insert(interests_keywords).values(**interests_keywords_dict)
                        session.execute(interests_keywords_query)
   
                
                # --------- SECTION : REFERENCES --------- #
                try:
                    references_data = resume["references"]
                    references_dict = {}
                    references_dict["resumeId"] = resumeId
                    for i in references_data:
                        for n in i:
                            references_dict[n] = i[n]
                        references_query = insert(references).values(**references_dict)
                        session.execute(references_query)
                except:
                    print("No Referenecs included")

                # --------- SECTION : PROJECTS --------- #
                projects_data = resume["projects"]
                projects_dict = {}
                projects_keywords_dict = {}
                projects_highlights_dict = {}
                projects_roles_dict = {}
                projects_dict["resumeId"] = resumeId
                for i in projects_data:
                    for n in i:
                        if n != "keywords":
                            if n != "highlights":
                                if n != "roles":        
                                    projects_dict[n] = i[n]
                    projects_query = insert(projects).values( **projects_dict)
                    session.execute(projects_query)

                    projects_max_id = session.execute(f"select max(projectsId) from projects").fetchall()
                    for i in projects_max_id:
                        projects_id = i[0]

                    for i in projects_data:
                        for n in i:
                            if n != "keywords":
                                if n != "roles":
                                    if n == "highlights":
                                        projects_highlights_data = i[n]
                    projects_highlights_dict["projectsId"] = projects_id
                    for phd in projects_highlights_data:
                        projects_highlights_dict["value"] = phd
                        projects_highlights_query = insert(projects_highlights).values(**projects_highlights_dict)
                        session.execute(projects_highlights_query)

                    for i in projects_data:
                        for n in i:
                            if n != "roles":
                                if n != "highlights":
                                    if n == "keywords":
                                        projects_keywords_data = i[n]
                    projects_keywords_dict["projectsId"] = projects_id
                    for pkd in projects_keywords_data:
                        projects_keywords_dict["value"] = pkd
                        projects_keywords_query = insert(projects_keywords).values(**projects_keywords_dict)
                        session.execute(projects_keywords_query)

                    for i in projects_data:
                        for n in i:
                            if n != "highlights":
                                if n != "keywords":
                                    if n == "roles":
                                        projects_roles_data = i[n]
                    projects_roles_dict["projectsId"] = projects_id
                    for prd in projects_roles_data:
                        projects_roles_dict["value"] = prd
                        projects_roles_query = insert(projects_roles).values(**projects_roles_dict)
                        session.execute(projects_roles_query)
                    projects_id + projects_id + 1
            except:
                print("error")
                transaction.rollback()
                raise Exception("Data Insertion Error")
            else:
                transaction.commit()
            finally:
                transaction.close()

    return resumeId


# ---------------------------- GET RESUME -------------------------------- #


async def fetch_all_resume():

    basics_information_results = connect_engine.execute(
        "select * from basics_information inner join basics_location on basics_information.id = basics_location.resumeId;").all()
    basics_profiles_results = engine.execute("select * from basics_profiles").fetchall()
    work_results = engine.execute("select * from work").fetchall()
    work_highlights_results = engine.execute("select * from work_highlights").fetchall()
    work_keywords_results = engine.execute("select * from work_keywords").fetchall()
    volunteer_results = engine.execute("select * from volunteer").fetchall()
    volunteer_highlights_results = engine.execute(
        "select * from volunteer_highlights").fetchall()
    education_results = engine.execute("select * from education").fetchall()
    education_courses_results = engine.execute("select * from education_courses").fetchall()
    awards_results = engine.execute("select * from awards").fetchall()
    publications_results = engine.execute("select * from publications").fetchall()
    certificates_results = engine.execute("select * from certificates").fetchall()
    skills_results = engine.execute("select * from skills").fetchall()
    skills_keywords_results = engine.execute("select * from skills_keywords").fetchall()
    languages_results = engine.execute("select * from languages").fetchall()
    interests_results = engine.execute("select * from interests").fetchall()
    interests_keywords_results = engine.execute("select * from interests_keywords").fetchall()
    references_results = engine.execute("select * from `references`").fetchall()
    projects_results = engine.execute("select * from projects").fetchall()
    projects_highlights_results = engine.execute(
        "select * from projects_highlights").fetchall()
    projects_keywords_results = engine.execute("select * from projects_keywords").fetchall()
    projects_roles_results = engine.execute("select * from projects_roles").fetchall()

    resume = [
        {
            "id": i["id"],
            "coverLetter": i["coverLetter"],
            "basics":{
                "name": i["name"],
                "label":i["label"],
                "image":i["image"],
                "email":i["email"],
                "phone":i["phone"],
                "url":i["url"],
                "summary":i["summary"],
                "location":{
                    "address": i["address"],
                    "postalCode":i["postalCode"],
                    "city":i["city"],
                    "countryCode":i["countryCode"],
                    "region":i["region"]
                },
                "profiles":[
                    {
                        "network": p["network"],
                        "username":p["username"],
                        "url":p["url"]
                    }
                    for p in basics_profiles_results
                    if p["resumeId"] == i["id"]
                ]
            },
            "work":[
                {
                    "name": w["name"],
                    "location":w["location"],
                    "description":w["description"],
                    "position":w["position"],
                    "url":w["url"],
                    "startDate":w["startDate"],
                    "endDate":w["endDate"],
                    "summary":w["summary"],
                    "highlights":[
                        wh["value"]
                        for wh in work_highlights_results
                        if wh["workId"] == w["workId"]
                    ],
                    "keywords":[
                        wk["value"]
                        for wk in work_keywords_results
                        if wk["workId"] == w["workId"]
                    ]
                }
                for w in work_results
                if w["resumeId"] == i["id"]
            ],
            "volunteer":[
                {
                    "organization": v["organization"],
                    "position":v["position"],
                    "url":v["url"],
                    "startDate":v["startDate"],
                    "endDate":v["endDate"],
                    "summary":v["summary"],
                    "highlights":[
                        vh["value"]
                        for vh in volunteer_highlights_results
                        if vh["volunteerId"] == v["volunteerId"]
                    ]
                }
                for v in volunteer_results
                if v["resumeId"] == i["id"]
            ],
            "education":[
                {
                    "institution": e["institution"],
                    "url":e["url"],
                    "area":e["area"],
                    "studyType":e["studyType"],
                    "startDate":e["startDate"],
                    "endDate": e["endDate"],
                    "score": e["score"],
                    "courses":[
                        ec["value"]
                        for ec in education_courses_results
                        if ec["educationId"] == e["educationId"]
                    ]
                }
                for e in education_results
                if e["resumeId"] == i["id"]
            ],
            "awards":[
                {
                    "title": a["title"],
                    "date":a["date"],
                    "awarder":a["awarder"],
                    "summary":a["summary"]
                }
                for a in awards_results
                if a["resumeId"] == i["id"]
            ],
            "certificates":[
                {
                    "name": c["name"],
                    "date":c["date"],
                    "url":c["url"],
                    "issuer":c["issuer"]
                }
                for c in certificates_results
                if c["resumeId"] == i["id"]
            ],
            "publications":[
                {
                    "name": p["name"],
                    "publisher":p["publisher"],
                    "releaseDate":p["releaseDate"],
                    "url":p["url"],
                    "summary":p["summary"]
                }
                for p in publications_results
                if p["resumeId"] == i["id"]
            ],
            "skills":[
                {
                    "name": s["name"],
                    "level":s["level"],
                    "keywords":[
                        sk["value"]
                        for sk in skills_keywords_results
                        if sk["skillsId"] == s["skillsId"]
                    ]
                }
                for s in skills_results
                if s["resumeId"] == i["id"]
            ],
            "languages":[
                {
                    "language": l["language"],
                    "fluency":l["fluency"]
                }
                for l in languages_results
                if l["resumeId"] == i["id"]
            ],
            "interests":[
                {
                    "name": intre["name"],
                    "keywords":[
                        ik["value"]
                        for ik in interests_keywords_results
                        if ik["interestsId"] == intre["interestsId"]
                    ]
                }
                for intre in interests_results
                if intre["resumeId"] == i["id"]
            ],
            "references":[
                {
                    "name": r["name"],
                    "reference":r["reference"]
                }
                for r in references_results
                if r["resumeId"] == i["id"]
            ],
            "projects":[
                {
                    "name": pr["name"],
                    "description":pr["description"],
                    "highlights":[
                        prh["value"]
                        for prh in projects_highlights_results
                        if prh["projectsId"] == pr["projectsId"]
                    ],
                    "keywords":[
                        prk["value"]
                        for prk in projects_keywords_results
                        if prk["projectsId"] == pr["projectsId"]
                    ],
                    "startDate":pr["startDate"],
                    "endDate":pr["endDate"],
                    "url":pr["url"],
                    "roles":[
                        prro["value"]
                        for prro in projects_roles_results
                        if prro["projectsId"] == pr["projectsId"]
                    ],
                    "entity":pr["entity"],
                    "type":pr["type"]

                }
                for pr in projects_results
                if pr["resumeId"] == i["id"]
            ]
        }
        for i in basics_information_results
    ]

    return resume

# -------------------------------------------------------------------- #


# -------------- GET PARAMETERED RESUME ------------------------ #


async def requested_resume(request):
    user_requested_id = request.path_params['pid']
    resumes = await fetch_all_resume()
    for i in resumes:
        if i["id"] == user_requested_id:
            passed_resume = dict(
                [
                    (key, value)
                    for key, value in i.items()
                    if value != []
                ]
            )
            break
        else:
            passed_resume = "empty"

    return JSONResponse(passed_resume)

# --------------------------------------------------------------- #


async def resumes_fetch(request):
    jsonout = await fetch_all_resume()

    return JSONResponse(jsonout)


async def resume_validate_and_insert(request):
    # -----  VALIDATION  ----- #
    resume = await request.json()
    validator = Draft7Validator(schema)
    error_list = list(validator.iter_errors(resume))
    if len(error_list) == 0:
        print("no validation issue")
        resumeId = await resume_insertion(resume)

    return JSONResponse(resumeId)


app = Starlette(debug=True,  routes=[
    Route('/resume', resumes_fetch, methods=['GET']),
    Route('/', resume_validate_and_insert, methods=['POST']),
    Route('/resume/{pid:int}', requested_resume, methods=['GET']),
])
