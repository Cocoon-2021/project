from requests.api import request
from starlette.applications import Starlette
from starlette.responses import JSONResponse,PlainTextResponse
from starlette.requests import Request
from starlette.routing import Route
import mysql.connector, requests,json

abc=mysql.connector.connect(host="localhost",user="root",passwd="password",auth_plugin="mysql_native_password", database="test")
db=abc.cursor()

def values():
    apiresp=requests.get("https://934f3f71-0be5-4ebc-8ce7-3f72ae4bddb6.mock.pstmn.io/resume")
    api=apiresp.json()[0] 
    return api

locals().update(values())
id=id
coverLetter=coverLetter
basics=basics




#db.execute("insert into data(name,contact)values(blaash,12)")
async def homepage(request):
    print(id,coverLetter,basics)

    '''apiresp=requests.get("https://934f3f71-0be5-4ebc-8ce7-3f72ae4bddb6.mock.pstmn.io/resume")
    api=apiresp.json()[0]  
    for items in api:
        fact=api['fact']
        print(fact)
        length=api["length"]
        print(length)
        sql="insert into data(name,contact) values(%s,%s)"
        val=(fact,length)
        db.execute(sql,val)
        abc.commit()'''

    return PlainTextResponse("sucess")





app= Starlette(debug=True, routes=[
    Route('/', homepage),
])