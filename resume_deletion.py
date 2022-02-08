from sqlalchemy import delete
from database_engine import connect_engine
from resume_tables import *
from sqlalchemy.sql import delete
from starlette.responses import JSONResponse

async def resume_deletion(request):
    user_requested_id = request.path_params['pid']

    work_deleteion_query = delete(basics_information).where(basics_information.resumeId == user_requested_id)
    connect_engine.execute(work_deleteion_query)

    return JSONResponse({"Deleted ID ": user_requested_id})

