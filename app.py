from os import name
from mysql.connector.abstracts import MySQLConnectionAbstract
from requests import api
from requests.api import post, get
from sqlalchemy import schema
from sqlalchemy.sql.expression import insert, intersect, label
from sqlalchemy.util.langhelpers import portable_instancemethod
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.routing import Route
from jsonschema import Draft7Validator
import sqlalchemy
import json

connect = sqlalchemy.create_engine(
    'mysql+mysqlconnector://root:password@localhost/resumedata', connect_args={'auth_plugin': 'mysql_native_password'})
print(connect)

with open('schema.json') as sc:
    schema = json.load(sc)


# async def value():
#     responseapi = get("https://934f3f71-0be5-4ebc-8ce7-3f72ae4bddb6.mock.pstmn.io/resume/1")
#     api = responseapi.json()
#     return api

async def dataIn(apival):
    validator = Draft7Validator(schema)
    checkList = list(validator.iter_errors(apival))
    print(checkList)
    if len(checkList) == 0:
        print("no validation isuee")
        await valueInsertion(apival)
    else:
        print(checkList)

    return checkList



async def valueInsertion(apival):
    id = apival["id"]
    coverLetter = apival["coverLetter"]
    resumeId = id
    connect.execute(f"insert into resume values({resumeId},'{coverLetter}')")


    basicsName = apival["basics"]["name"]
    basicsLabel = apival["basics"]["label"]
    basicsImage = apival["basics"]["image"]
    basicsEmail = apival["basics"]["email"]
    basicsPhone = apival["basics"]["phone"]
    basicsUrl = apival["basics"]["url"]
    basicsSummary = apival["basics"]["summary"]

    connect.execute(f"insert into basics values({resumeId},'{ basicsName}','{ basicsLabel}','{ basicsImage}','{ basicsEmail}','{ basicsPhone}','{ basicsUrl}','{ basicsSummary}')")



    locationAddress = apival["basics"]["location"]["address"]
    locationPostalCode = apival["basics"]["location"]["postalCode"]
    locationCity = apival["basics"]["location"]["city"]
    locationCountyCode = apival["basics"]["location"]["countryCode"]
    locationRegion = apival["basics"]["location"]["region"]
    connect.execute(f"insert into basics_location values({resumeId},'{locationAddress}','{locationPostalCode}','{locationCity}','{locationCountyCode}','{locationRegion}')")


    profiles = apival["basics"]["profiles"]
    for i in profiles:
        bp_network = i["network"]
        bp_username = i["username"]
        bp_url = i["url"]
        connect.execute(f"insert into basics_profiles values({resumeId},'{bp_network}','{bp_username}','{bp_url}')")


    work = apival["work"]
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
        connect.execute(f"insert into work values({resumeId},'{workName}','{workLocation}','{workDescription}','{workPosition}','{workUrl}','{workStartDate}','{workEndDate}','{workSummary}')")
        for m in workHighlights:
            highValues = m
            connect.execute(f"insert into work_highlights values({resumeId},'{highValues}')")
        for n in workKeywords:
            workKeywordsVal = n
            connect.execute(f"insert into work_keywords values({resumeId},'{workKeywordsVal}')")


    volunteer=apival["volunteer"]
    for i in volunteer:
        volunteerOrganization = i["organization"]
        volunteerPosition = i["position"]
        volunteerUrl = i["url"]
        volunteerStartDate = i["startDate"]
        volunteerEndDate = i["endDate"]
        volunteerSummary = i["summary"]
        volunteerHighlights = i["highlights"]
        connect.execute(f"insert into volunteer values({resumeId},'{volunteerOrganization}','{volunteerPosition}','{volunteerUrl}','{volunteerStartDate}','{volunteerEndDate}','{volunteerSummary}')")
        for m in volunteerHighlights:
            vHighValues = m
            print(vHighValues)
            connect.execute(f"insert into volunteer_highlights values({resumeId},%s)",vHighValues)


    education = apival["education"]
    for i in education:
        educationInstitution = i["institution"]
        educationUrl = i["url"]
        educationArea = i["area"]
        educationStudyType = i["studyType"]
        educationStartDate = i["startDate"]
        educationEndDate = i["endDate"]
        educationScore = i["score"]
        educationCourses = i["courses"]
        connect.execute(f"insert into education values({resumeId},'{educationInstitution}','{educationUrl}','{educationArea}','{educationStudyType}','{educationStartDate}','{educationEndDate}','{educationScore}')")
        for m in educationCourses:
            eduCourse = m
            connect.execute(f"insert into education_courses values({resumeId},'{eduCourse}')")


    awards=apival["awards"]
    for i in awards:
        awardsTitle=i["title"]
        awardsDate=i["date"]
        awardsAwarder=i["awarder"]
        awardsSummary=i["summary"]
        connect.execute(f"insert into awards values({resumeId},'{awardsTitle}','{awardsDate}','{awardsAwarder}','{awardsSummary}')")



    publications = apival["publications"]
    for i in publications:
        pubName = i["name"]
        pubPublisher = i["publisher"]
        pubReleaseDate = i["releaseDate"]
        pubUrl = i["url"]
        pubSummary = i["summary"]
        connect.execute(f"insert into publications values({resumeId},'{pubName}','{pubPublisher}','{pubReleaseDate}','{pubUrl}','{pubSummary}')")



    skills = apival["skills"]
    for i in skills:
        skillName = i["name"]
        skilLevel = i["level"]
        skillKeywords = i["keywords"]
        connect.execute(f"insert into skills values({resumeId},'{skillName}','{skilLevel}')")
        for n in skillKeywords:
            keywordValues = n
            connect.execute(f"insert into skills_keywords values({resumeId},'{keywordValues}')")



    languages = apival["languages"]
    for i in languages:
        langLanguage = i["language"]
        langFluency = i["fluency"]
        connect.execute(f"insert into languages values({resumeId},'{langLanguage}','{langFluency}')")


    interests = apival["interests"]
    for i in interests:
        interestsName = i["name"]
        interestsKeyWord = i["keywords"]
        connect.execute(f"insert into interests values({resumeId},'{interestsName}')")

        for n in interestsKeyWord:
            intrKeywords = n
            connect.execute(f"insert into interests_keywords values({resumeId},'{intrKeywords}')")



    references = apival["references"]
    for i in references:
        refName = i["name"]
        refReference = i["reference"]
        connect.execute(f"insert into `references` values({resumeId},'{refName}','{refReference}')")


    id = id + 1
    return id




