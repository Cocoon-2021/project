from sqlalchemy import schema,create_engine
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


async def firstInsert(apival):
    scsRate="basics and resume table done"
    id = apival["id"]
    coverLetter = apival["coverLetter"]
    global resumeId 
    resumeId = id
            
    basicsName = apival["basics"]["name"]
    basicsLabel = apival["basics"]["label"]
    basicsImage = apival["basics"]["image"]
    basicsEmail = apival["basics"]["email"]
    basicsPhone = apival["basics"]["phone"]
    basicsUrl = apival["basics"]["url"]
    basicsSummary = apival["basics"]["summary"]
    session.execute(f"insert into resume values({id},'{coverLetter}','{ basicsName}','{ basicsLabel}','{ basicsImage}','{ basicsEmail}','{ basicsPhone}','{ basicsUrl}','{ basicsSummary}')")


    locationAddress = apival["basics"]["location"]["address"]
    locationPostalCode = apival["basics"]["location"]["postalCode"]
    locationCity = apival["basics"]["location"]["city"]
    locationCountyCode = apival["basics"]["location"]["countryCode"]
    locationRegion = apival["basics"]["location"]["region"]
    session.execute(f"insert into basics_location values({resumeId},'{locationAddress}','{locationPostalCode}','{locationCity}','{locationCountyCode}','{locationRegion}')")


    profiles = apival["basics"]["profiles"]
    for i in profiles:
        bp_network = i["network"]
        bp_username = i["username"]
        bp_url = i["url"]
        session.execute(f"insert into basics_profiles values({resumeId},'{bp_network}','{bp_username}','{bp_url}')")

    return scsRate


async def workInsert(apival):
    scsRate = "work table done"
    work = apival["work"]
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
        session.execute(f"insert into work values({resumeId},{workId},'{workName}','{workLocation}','{workDescription}','{workPosition}','{workUrl}','{workStartDate}','{workEndDate}','{workSummary}')")
        for m in workHighlights:
            highValues = m
            session.execute(f"insert into work_highlights values({resumeId},{workId},'{highValues}')")
        for n in workKeywords:
            workKeywordsVal = n
            session.execute(f"insert into work_keywords values({resumeId},{workId},'{workKeywordsVal}')")
        workId = workId + 1
    return scsRate


async def volInsert(apival):
    volunteer=apival["volunteer"]
    scsRate = "volunteer section sucess"
    volunteerId = 1
    for i in volunteer:
        volunteerOrganization = i["organization"]
        volunteerPosition = i["position"]
        volunteerUrl = i["url"]
        volunteerStartDate = i["startDate"]
        volunteerEndDate = i["endDate"]
        volunteerSummary = i["summary"]
        volunteerHighlights = i["highlights"]
        session.execute(f"insert into volunteer values({resumeId},{volunteerId},'{volunteerOrganization}','{volunteerPosition}','{volunteerUrl}','{volunteerStartDate}','{volunteerEndDate}','{volunteerSummary}')")

        for n in volunteerHighlights:
            vHighValues = n
            session.execute(f"insert into volunteer_highlights values({resumeId},{volunteerId},'{vHighValues}')")
        volunteerId = volunteerId + 1
    return scsRate


async def eduInsert(apival):
    scsRate = "education section Done"
    education = apival["education"]
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
        session.execute(f"insert into education values({resumeId},{educationId},'{educationInstitution}','{educationUrl}','{educationArea}','{educationStudyType}','{educationStartDate}','{educationEndDate}','{educationScore}')")
        for m in educationCourses:
            eduCourse = m
            session.execute(f"insert into education_courses values({resumeId},{educationId},'{eduCourse}')")
        educationId = educationId + 1
    return scsRate


async def awardsInsert(apival):
    scsRate = "awards section done"
    awards=apival["awards"]
    for i in awards:
        awardsTitle=i["title"]
        awardsDate=i["date"]
        awardsAwarder=i["awarder"]
        awardsSummary=i["summary"]
        session.execute(f"insert into awards values({resumeId},'{awardsTitle}','{awardsDate}','{awardsAwarder}','{awardsSummary}')")

