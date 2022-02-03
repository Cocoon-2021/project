from sqlalchemy import delete
from resumeTables import *
from sqlalchemy.sql import delete
from starlette.responses import JSONResponse

async def resume_deletion(request):
    user_requested_id = request.path_params['pid']

    return JSONResponse({"Deletion ID": user_requested_id})

