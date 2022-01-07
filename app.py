from requests.api import request
from starlette.applications import Starlette
from starlette.responses import JSONResponse,PlainTextResponse
from starlette.requests import Request
from starlette.routing import Route
import mysql.connector, requests,json

abc=mysql.connector.connect(host="localhost",user="root",passwd="password",auth_plugin="mysql_native_password", database="RESUME")
db=abc.cursor()

def values():
    responseapi=requests.get("https://934f3f71-0be5-4ebc-8ce7-3f72ae4bddb6.mock.pstmn.io/resume/1")
    api=responseapi.json()
    return api

locals().update(values())
id=id
coverLetter=coverLetter
enableSourceDataDownload=enableSourceDataDownload
basics=basics
locals().update(basics)
name,label,image,email,phone,url,summary=name,label,image,email,phone,url,summary
location=location
locals().update(location)
address,postalCode,city,countryCode,region=address,postalCode,city,countryCode,region
profiles=profiles
lp=len(profiles)
net,uname,ur=list(),list(),list()
for i in profiles:
    locals().update(i)
    net.append(network)
    uname.append(username)
    ur.append(url)
network,username,url=net,uname,ur


work=work
education=education
awards=awards
publications=publications
skills=skills
languages=languages
interests=interests
references=references
projects=projects
meta=meta
__translation__=__translation__




#db.execute("insert into data(name,contact)values(blaash,12)")
async def homepage(request):
    print(id,network,username,url)

    
    '''#sql="insert into resume(id) values(%s)
    #val=(id)
    #sql1="insert into resume_0(id,resume_id,coverLetter,enableSourceDataDownload) values(%s,%s,%s,%s)"
    #val1=(id,id,coverLetter,enableSourceDataDownload)
    #sql2="insert into resume(id) values (%s)"'''

    '''val3=(email,image,label,name,phone)
    print(val3)
    sql3="insert into basics(email,image,label,name,phone,id) values(%s,%s,%s,%s,%s,%(id)s)"
    db.execute(sql3,val3)'''

    '''#db.execute("insert into resume values 7")
    #db.execute("insert into resume_0 values(%s,%s,%s,%s)",id,id,coverLetter,enableSourceDataDownload)'''

    abc.commit()

    return JSONResponse({"sucess":"blash"})





app= Starlette(debug=True, routes=[
    Route('/', homepage),
])