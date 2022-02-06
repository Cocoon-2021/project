from sqlalchemy import delete
from database_engine import connect_engine
from resume_tables import *
from sqlalchemy.sql import delete
from starlette.responses import JSONResponse

async def resume_deletion(request):
    user_requested_id = request.path_params['pid']

    work_delteion_query = delete(work).where(work.resumeId == user_requested_id)
    basics_profiles_deletion_query = delete(basics_profiles).where(basics_profiles.resumeId == user_requested_id)
    volunteer_deletion_query = delete(volunteer).where(volunteer.resumeId == user_requested_id)
    connect_engine.execute(work_delteion_query,basics_profiles_deletion_query,volunteer_deletion_query)
    return JSONResponse({"Deletion ID": user_requested_id})