async def certInsert(apival):
    certificates = apival["certificates"]
    scsRate = "certificate section done"
    for i in certificates:
        certName = i["name"]
        certDate = i["date"]
        certUrl = i["url"]
        certIssuer = i["issuer"]
        session.execute(f"insert into certificates values({resumeId},'{certName}','{certDate}','{certUrl}','{certIssuer}')")

    return scsRate


async def pubInsert(apival):
    scsRate = "publication section Done"
    publications = apival["publications"]
    for i in publications:
        pubName = i["name"]
        pubPublisher = i["publisher"]
        pubReleaseDate = i["releaseDate"]
        pubUrl = i["url"]
        pubSummary = i["summary"]
        session.execute(f"insert into publications values({resumeId},'{pubName}','{pubPublisher}','{pubReleaseDate}','{pubUrl}','{pubSummary}')")
    return scsRate


async def skillInsert(apival):
    scsRate = "skill scruion done"
    skills = apival["skills"]
    skillId = 1
    for i in skills:
        skillName = i["name"]
        skilLevel = i["level"]
        skillKeywords = i["keywords"]
        session.execute(f"insert into skills values({resumeId},{skillId},'{skillName}','{skilLevel}')")
        for n in skillKeywords:
            keywordValues = n
            session.execute(f"insert into skills_keywords values({resumeId},{skillId},'{keywordValues}')")
        skillId = skillId + 1
    return scsRate


async def lanInsert(apival):
    scsRate = "language,interestes,refereneces section done"
    languages = apival["languages"]
    for i in languages:
        langLanguage = i["language"]
        langFluency = i["fluency"]
        session.execute(f"insert into languages values({resumeId},'{langLanguage}','{langFluency}')")
    return scsRate

async def interInsert(apival):
    scsRate = "interestes section done"
    interests = apival["interests"]
    intId = 1
    for i in interests:
        interestsName = i["name"]
        interestsKeyWord = i["keywords"]
        session.execute(f"insert into interests values({resumeId},{intId},'{interestsName}')")

        for n in interestsKeyWord:
            intrKeywords = n
            session.execute(f"insert into interests_keywords values({resumeId},{intId},'{intrKeywords}')")
        intId = intId + 1
    return scsRate


async def referencesInsert(apival):
    scsRate = "refereneces section done"
    references = apival["references"]
    for i in references:
        refName = i["name"]
        refReference = i["reference"]
        session.execute(f"insert into `references` values({resumeId},'{refName}','{refReference}')")
    return scsRate


async def projectInsert(apival):
    scsRate = "projects section done"  
    projects = apival["projects"]
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
        session.execute(f"insert into projects values({resumeId},{proId},'{projectName}','{projectDescription}','{projectStartDate}','{projectEndDate}','{projectUrl}','{projectEntity}','{projectType}')")
        for n in projectHighlights:
            projectHighValues = n
            session.execute(f"insert into projects_highlights values({resumeId},{proId},'{projectHighValues}')")
        
        for m in projectKeywords:
            projectKeyValues = m
            session.execute(f"insert into projects_keywords values({resumeId},{proId},'{projectKeyValues}')")

        for r in  projectRoles:
            projectRolesValues = r
            session.execute(f"insert into projects_roles values({resumeId},{proId},'{projectRolesValues}')")
        proId = proId + 1
    return scsRate

# ------------------------------------------------------------------ #

# ---------------------  VALIDATION  ------------------------------- #

async def dataIn(apival):
    validator = Draft7Validator(schema)
    checkList = list(validator.iter_errors(apival))
    if len(checkList) == 0:
        print("no validation issue")
        global session
        with Session(connect) as session:
            session.begin()
            try:
                await firstInsert(apival)
                await workInsert(apival)
                try:
                    await volInsert(apival)
                except:
                    print("no Volunteer Data")
                await eduInsert(apival)
                try:
                    await awardsInsert(apival)
                except:
                    print("no awards data")
                await certInsert(apival)
                await skillInsert(apival)
                try:
                    await pubInsert(apival)
                except:
                    print("no publication data")
                try:
                    await lanInsert(apival)
                except:
                    print("no language data")
                await interInsert(apival)
                try:
                    await referencesInsert(apival)
                except:
                    print("no refereneces data")
                await projectInsert(apival)
            except:
                session.rollback()
                checkList = "Data Insertion Error"
            else:
                session.commit()
            finally:
                session.close()
        checkList = "Data Insertion Sucessfull"
    else:
        print(checkList)
        checkList = str(checkList)

    return checkList

