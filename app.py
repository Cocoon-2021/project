
from resumeTables import *
from sqlalchemy import schema
from sqlalchemy.orm import sessionmaker
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from jsonschema import Draft7Validator
import json
import databases

with open('validationSchema.json') as sc:
    schema = json.load(sc)

print(engine)

# database = databases.Database('mysql+mysqlconnector://root:password@localhost/resumedata', connect_args={'auth_plugin': 'mysql_native_password'} )
# print(database)



# ------------------- RESUME INSERTION --------------------------- #

async def dataInsertion(resume):
    
    try:
        # --------- SECTION : BASICS --------- #
        
        basics_dict = {}
        basics = resume["basics"]
        for i in basics:
            basics_dict[i] = basics[i]
        basics_dict["coverLetter"] = resume["coverLetter"]
        basics_query = basics_information.insert()
        connect_engine.execute(basics_query, **basics_dict)

        max_id = connect_engine.execute(f"select max(id) from basics_information").fetchall()
        for i in max_id:
            resumeId = i[0]

        basics_location_dict = {}
        basics_location_dict["resumeId"] = resumeId
        basicslocation = resume["basics"]["location"]
        for i in basicslocation:
            basics_location_dict[i] = basicslocation[i]
        basics_location_query = basics_location.insert()
        connect_engine.execute(basics_location_query, **basics_location_dict)

        basics_profiles_dict = {}
        basics_profiles_dict["resumeId"] = resumeId
        basicsprofiles = resume["basics"]["profiles"]
        for i in basicsprofiles:
            for n in i:
                basics_profiles_dict[n] = i[n]
            basics_profiles_query = basics_profiles.insert()
            connect_engine.execute(basics_profiles_query, **basics_profiles_dict)

        # --------- SECTION : WORK --------- #
        work_dict = {}
        work_highlights_dict = {}
        work_keywords_dict = {}
        work_id = 1
        work_dict["resumeId"] = resumeId
        work_dict["id"] = work_id
        work_data = resume["work"]
        for i in work_data:
            for n in i:
                work_dict[n] = i[n]
            work_query = work.insert()
            connect_engine.execute(work_query,**work_dict)

            work_highlights_data = work_dict["highlights"]
            work_highlights_dict["resumeId"] = resumeId
            work_highlights_dict["workId"] = work_id
            for whd in work_highlights_data:
                work_highlights_dict["value"] = whd
                work_highlights_query = work_highlights.insert()
                connect_engine.execute(work_highlights_query,**work_highlights_dict)
            
            work_keywords_data = work_dict["keywords"]
            work_keywords_dict["resumeId"] = resumeId
            work_keywords_dict["workId"] = work_id
            for wkd in work_keywords_data:
                work_keywords_dict["value"] = wkd
                work_keywords_query = work_keywords.insert()
                connect_engine.execute(work_keywords_query,**work_keywords_dict)

            work_id = work_id + 1

        try:
            # ---------- SECTION : VOLUNTEER --------- #
            volunteer_data = resume["volunteer"]
            volunteer_dict = {}
            volunteer_highlights_dict = {}
            volunteer_id = 1
            volunteer_dict["resumeId"] = resumeId
            volunteer_dict["id"] = volunteer_id
            for i in volunteer_data:
                for n in i:
                    volunteer_dict[n] = i[n]
                volunteer_query = volunteer.insert()
                connect_engine.execute(volunteer_query, **volunteer_dict)

                volunteer_highlights_data = volunteer_dict["highlights"]
                volunteer_highlights_dict["resumeId"] = resumeId
                volunteer_highlights_dict["volunteerId"] = "1"
                for vhd in volunteer_highlights_data:
                    volunteer_highlights_dict["value"] = vhd
                    volunteer_highlights_query = volunteer_highlights.insert()
                    connect_engine.execute(volunteer_highlights_query,**volunteer_highlights_dict)
            volunteer_id = volunteer_id + 1
        except:
            print("No volunteer datas. ")


        # ---------- SECTION : EDUCATION ---------- #
        education_data = resume["education"]
        education_dict = {}
        education_courses_dict = {}
        education_id = 1
        education_dict["resumeId"] = resumeId
        education_dict["id"] = education_id
        for i in education_data:
            for n in i:
                education_dict[n] = i[n]
            education_query = education.insert()
            connect_engine.execute(education_query, **education_dict)

            education_courses_data = education_dict["courses"]
            education_courses_dict["resumeId"] = resumeId
            education_courses_dict["educationId"] = education_id
            for ecd in education_courses_data:
                education_courses_dict["value"] = ecd
                education_courses_query = education_courses.insert()
                connect_engine.execute(education_courses_query,**education_courses_dict)
            education_id = education_id + 1
        
        # --------- SECTION : AWARDS ---------- #
        try:
            awards_data = resume["awards"]
            awards_dict = {}
            awards_dict["resumeId"] = resumeId
            for i in awards_data:
                for n in i:
                    awards_dict[n] = i[n]
                awards_query = awards.insert()
                connect_engine.execute(awards_query, **awards_dict)

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
                certificates_query = certificates.insert()
                connect_engine.execute(certificates_query, **certificates_dict)
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
                publications_query = publications.insert()
                connect_engine.execute(publications_query, **publications_dict)
        except:
            print("Publications Data Missing")

        # --------- SECTION : SKILLS --------- #
        skills_data = resume["skills"]
        skills_dict = {}
        skills_keywords_dict = {}
        skills_id = 1
        skills_dict["resumeId"] = resumeId
        skills_dict["id"] = skills_id
        for i in skills_data:
            for n in i:
                skills_dict[n] = i[n]
            skills_query = skills.insert()
            connect_engine.execute(skills_query, **skills_dict)

            skills_keywords_data = skills_dict["keywords"]
            skills_keywords_dict["resumeId"] = resumeId
            skills_keywords_dict["skillsId"] = "1"
            for skd in skills_keywords_data:
                skills_keywords_dict["value"] = skd
                skills_keywords_query = skills_keywords.insert()
                connect_engine.execute(skills_keywords_query,**skills_keywords_dict)
            skills_id = skills_id + 1

        # --------- SECTION : LANGUAGES --------- #
        languages_data = resume["languages"]
        languages_dict = {}
        languages_dict["resumeId"] = resumeId
        for i in languages_data:
            for n in i:
                languages_dict[n] = i[n]
            languages_query = languages.insert()
            connect_engine.execute(languages_query, **languages_dict)

        # --------- SECTION : INTERESTS --------- #
        interests_data = resume["interests"]
        interests_dict = {}
        interests_keywords_dict = {}
        interests_id = 1
        interests_dict["resumeId"] = resumeId
        interests_dict["id"] = interests_id
        for i in interests_data:
            for n in i:
                interests_dict[n] = i[n]
            interests_query = interests.insert()
            connect_engine.execute(interests_query, **interests_dict)

            interests_keywords_data = interests_dict["keywords"]
            interests_keywords_dict["resumeId"] = resumeId
            interests_keywords_dict["interestsId"] = "1"
            for ikd in interests_keywords_data:
                interests_keywords_dict["value"] = ikd
                interests_keywords_query = interests_keywords.insert()
                connect_engine.execute(interests_keywords_query,**interests_keywords_dict)
            interests_id = interests_id + 1
        
        # --------- SECTION : REFERENCES --------- #
        try:
            references_data = resume["references"]
            references_dict = {}
            references_dict["resumeId"] = resumeId
            for i in references_data:
                for n in i:
                    references_dict[n] = i[n]
                references_query = references.insert()
                connect_engine.execute(references_query, **references_dict)
        except:
            print("No Referenecs included")

        # --------- SECTION : PROJECTS --------- #
        projects_data = resume["projects"]
        projects_dict = {}
        projects_keywords_dict = {}
        projects_highlights_dict = {}
        projects_roles_dict = {}
        projects_id = 1
        projects_dict["resumeId"] = resumeId
        projects_dict["id"] = projects_id
        for i in projects_data:
            for n in i:
                projects_dict[n] = i[n]
            projects_query = projects.insert()
            connect_engine.execute(projects_query, **projects_dict)

            projects_highlights_data = projects_dict["highlights"]
            projects_highlights_dict["resumeId"] = resumeId
            projects_highlights_dict["projectsId"] = projects_id
            for phd in projects_highlights_data:
                projects_highlights_dict["value"] = phd
                projects_highlights_query = projects_highlights.insert()
                connect_engine.execute(projects_highlights_query,**projects_highlights_dict)

            projects_keywords_data = projects_dict["keywords"]
            projects_keywords_dict["resumeId"] = resumeId
            projects_keywords_dict["projectsId"] = projects_id
            for pkd in projects_keywords_data:
                projects_keywords_dict["value"] = pkd
                projects_keywords_query = projects_keywords.insert()
                connect_engine.execute(projects_keywords_query,**projects_keywords_dict)

            projects_roles_data = projects_dict["roles"]
            projects_roles_dict["resumeId"] = resumeId
            projects_roles_dict["projectsId"] = projects_id
            for prd in projects_roles_data:
                projects_roles_dict["value"] = prd
                projects_roles_query = projects_roles.insert()
                connect_engine.execute(projects_roles_query,**projects_roles_dict)
            projects_id + projects_id + 1
    except:
        print("error")
    #     session.rollback()
    #     raise Exception("Data Insertion Error")
    # else:
    #     session.commit()
    # finally:
    #     session.close()

    return resumeId


