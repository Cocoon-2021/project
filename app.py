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
        await valueInsertion()
    else:
        print(checkList)

    return checkList

async def valueInsertion(apival):
    id = apival["id"]
    coverLetter = apival["coverLetter"]
    ESDD = apival["enableSourceDataDownload"]
    resume_id = id
    connect.execute(f"insert into resume values({resume_id},'{coverLetter}','{ESDD}')")


    basicsName = apival["basics"]["name"]
    basicsLabel = apival["basics"]["label"]
    basicsImage = apival["basics"]["image"]
    basicsEmail = apival["basics"]["email"]
    basicsPhone = apival["basics"]["phone"]
    basicsUrl = apival["basics"]["url"]
    basicsSummary = apival["basics"]["summary"]
    bId = 1
    connect.execute(f"insert into basics values({resume_id},{bId},'{ basicsName}','{ basicsLabel}','{ basicsImage}','{ basicsEmail}','{ basicsPhone}','{ basicsUrl}','{ basicsSummary}')")
    bId = bId + 1


    locationAddress = apival["basics"]["location"]["address"]
    locationPostalCode = apival["basics"]["location"]["postalCode"]
    locationCity = apival["basics"]["location"]["city"]
    locationCountyCode = apival["basics"]["location"]["countryCode"]
    locationRegion = apival["basics"]["location"]["region"]
    basicsId = 1
    connect.execute(f"insert into basics_location values({basicsId},{id},'{locationAddress}','{locationPostalCode}','{locationCity}','{locationCountyCode}','{locationRegion}')")


    profiles = apival["basics"]["profiles"]
    bpId=1
    for i in profiles:
        bp_network = i["network"]
        bp_username = i["username"]
        bp_url = i["url"]
        bpId = bpId + 1
        connect.execute(f"insert into basics_profiles values({basicsId},{bpId},'{bp_network}','{bp_username}','{bp_url}')")
    basicsId = basicsId + 1


    work = apival["work"]
    wId = 1
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
        connect.execute(f"insert into work values({resume_id},{wId},'{workName}','{workLocation}','{workDescription}','{workPosition}','{workUrl}','{workStartDate}','{workEndDate}','{workSummary}')")
        whId = 1
        wkId = 1
        for m in workHighlights:
            highValues = m
            connect.execute(f"insert into work_highlights values({wId},{whId},'{highValues}')")
            whId = whId+1
        for n in workKeywords:
            workKeywordsVal = n
            connect.execute(f"insert into work_keywords values({wId},{wkId},'{workKeywordsVal}')")
            wkId = wkId + 1
        wId = wId+1


    volunteer=apival["volunteer"]
    vId = 1
    for i in volunteer:
        volunteerOrganization = i["organization"]
        volunteerPosition = i["position"]
        volunteerUrl = i["url"]
        volunteerStartDate = i["startDate"]
        volunteerEndDate = i["endDate"]
        volunteerSummary = i["summary"]
        volunteerHighlights = i["highlights"]
        connect.execute(f"insert into volunteer values({resume_id},{vId},'{volunteerOrganization}','{volunteerPosition}','{volunteerUrl}','{volunteerStartDate}','{volunteerEndDate}','{volunteerSummary}')")
        vhId = 1
        for m in volunteerHighlights:
            vHighValues = m
            print(vHighValues)
            #connect.execute(f"insert into volunteer_highlights values({vId},{vhId},'{vHighValues}')")
            vhId = vhId + 1
        vId = vId + 1


    education = apival["education"]
    eduId = 1
    for i in education:
        educationInstitution = i["institution"]
        educationUrl = i["url"]
        educationArea = i["area"]
        educationStudyType = i["studyType"]
        educationStartDate = i["startDate"]
        educationEndDate = i["endDate"]
        educationScore = i["score"]
        educationCourses = i["courses"]
        connect.execute(f"insert into education values({resume_id},{eduId},'{educationInstitution}','{educationUrl}','{educationArea}','{educationStudyType}','{educationStartDate}','{educationEndDate}','{educationScore}')")
        edHiId = 1
        for m in educationCourses:
            eduCourse = m
            connect.execute(f"insert into education_courses values({eduId},{edHiId},'{eduCourse}')")
            edHiId = edHiId + 1


    awards=apival["awards"]
    aId = 1
    for i in awards:
        awardsTitle=i["title"]
        awardsDate=i["date"]
        awardsAwarder=i["awarder"]
        awardsSummary=i["summary"]
        connect.execute(f"insert into awards values({resume_id},{aId},'{awardsTitle}','{awardsDate}','{awardsAwarder}','{awardsSummary}')")
        aId = aId + 1



    publications = apival["publications"]
    pId = 1
    for i in publications:
        pubName = i["name"]
        pubPublisher = i["publisher"]
        pubReleaseDate = i["releaseDate"]
        pubUrl = i["url"]
        pubSummary = i["summary"]
        connect.execute(f"insert into publications values({resume_id},{pId},'{pubName}','{pubPublisher}','{pubReleaseDate}','{pubUrl}','{pubSummary}')")
        pId = pId + 1



    skills = apival["skills"]
    sId = 1
    for i in skills:
        skillName = i["name"]
        skilLevel = i["level"]
        skillKeywords = i["keywords"]
        connect.execute(f"insert into skills values({resume_id},{sId},'{skillName}','{skilLevel}')")
        for n in skillKeywords:
            keywordValues = n
            sKId = 1
            #connect.execute(f"insert into skills_keywords values({sId},{sKId},'{keywordValues}')")
            skId = sKId + 1
        sId = sId + 1



    languages = apival["languages"]
    langId = 1
    for i in languages:
        langLanguage = i["language"]
        langFluency = i["fluency"]
        connect.execute(f"insert into languages values({resume_id},{langId},'{langLanguage}','{langFluency}')")
        langId = langId + 1


    interests = apival["interests"]
    intrId = 1
    intrKeyId = 1
    for i in interests:
        interestsName = i["name"]
        interestsKeyWord = i["keywords"]
        connect.execute(f"insert into interests values({resume_id},{intrId},'{interestsName}')")

        for n in interestsKeyWord:
            intrKeywords = n
            connect.execute(f"insert into interests_keywords values({intrId},{intrKeyId},'{intrKeywords}')")
            intrKeyId = intrKeyId + 1
        intrId = intrId + 1



    references = apival["references"]
    refId = 1
    for i in references:
        refName = i["name"]
        refReference = i["reference"]
        #connect.execute(f"insert into references values({resume_id},{refId},'{refName}','{refReference}')")
        refId = refId + 1


    id = id + 1
    return id




def fetchData():
    testDict = dict()
    outPut = connect.execute("select resume.id,resume.coverLetter,basics.name,basics.label,basics.image from resume inner join basics on resume.id = basics.resume_id " ).fetchall()
    qResult = [dict(row) for row in outPut]
    # print({json.dumps(outPut)})
    return qResult


#db.execute("insert into data(name,contact)values(blaash,12)")
async def homepage(request):
    
    jsonout = fetchData()
    print(jsonout)


    return JSONResponse(jsonout)

async def homepost(request):
    global apival
    apival = await request.json()
    await valueInsertion(apival)




    return JSONResponse("blash")


app = Starlette(debug=True,  routes=[
    Route('/', homepage, methods=['GET']),
    Route('/', homepost, methods=['POST'])
])
