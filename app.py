
from resume_tables import *
from database_engine import connect_engine
from resume_deletion import resume_deletion
from resume_update import resume_edit_and_update
from resume_list import list_all_resume,requested_resume
from sqlalchemy import schema
from sqlalchemy.sql import insert
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.routing import Route
from jsonschema import Draft7Validator
import json

with open('validationSchema.json') as sc:
    schema = json.load(sc)


# ------------------- RESUME INSERTION --------------------------- #

async def resume_insertion(resume):
    with connect_engine.connect() as session:
        with session.begin() as transaction:
            try:
                # --------- SECTION : BASICS --------- #

                basics_dict = {}
                basics_information_data = resume["basics"]
                for basics_items in basics_information_data:
                    basics_dict[basics_items] = basics_information_data[basics_items]
                basics_dict["resumeCoverLetter"] = resume["resumeCoverLetter"]
                basics_dict.pop("location")
                basics_dict.pop("profiles")

                basics_location_dict = {}
                basics_location_data = resume["basics"]["location"]
                for basics_location_items in basics_location_data:
                    basics_location_dict[basics_location_items] = basics_location_data[basics_location_items]
                basics_dict.update(basics_location_dict)
                basics_query = insert(basics_information).values(**basics_dict)
                session.execute(basics_query)

                max_id = session.execute(
                    f"select max(resumeId) from basics_information").fetchall()
                for i in max_id:
                    resumeId = i[0]

                basics_profiles_dict = {}
                basics_profiles_dict["resumeId"] = resumeId
                basics_profiles_data = resume["basics"]["profiles"]
                for basics_profiles_items in basics_profiles_data:
                    for item_value in basics_profiles_items:
                        basics_profiles_dict[item_value] = basics_profiles_items[item_value]
                    basics_profiles_query = insert(
                        basics_profiles).values(**basics_profiles_dict)
                    session.execute(basics_profiles_query)

                # --------- SECTION : WORK --------- #
                work_dict = {}
                work_dict["resumeId"] = resumeId
                work_data = resume["work"]
                for work_data_item in work_data:
                    for item_value in work_data_item:
                        work_dict[item_value] = work_data_item[item_value]

                    work_query = insert(work).values(**work_dict)
                    session.execute(work_query)

                try:
                    # ---------- SECTION : VOLUNTEER --------- #
                    volunteer_data = resume["volunteer"]
                    volunteer_dict = {}
                    volunteer_dict["resumeId"] = resumeId
                    for volunteer_items in volunteer_data:
                        for item_value in volunteer_items:
                            volunteer_dict[item_value] = volunteer_items[item_value]

                        volunteer_query = insert(
                            volunteer).values(**volunteer_dict)
                        session.execute(volunteer_query)

                except:
                    print("No volunteer datas. ")

                # ---------- SECTION : EDUCATION ---------- #
                education_data = resume["education"]
                education_dict = {}
                education_courses_dict = {}
                education_dict["resumeId"] = resumeId
                for education_items in education_data:
                    for item_value in education_items:
                        if item_value != "educatedCourses":
                            education_dict[item_value] = education_items[item_value]
                        elif item_value == "educatedCourses":
                            education_courses_data = education_items[item_value]
                    
                    education_query = insert(education).values(**education_dict)
                    session.execute(education_query)

                    education_max_id = session.execute(f"select max(educationId) from education").fetchall()

                    for n in education_max_id:
                        education_id = n[0]
                    for m in education_courses_data: 
                        education_courses_dict["educatedCourses"] = m
                        education_courses_dict["educationId"] = education_id
                        education_courses_query = insert(education_courses).values(**education_courses_dict)
                        session.execute(education_courses_query)
                    


                # --------- SECTION : AWARDS ---------- #
                try:
                    awards_data = resume["awards"]
                    awards_dict = {}
                    awards_dict["resumeId"] = resumeId
                    for awards_items in awards_data:
                        for item_value in awards_items:
                            awards_dict[item_value] = awards_items[item_value]
                        awards_query = insert(awards).values(**awards_dict)
                        session.execute(awards_query)

                except:
                    print("No awards datas. ")

                # --------- SECTION : CERTIFICATES --------- #
                try:
                    certificates_data = resume["certificates"]
                    certificates_dict = {}
                    certificates_dict["resumeId"] = resumeId
                    for certificates_items in certificates_data:
                        for item_value in certificates_items:
                            certificates_dict[item_value] = certificates_items[item_value]
                        certificates_query = insert(
                            certificates).values(**certificates_dict)
                        session.execute(certificates_query)
                except:
                    print("No certificates datas.")

                # --------- SECTION : PUBLICATIONS --------- #
                try:
                    publications_data = resume["publications"]
                    publications_dict = {}
                    publications_dict["resumeId"] = resumeId
                    for publications_items in publications_data:
                        for item_value in publications_items:
                            publications_dict[item_value] = publications_items[item_value]
                        publications_query = insert(
                            publications).values(**publications_dict)
                        session.execute(publications_query)
                except:
                    print("Publications Data Missing")

                # --------- SECTION : SKILLS ------------ #
                skills_data = resume["skills"]
                skills_dict = {}
                skills_dict["resumeId"] = resumeId
                for skills_item in skills_data:
                    for item_value in skills_item:
                        skills_dict[item_value] = skills_item[item_value]

                    skills_query = insert(skills).values(**skills_dict)
                    session.execute(skills_query)

                # --------- SECTION : LANGUAGES --------- #
                languages_data = resume["languages"]
                languages_dict = {}
                languages_dict["resumeId"] = resumeId
                for languages_items in languages_data:
                    for item_value in languages_items:
                        languages_dict[item_value] = languages_items[item_value]

                    languages_query = insert(
                        languages).values(**languages_dict)
                    session.execute(languages_query)

                # --------- SECTION : INTERESTS --------- #
                interests_data = resume["interests"]
                interests_dict = {}
                interests_dict["resumeId"] = resumeId
                for interests_items in interests_data:
                    for item_value in interests_items:
                        interests_dict[item_value] = interests_items[item_value]

                    interests_query = insert(
                        interests).values(**interests_dict)
                    session.execute(interests_query)

                # --------- SECTION : REFERENCES --------- #
                try:
                    references_data = resume["references"]
                    references_dict = {}
                    references_dict["resumeId"] = resumeId
                    for references_items in references_data:
                        for item_value in references_items:
                            references_dict[item_value] = references_items[item_value]
                        
                        references_query = insert(
                            references).values(**references_dict)
                        session.execute(references_query)
                except:
                    print("No Referenecs included")

                # --------- SECTION : PROJECTS --------- #
                projects_data = resume["projects"]
                projects_dict = {}
                projects_dict["resumeId"] = resumeId
                for projects_items in projects_data:
                    for item_value in projects_items:
                        projects_dict[item_value] = projects_items[item_value]

                    projects_query = insert(projects).values(**projects_dict)
                    session.execute(projects_query)

            except:
                print("error")
                transaction.rollback()
                raise Exception("Data Insertion Error")
            else:
                transaction.commit()
            finally:
                transaction.close()

    return resumeId


async def resume_validate_and_insert(request): # -- function for validation verification and calling insertion
    # -----  VALIDATION  ----- #
    resume = await request.json()
    validator = Draft7Validator(schema)
    error_list = list(validator.iter_errors(resume))
    if len(error_list) == 0:
        print("no validation issue")
        resumeId = await resume_insertion(resume)
    else:
        raise Exception(error_list)

    return JSONResponse(resumeId)


middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'])
]

routes=[ # -- list of all routes
    Route('/resume', list_all_resume, methods=['GET']),
    Route('/resume', resume_validate_and_insert, methods=['POST']),
    Route('/resume/{pid:int}', requested_resume, methods=['GET']),
    Route('/resume/{pid:int}', resume_edit_and_update, methods=['PUT']),
    Route('/resume/{pid:int}', resume_deletion, methods=['DELETE'])
]

app = Starlette(debug=False, routes=routes, middleware=middleware )