# ---------------------------- GET RESUME -------------------------------- #


async def fetchResume():
    outResult = engine.execute(
        "select * from basics_information inner join basics_location on basics_information.id = basics_location.resumeId;").fetchall()
    bpResults = engine.execute("select * from basics_profiles").fetchall()
    wrResults = engine.execute("select * from work").fetchall()
    whResults = engine.execute("select * from work_highlights").fetchall()
    wkResults = engine.execute("select * from work_keywords").fetchall()
    vResults = engine.execute("select * from volunteer").fetchall()
    vhResults = engine.execute(
        "select * from volunteer_highlights").fetchall()
    eResults = engine.execute("select * from education").fetchall()
    ecResults = engine.execute("select * from education_courses").fetchall()
    awResults = engine.execute("select * from awards").fetchall()
    pResults = engine.execute("select * from publications").fetchall()
    cResults = engine.execute("select * from certificates").fetchall()
    sResults = engine.execute("select * from skills").fetchall()
    skResults = engine.execute("select * from skills_keywords").fetchall()
    lResults = engine.execute("select * from languages").fetchall()
    iResults = engine.execute("select * from interests").fetchall()
    ikResults = engine.execute("select * from interests_keywords").fetchall()
    rResults = engine.execute("select * from `references`").fetchall()
    proResults = engine.execute("select * from projects").fetchall()
    prohResults = engine.execute(
        "select * from projects_highlights").fetchall()
    prokResults = engine.execute("select * from projects_keywords").fetchall()
    prorResults = engine.execute("select * from projects_roles").fetchall()

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
                    for p in bpResults
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
                        for wh in whResults
                        if wh["resumeId"] == i["id"] and wh["workId"] == w["id"]
                    ],
                    "keywords":[
                        wk["value"]
                        for wk in wkResults
                        if wk["resumeId"] == i["id"] and wk["workId"] == w["id"]
                    ]
                }
                for w in wrResults
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
                        for vh in vhResults
                        if vh["resumeId"] == i["id"] and vh["volunteerId"] == v["id"]
                    ]
                }
                for v in vResults
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
                        for ec in ecResults
                        if ec["resumeId"] == i["id"] and ec["educationId"] == e["id"]
                    ]
                }
                for e in eResults
                if e["resumeId"] == i["id"]
            ],
            "awards":[
                {
                    "title": a["title"],
                    "date":a["date"],
                    "awarder":a["awarder"],
                    "summary":a["summary"]
                }
                for a in awResults
                if a["resumeId"] == i["id"]
            ],
            "certificates":[
                {
                    "name": c["name"],
                    "date":c["date"],
                    "url":c["url"],
                    "issuer":c["issuer"]
                }
                for c in cResults
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
                for p in pResults
                if p["resumeId"] == i["id"]
            ],
            "skills":[
                {
                    "name": s["name"],
                    "level":s["level"],
                    "keywords":[
                        sk["value"]
                        for sk in skResults
                        if sk["resumeId"] == i["id"] and sk["skillsId"] == s["id"]
                    ]
                }
                for s in sResults
                if s["resumeId"] == i["id"]
            ],
            "languages":[
                {
                    "language": l["language"],
                    "fluency":l["fluency"]
                }
                for l in lResults
                if l["resumeId"] == i["id"]
            ],
            "interests":[
                {
                    "name": intre["name"],
                    "keywords":[
                        ik["value"]
                        for ik in ikResults
                        if ik["resumeId"] == i["id"] and ik["interestsId"] == intre["id"]
                    ]
                }
                for intre in iResults
                if intre["resumeId"] == i["id"]
            ],
            "references":[
                {
                    "name": r["name"],
                    "reference":r["reference"]
                }
                for r in rResults
                if r["resumeId"] == i["id"]
            ],
            "projects":[
                {
                    "name": pr["name"],
                    "description":pr["description"],
                    "highlights":[
                        prh["value"]
                        for prh in prohResults
                        if prh["resumeId"] == i["id"] and prh["projectsId"] == pr["id"]
                    ],
                    "keywords":[
                        prk["value"]
                        for prk in prokResults
                        if prk["resumeId"] == i["id"] and prk["projectsId"] == pr["id"]
                    ],
                    "startDate":pr["startDate"],
                    "endDate":pr["endDate"],
                    "url":pr["url"],
                    "roles":[
                        prro["value"]
                        for prro in prorResults
                        if prro["resumeId"] == i["id"] and prro["projectsId"] == pr["id"]
                    ],
                    "entity":pr["entity"],
                    "type":pr["type"]

                }
                for pr in proResults
                if pr["resumeId"] == i["id"]
            ]
        }
        for i in outResult
    ]


    return resume

# -------------------------------------------------------------------- #


# -------------- GET PARAMETERED RESUME ------------------------ #


async def resumeGetOne(request):
    userPassId = request.path_params['pid']
    fetchedResume = await fetchResume()
    for i in fetchedResume:
        if i["id"] == userPassId:
            parmResume = dict(
                [
                    (key, value)
                    for key, value in i.items()
                    if value != []
                ]
            )
            break
        else:
            parmResume = "empty"

    return JSONResponse(parmResume)

# --------------------------------------------------------------- #


async def resumeGetAll(request):
    jsonout = await fetchResume()

    return JSONResponse(jsonout)


async def resumeInsert(request):
    # -----  VALIDATION  ----- #
    resume = await request.json()
    validator = Draft7Validator(schema)
    checkList = list(validator.iter_errors(resume))
    if len(checkList) == 0:
        print("no validation issue")
        resumeId = await dataInsertion(resume)

    return JSONResponse(resumeId)


app = Starlette(debug=True,  routes=[
    Route('/resume', resumeGetAll, methods=['GET']),
    Route('/', resumeInsert, methods=['POST']),
    Route('/resume/{pid:int}', resumeGetOne, methods=['GET']),
])
