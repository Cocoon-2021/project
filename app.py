from mysql.connector.abstracts import MySQLConnectionAbstract
from requests import api
from requests.api import request
from sqlalchemy import schema
from sqlalchemy.sql.expression import insert
from sqlalchemy.util.langhelpers import portable_instancemethod
from starlette.applications import Starlette
from starlette.responses import JSONResponse,PlainTextResponse
from starlette.requests import Request
from starlette.routing import Route
from jsonschema import Draft7Validator
import mysql.connector,sqlalchemy, requests,json

connect=sqlalchemy.create_engine('mysql+mysqlconnector://root:password@localhost/RESUME',connect_args={'auth_plugin':'mysql_native_password'})
print(connect)

with open('schema.json') as sc:
    schema = json.load(sc)

'''abc=mysql.connector.connect(host="localhost",user="root",passwd="password",auth_plugin="mysql_native_password", database="RESUME")
db=abc.cursor()'''

async def value():
    responseapi=requests.get("https://934f3f71-0be5-4ebc-8ce7-3f72ae4bddb6.mock.pstmn.io/resume/1")
    api=responseapi.json()
    return api

async def dataIn():
    apival=await value()
    validator = Draft7Validator(schema)
    checkList =list(validator.iter_errors(apival))
    print(checkList)

    if len(checkList) == 0:
        print("no validation isuee")
        await valueInsertion()
    else:
        print(checkList)

    #sqlalchemy.insert(resume).values(name=) 
    # connect.execute(f"insert into resume(id) values('$apival.row[id]')")
    # for i in apival:
    #     print(i.get("id", {}))

async def valueInsertion():
    apival=await value()

    id,coverLetter,ESDD = apival["id"],apival["coverLetter"],apival["enableSourceDataDownload"]
    resume_id=id
    connect.execute(f"insert into resume(id) values({id})")
    

    b_name,b_label,b_image,b_email = apival["basics"]["name"],apival["basics"]["label"],apival["basics"]["image"],apival["basics"]["email"]
    b_phone,b_url,b_summary = apival["basics"]["phone"],apival["basics"]["url"],apival["basics"]["summary"]
    connect.execute(f"insert into resume_0 values({resume_id},{id},'{coverLetter}','{ESDD}')")

    l_address,l_postalCode,l_city = apival["basics"]["location"]["address"],apival["basics"]["location"]["postalCode"],apival["basics"]["location"]["city"]
    l_countyCode,l_region = apival["basics"]["location"]["countryCode"],apival["basics"]["location"]["region"]


    

    '''profiles=profiles
    lp=len(profiles)
    net,uname,ur=list(),list(),list()
    for i in profiles:
        locals().update(i)
        net.append(network)
        uname.append(username)
        ur.append(url)
    network,username,url=net,uname,ur
    print(id,network,username,url)

    work=work
    for i in work:
        locals().update(i)    
        wname.append(name)               #name
        wlocation.append(location)       #location (name to be changed)
        wdescription.append(description) #desciption
        wposition.append(position)       #position
        wurl.append(url)                #wurl
        wstartDate.append(startDate)     #startdate
        wendDate.append(endDate)         #endDate
        wsummary.append(summary)         #summury
        whighlights.append(highlights)   #highlights
        wkeywordas.append(keywords)      #keywords

    volunteer=volunteer
    for i in volunteer:
        locals().update(i)
        organization.append(organization)
        position.append(position)
        vurl.append(url)
        startDate.append(startDate)
        endDate.append(endDate)
        summary.append(summary)
        highlights.append(highlights)

    education=education
    for i in education:
        locals().update(i)
        institution.append(institution)
        e_url.append(url)
        e_area.append(area)
        e_studyType.append(studyType)
        e_startDate.append(startDate)
        e_endDate.append(endDate)
        e_score.append(score)
        e_courses.append(courses)
    awards=awards
    publications=publications
    skills=skills
    languages=languages
    interests=interests
    references=references
    projects=projects
    meta=meta
    __translation__=__translation__ '''
    




#db.execute("insert into data(name,contact)values(blaash,12)")
async def homepage(request):
    await dataIn()

    
    '''#sql="insert into resume(id) values(%s)
    #val=(id)
    #sql1="insert into resume_0(id,resume_id,coverLetter,enableSourceDataDownload) values(%s,%s,%s,%s)"
    #val1=(id,id,coverLetter,enableSourceDataDownload)
    #sql2="insert into resume(id) values (%s)"'''

    #sql="insert into basics(email,image,label,name,ohone,id) values((json.dumps(api)),(json.dumps(api)),(json.dumps(api)),(json.dumps(api)),(json.dumps(api)),(json.dumps(api))"
    #sql3=f"insert into basics(email,image,label,name,phone,id) values('{email}','{image}','{label}','{name}','{phone}',{id})"
    
    '''apival=await values()
    for items in apival:
        print(items)
        id=items.get["id"]
        print(id)
        coverLetter=items.get["coverLetter"]
        print(coverLetter)
        enableSourceDataDownload=items.get["enableSourceDataDownload"]
        print(coverLetter)'''
    
    #connect.execute(sql)


    '''#db.execute("insert into resume values 7")
    #db.execute("insert into resume_0 values(%s,%s,%s,%s)",id,id,coverLetter,enableSourceDataDownload)'''


    return JSONResponse({"sucess":"blash"})





app= Starlette(debug=True, routes=[
    Route('/', homepage),
])