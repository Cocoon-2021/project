from sqlalchemy import create_engine

# --------- Engine creation ---------- #
engine = create_engine(
    'mysql+mysqlconnector://root:password@localhost/resumedata', connect_args={'auth_plugin': 'mysql_native_password'} 
    )
connect_engine = engine.connect()
# ------------------------------------- #