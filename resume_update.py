from resume_tables import *
from sqlalchemy.sql import update,delete
from starlette.responses import JSONResponse

async def resume_edit_and_update(request):
    user_requested_id = request.path_params['pid']

    return JSONResponse({"update ID": user_requested_id})