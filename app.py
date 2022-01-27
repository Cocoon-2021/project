from itsdangerous import exc
from sqlalchemy import schema, create_engine
from sqlalchemy.orm import Session
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from jsonschema import Draft7Validator
import json

connect = create_engine(
    'mysql+mysqlconnector://root:password@localhost/resumedata', connect_args={'auth_plugin': 'mysql_native_password'})
print(connect)


with open('schema.json') as sc:
    schema = json.load(sc)


# ------------------- INSERTION --------------------------- #


async def dataInsertion(resume):
    with Session(connect) as session:
        try:
            coverLetter = resume["coverLetter"]
            basicsName = resume["basics"]["name"]
            basicsLabel = resume["basics"]["label"]
            basicsImage = resume["basics"]["image"]
            basicsEmail = resume["basics"]["email"]
            basicsPhone = resume["basics"]["phone"]
            basicsUrl = resume["basics"]["url"]
            basicsSummary = resume["basics"]["summary"]
            session.execute(
                f"insert into resume(coverLetter,name,label,image,email,phone,url,summary) values('{coverLetter}','{ basicsName}','{ basicsLabel}','{ basicsImage}','{ basicsEmail}','{ basicsPhone}','{ basicsUrl}','{ basicsSummary}')")
            idTaking = session.execute(
                f"select max(id) from resume").fetchall()
            for i in idTaking:
                resumeId = i[0]

            locationAddress = resume["basics"]["location"]["address"]
            locationPostalCode = resume["basics"]["location"]["postalCode"]
            locationCity = resume["basics"]["location"]["city"]
            locationCountyCode = resume["basics"]["location"]["countryCode"]
            locationRegion = resume["basics"]["location"]["region"]
            session.execute(
                f"insert into basics_location values({resumeId},'{locationAddress}','{locationPostalCode}','{locationCity}','{locationCountyCode}','{locationRegion}')")

            profiles = resume["basics"]["profiles"]
            for i in profiles:
                bp_network = i["network"]
                bp_username = i["username"]
                bp_url = i["url"]
                session.execute(
                    f"insert into basics_profiles values({resumeId},'{bp_network}','{bp_username}','{bp_url}')")

            work = resume["work"]
            workId = 1
            for i in work:
                workName = i["name"]
                workLocation = i["location"]
                workDescription = i["description"]
                workPosition = i["position"]
                workUrl = i["url"]
                workStartDate = i["startDate"]
                workEndDate = i["endDate"]
                workSummary = i["summary"]
                workHighlights = i["highlights"]
                workKeywords = i["keywords"]
                session.execute(
                    f"insert into work values({resumeId},{workId},'{workName}','{workLocation}','{workDescription}','{workPosition}','{workUrl}','{workStartDate}','{workEndDate}','{workSummary}')")
                for m in workHighlights:
                    highValues = m
                    session.execute(
                        f"insert into work_highlights values({resumeId},{workId},'{highValues}')")
                for n in workKeywords:
                    workKeywordsVal = n
                    session.execute(
                        f"insert into work_keywords values({resumeId},{workId},'{workKeywordsVal}')")
                workId = workId + 1

            try:
                volunteer = resume["volunteer"]
                volunteerId = 1
                for i in volunteer:
                    volunteerOrganization = i["organization"]
                    volunteerPosition = i["position"]
                    volunteerUrl = i["url"]
                    volunteerStartDate = i["startDate"]
                    volunteerEndDate = i["endDate"]
                    volunteerSummary = i["summary"]
                    volunteerHighlights = i["highlights"]
                    session.execute(
                        f"insert into volunteer values({resumeId},{volunteerId},'{volunteerOrganization}','{volunteerPosition}','{volunteerUrl}','{volunteerStartDate}','{volunteerEndDate}','{volunteerSummary}')")

                    for s in volunteerHighlights:
                        vHighValues = s
                        session.execute(
                            f"insert into volunteer_highlights values({resumeId},{volunteerId},'{vHighValues}')")
                    volunteerId = volunteerId + 1
            except:
                print("No volunteer datas. ")

            education = resume["education"]
            educationId = 1
            for i in education:
                educationInstitution = i["institution"]
                educationUrl = i["url"]
                educationArea = i["area"]
                educationStudyType = i["studyType"]
                educationStartDate = i["startDate"]
                educationEndDate = i["endDate"]
                educationScore = i["score"]
                educationCourses = i["courses"]
                session.execute(
                    f"insert into education values({resumeId},{educationId},'{educationInstitution}','{educationUrl}','{educationArea}','{educationStudyType}','{educationStartDate}','{educationEndDate}','{educationScore}')")
                for m in educationCourses:
                    eduCourse = m
                    session.execute(
                        f"insert into education_courses values({resumeId},{educationId},'{eduCourse}')")
                educationId = educationId + 1

            try:
                awards = resume["awards"]
                for i in awards:
                    awardsTitle = i["title"]
                    awardsDate = i["date"]
                    awardsAwarder = i["awarder"]
                    awardsSummary = i["summary"]
                    session.execute(
                        f"insert into awards values({resumeId},'{awardsTitle}','{awardsDate}','{awardsAwarder}','{awardsSummary}')")
            except:
                print("No awards datas. ")

            try:
                certificates = resume["certificates"]
                for i in certificates:
                    certName = i["name"]
                    certDate = i["date"]
                    certUrl = i["url"]
                    certIssuer = i["issuer"]
                    session.execute(
                        f"insert into certificates values({resumeId},'{certName}','{certDate}','{certUrl}','{certIssuer}')")
            except:
                print("No certificates datas.")

            try:
                publications = resume["publications"]
                for i in publications:
                    pubName = i["name"]
                    pubPublisher = i["publisher"]
                    pubReleaseDate = i["releaseDate"]
                    pubUrl = i["url"]
                    pubSummary = i["summary"]
                    session.execute(
                        f"insert into publications values({resumeId},'{pubName}','{pubPublisher}','{pubReleaseDate}','{pubUrl}','{pubSummary}')")
            except:
                print("Publications Data Missing")

            skills = resume["skills"]
            skillId = 1
            for i in skills:
                skillName = i["name"]
                skilLevel = i["level"]
                skillKeywords = i["keywords"]
                session.execute(
                    f"insert into skills values({resumeId},{skillId},'{skillName}','{skilLevel}')")
                for n in skillKeywords:
                    keywordValues = n
                    session.execute(
                        f"insert into skills_keywords values({resumeId},{skillId},'{keywordValues}')")
                skillId = skillId + 1

            languages = resume["languages"]
            for i in languages:
                langLanguage = i["language"]
                langFluency = i["fluency"]
                session.execute(
                    f"insert into languages values({resumeId},'{langLanguage}','{langFluency}')")

            interests = resume["interests"]
            intId = 1
            for i in interests:
                interestsName = i["name"]
                interestsKeyWord = i["keywords"]
                session.execute(
                    f"insert into interests values({resumeId},{intId},'{interestsName}')")

                for n in interestsKeyWord:
                    intrKeywords = n
                    session.execute(
                        f"insert into interests_keywords values({resumeId},{intId},'{intrKeywords}')")
                intId = intId + 1

            try:
                references = resume["references"]
                for i in references:
                    refName = i["name"]
                    refReference = i["reference"]
                    session.execute(
                        f"insert into `references` values({resumeId},'{refName}','{refReference}')")
            except:
                print("No Referenecs included")

            projects = resume["projects"]
            proId = 1
            for i in projects:
                projectName = i["name"]
                projectDescription = i["description"]
                projectStartDate = i["startDate"]
                projectEndDate = i["endDate"]
                projectUrl = i["url"]
                projectEntity = i["entity"]
                projectType = i["type"]
                projectHighlights = i["highlights"]
                projectKeywords = i["keywords"]
                projectRoles = i["roles"]
                session.execute(
                    f"insert into projects values({resumeId},{proId},'{projectName}','{projectDescription}','{projectStartDate}','{projectEndDate}','{projectUrl}','{projectEntity}','{projectType}')")
                for n in projectHighlights:
                    projectHighValues = n
                    session.execute(
                        f"insert into projects_highlights values({resumeId},{proId},'{projectHighValues}')")

                for m in projectKeywords:
                    projectKeyValues = m
                    session.execute(
                        f"insert into projects_keywords values({resumeId},{proId},'{projectKeyValues}')")

                for r in projectRoles:
                    projectRolesValues = r
                    session.execute(
                        f"insert into projects_roles values({resumeId},{proId},'{projectRolesValues}')")
                proId = proId + 1
        except:
            print("error")
            session.rollback()
            raise Exception("Data Insertion Error")
        else:
            session.commit()
        finally:
            session.close()

    return resumeId