# ---------------------------------------------------------------------- #

# ---------------------------- GET DATA -------------------------------- #  


async def fetchData():
    outResult=connect.execute("select * from resume inner join basics_location on resume.id = basics_location.resumeId;").fetchall()
    bpResult = connect.execute("select * from basics_profiles").fetchall()
    wrResults = connect.execute("select * from work").fetchall()
    whResults = connect.execute("select * from work_highlights").fetchall()
    wkResults = connect.execute("select * from work_keywords").fetchall()
    vResults = connect.execute("select * from volunteer").fetchall()
    vhResults = connect.execute("select * from volunteer_highlights").fetchall()
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
    prohResults = connect.execute("select * from projects_highlights").fetchall()
    prokResults = connect.execute("select * from projects_keywords").fetchall()
    prorResults = connect.execute("select * from projects_roles").fetchall()


    content = [
            {
                "id":i["id"],
                "coverLetter": i["coverLetter"],
                "basics":{
                    "name":i["name"],
                    "label":i["label"],
                    "image":i["image"],
                    "email":i["email"],
                    "phone":i["phone"],
                    "url":i["url"],
                    "summary":i["summary"],
                    "location":{
                        "address":i["address"],
                        "postalCode":i["postalCode"],
                        "city":i["city"],
                        "countryCode":i["countryCode"],
                        "region":i["region"]
                    },
                    "profiles":[
                        {
                        "network":p["network"],
                        "username":p["username"],
                        "url":p["url"]
                    }
                    for p in bpResult
                    if p["resumeId"] == i["id"]
                ]
                },
                "work":[
                    {
                        "name":w["name"],
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
                        "organization":v["organization"],
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
                        "institution":e["institution"],
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
                        "title":a["title"],
                        "date":a["date"],
                        "awarder":a["awarder"],
                        "summary":a["summary"]
                    }
                    for a in awResults
                    if a["resumeId"] == i["id"]
                ],
                "certificates":[
                    {
                        "name":c["name"],
                        "date":c["date"],
                        "url":c["url"],
                        "issuer":c["issuer"]
                    }
                    for c in cResults
                    if c["resumeId"] == i["id"]
                ],
                "publications":[
                    {
                        "name":p["name"],
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
                        "name":s["name"],
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
                        "language":l["language"],
                        "fluency":l["fluency"]
                    }
                    for l in lResults
                    if l["resumeId"] == i["id"]
                ],
                "interests":[
                    {
                        "name":intra["name"],
                        "keywords":[
                            ik["value"]
                            for ik in ikResults
                            if ik["resumeId"] == i["id"] and ik["intrId"] == intra["id"]
                        ]
                    }
                    for intra in iResults
                    if intra["resumeId"] == i["id"]
                ],
                "references":[
                    {
                        "name":r["name"],
                        "reference":r["reference"]
                    }
                    for r in rResults
                    if r["resumeId"] == i["id"]
                ],
                "projects":[
                    {
                        "name":pr["name"],
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
    return content


# -------------- PARAMETER ------------------------ #


async def parmPass(request):
    userPassId = request.path_params['pid']
    fetchContent = await fetchData()
    for i in fetchContent:
        if i["id"] == userPassId:
            content2 = dict(
                [
                    (key, value) 
                    for key, value in i.items() 
                    if value != [] 
                ]
            )

            break
        else:
            content2 = "empty"
    
    return JSONResponse( content2)

#---------------------------------------------------- #


async def homepage(request):
    jsonout = await fetchData()

    return JSONResponse(jsonout)


async def homepost(request):
    global apival
    apival = await request.json()
    dataInVal = await dataIn(apival)

    return JSONResponse(dataInVal)


app = Starlette(debug=True,  routes=[
    Route('/', homepage, methods=['GET']),
    Route('/', homepost, methods=['POST']),
    Route('/{pid:int}',parmPass, methods=['GET']),
])