def fetchData():
    outResult=connect.execute("select resume.id,resume.coverLetter,basics.name,basics.label,basics.image,basics.email,basics.phone,basics.url,basics.summary,basics_location.address,basics_location.postalCode,basics_location.city,basics_location.countryCode,basics_location.region,basics_profiles.network,basics_profiles.username,basics_profiles.url from resume inner join basics inner join basics_location inner join basics_profiles on resume.id=basics.resume_id and resume.id = basics_location.resume_id and resume.id = basics_profiles.resume_id;").fetchall()
    bpResult = connect.execute("select basics_profiles.network,basics_profiles.username,basics_profiles.url from basics_profiles,resume where basics_profiles.resume_id = resume.id ").fetchall()
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
                    "url":i["summary"],
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
                        ],
                        "keywords":[
                            wk["value"]
                            for wk in wkResults
                        ]
                    }
                    for w in wrResults
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
                        ]
                    }
                    for v in vResults
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
                        ]
                        
                    }
                    for e in eResults
                ],
                "awards":[
                    {
                        "title":a["title"],
                        "date":a["date"],
                        "awarder":a["awarder"],
                        "summary":a["summary"]
                    }
                    for a in awResults
                ],
                "certificates":[
                    {
                        "name":c["name"],
                        "date":c["date"],
                        "url":c["url"],
                        "issuer":["issuer"]
                    }
                    for c in cResults
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
                ],
                "skills":[
                    {
                        "name":s["name"],
                        "level":s["level"],
                        "keywords":[
                            sk["value"]
                            for sk in skResults
                        ]
                    }
                    for s in sResults
                ],
                "languages":[
                    {
                        "language":l["language"],
                        "fluency":l["fluency"]
                    }
                    for l in lResults
                ],
                "interests":[
                    {
                        "name":i["name"],
                        "keywords":[
                            ik["value"]
                            for ik in ikResults
                        ]
                    }
                    for i in iResults
                ],
                "references":[
                    {
                        "name":r["name"],
                        "reference":r["reference"]
                    }
                    for r in rResults
                ],
                "projects":[
                    {
                        "name":pr["name"],
                        "description":pr["description"],
                        "highlights":[
                            prh["value"]
                            for prh in prohResults
                        ],
                        "keywords":[
                            prk["value"]
                            for prk in prokResults
                        ],
                        "startDate":pr["startDate"],
                        "endDate":pr["endDate"],
                        "url":pr["url"],
                        "roles":[
                            prro["value"]
                            for prro in prorResults
                        ],
                        "enitity":pr["entity"],
                        "type":pr["type"]

                    }
                    for pr in proResults
                ]


                
            }
            for i in outResult
    ]
    return content



async def homepage(request):
    
    jsonout = fetchData()
    print(jsonout)


    return JSONResponse(jsonout)

async def homepost(request):
    global apival
    apival = await request.json()
    await dataIn(apival)




    return JSONResponse("blash")


app = Starlette(debug=True,  routes=[
    Route('/', homepage, methods=['GET']),
    Route('/', homepost, methods=['POST'])
])