# ---------------------------- GET DATA -------------------------------- #


async def fetchResume():
    outResult = connect.execute(
        "select * from resume inner join basics_location on resume.id = basics_location.resumeId;").fetchall()
    bpResult = connect.execute("select * from basics_profiles").fetchall()
    wrResults = connect.execute("select * from work").fetchall()
    whResults = connect.execute("select * from work_highlights").fetchall()
    wkResults = connect.execute("select * from work_keywords").fetchall()
    vResults = connect.execute("select * from volunteer").fetchall()
    vhResults = connect.execute(
        "select * from volunteer_highlights").fetchall()
    eResults = connect.execute("select * from education").fetchall()
    ecResults = connect.execute("select * from education_courses").fetchall()
    awResults = connect.execute("select * from awards").fetchall()
    pResults = connect.execute("select * from publications").fetchall()
    cResults = connect.execute("select * from certificates").fetchall()
    sResults = connect.execute("select * from skills").fetchall()
    skResults = connect.execute("select * from skills_keywords").fetchall()
    lResults = connect.execute("select * from languages").fetchall()
    iResults = connect.execute("select * from interests").fetchall()
    ikResults = connect.execute("select * from interests_keywords").fetchall()
    rResults = connect.execute("select * from `references`").fetchall()
    proResults = connect.execute("select * from projects").fetchall()
    prohResults = connect.execute(
        "select * from projects_highlights").fetchall()
    prokResults = connect.execute("select * from projects_keywords").fetchall()
    prorResults = connect.execute("select * from projects_roles").fetchall()

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
                    for p in bpResult
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
                        if vh["resumeId"] == i["id"] and vh["volId"] == v["id"]
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
                        if ec["resumeId"] == i["id"] and ec["eduId"] == e["id"]
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
                        if sk["resumeId"] == i["id"] and sk["skillId"] == s["id"]
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
                        if ik["resumeId"] == i["id"] and ik["intrId"] == intre["id"]
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
                        if prh["resumeId"] == i["id"] and prh["proId"] == pr["id"]
                    ],
                    "keywords":[
                        prk["value"]
                        for prk in prokResults
                        if prk["resumeId"] == i["id"] and prk["proId"] == pr["id"]
                    ],
                    "startDate":pr["startDate"],
                    "endDate":pr["endDate"],
                    "url":pr["url"],
                    "roles":[
                        prro["value"]
                        for prro in prorResults
                        if prro["resumeId"] == i["id"] and prro["proId"] == pr["id"]
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


# -------------- PARAMETER ------------------------ #


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

#---------------------------------------------------- #


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
