
from resume_tables import *
from database_engine import connect_engine
from resume_deletion import resume_deletion
from resume_update import resume_edit_and_update
from resume_list import list_all_resume,requested_resume
from sqlalchemy import schema
from sqlalchemy.sql import insert
from starlette.applications import Starlette
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
                for i in basics_information_data:
                    basics_dict[i] = basics_information_data[i]
                basics_dict["resumeCoverLetter"] = resume["resumeCoverLetter"]
                basics_dict.pop("location")
                basics_dict.pop("profiles")

                basics_location_dict = {}
                basics_location_data = resume["basics"]["location"]
                for i in basics_location_data:
                    basics_location_dict[i] = basics_location_data[i]
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
                for i in basics_profiles_data:
                    for n in i:
                        basics_profiles_dict[n] = i[n]
                    basics_profiles_query = insert(
                        basics_profiles).values(**basics_profiles_dict)
                    session.execute(basics_profiles_query)

                # --------- SECTION : WORK --------- #
                work_dict = {}
                work_dict["resumeId"] = resumeId
                work_data = resume["work"]
                for i in work_data:
                    for n in i:
                        if n != "workHighlights":
                            if n != "workKeywords":
                                work_dict[n] = i[n]

                    for m in work_data:
                        for p in m:
                            if p == "workHighlights":
                                work_highlights = m[p]
                    work_highlights_data = work_highlights
                    # work_highlights_data = ",".join(work_highlights)
                    work_dict["workHighlights"] = work_highlights_data

                    for x in work_data:
                        for y in x:
                            if y == "workKeywords":
                                work_keywords = x[y]
                    work_keywords_data = work_keywords
                    # work_keywords_data = ",".join(work_keywords)
                    work_dict["workKeywords"] = work_keywords_data

                    work_query = insert(work).values(**work_dict)
                    session.execute(work_query)

                try:
                    # ---------- SECTION : VOLUNTEER --------- #
                    volunteer_data = resume["volunteer"]
                    volunteer_dict = {}
                    volunteer_dict["resumeId"] = resumeId
                    for i in volunteer_data:
                        for n in i:
                            if n != "volunteeringHighlights":
                                volunteer_dict[n] = i[n]

                        for m in volunteer_data:
                            for p in m:
                                if p == "volunteeringHighlights":
                                    volunteer_highlights = i[n]
                        volunteer_highlights_data = volunteer_highlights
                        # volunteer_highlights_data = ",".join(
                        #     volunteer_highlights)
                        volunteer_dict["volunteeringHighlights"] = volunteer_highlights_data

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
                for i in education_data:
                    for n in i:
                        if n != "educatedCourses":
                            education_dict[n] = i[n]
                        elif n == "educatedCourses":
                            education_courses_data = i[n]
                    print(education_dict)
                    print(education_courses_dict)
                    education_query = insert(education).values(**education_dict)
                    session.execute(education_query)

                    education_max_id = session.execute(f"select max(educationId) from education").fetchall()

                    for n in education_max_id:
                        education_id = n[0]
                        print(education_id)
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
                    for i in awards_data:
                        for n in i:
                            awards_dict[n] = i[n]
                        awards_query = insert(awards).values(**awards_dict)
                        session.execute(awards_query)

                except:
                    print("No awards datas. ")

                # --------- SECTION : CERTIFICATES --------- #
                try:
                    certificates_data = resume["certificates"]
                    certificates_dict = {}
                    certificates_dict["resumeId"] = resumeId
                    for i in certificates_data:
                        for n in i:
                            certificates_dict[n] = i[n]
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
                    for i in publications_data:
                        for n in i:
                            publications_dict[n] = i[n]
                        publications_query = insert(
                            publications).values(**publications_dict)
                        session.execute(publications_query)
                except:
                    print("Publications Data Missing")

                # --------- SECTION : SKILLS ------------ #
                skills_data = resume["skills"]
                skills_dict = {}
                skills_dict["resumeId"] = resumeId
                for i in skills_data:
                    for n in i:
                        if n != "skillKeywords":
                            skills_dict[n] = i[n]

                    for m in skills_data:
                        for p in m:
                            if p == "skillKeywords":
                                skills_keywords = m[p]
                    skills_keywords_data = skills_keywords
                    # skills_keywords_data = ",".join(skills_keywords)
                    skills_dict["skillKeywords"] = skills_keywords_data

                    skills_query = insert(skills).values(**skills_dict)
                    session.execute(skills_query)

                # --------- SECTION : LANGUAGES --------- #
                languages_data = resume["languages"]
                languages_dict = {}
                languages_dict["resumeId"] = resumeId
                for i in languages_data:
                    for n in i:
                        languages_dict[n] = i[n]
                    languages_query = insert(
                        languages).values(**languages_dict)
                    session.execute(languages_query)

                # --------- SECTION : INTERESTS --------- #
                interests_data = resume["interests"]
                interests_dict = {}
                interests_dict["resumeId"] = resumeId
                for i in interests_data:
                    for n in i:
                        if n != "interestKeywords":
                            interests_dict[n] = i[n]

                    for m in interests_data:
                        for p in m:
                            if p == "interestKeywords":
                                interests_keywords = m[p]
                    interests_keywords_data = interests_keywords
                    # interests_keywords_data = ",".join(interests_keywords)
                    interests_dict["interestKeywords"] = interests_keywords_data

                    interests_query = insert(
                        interests).values(**interests_dict)
                    session.execute(interests_query)

                # --------- SECTION : REFERENCES --------- #
                try:
                    references_data = resume["references"]
                    references_dict = {}
                    references_dict["resumeId"] = resumeId
                    for i in references_data:
                        for n in i:
                            references_dict[n] = i[n]
                        references_query = insert(
                            references).values(**references_dict)
                        session.execute(references_query)
                except:
                    print("No Referenecs included")

                # --------- SECTION : PROJECTS --------- #
                projects_data = resume["projects"]
                projects_dict = {}
                projects_dict["resumeId"] = resumeId
                for i in projects_data:
                    for n in i:
                        if n != "projectsKeywords":
                            if n != "projectHighlights":
                                if n != "projectRoles":
                                    projects_dict[n] = i[n]

                    for i in projects_data:
                        for n in i:
                            if n != "projectKeywords":
                                if n != "projectRoles":
                                    if n == "projectHighlights":
                                        projects_highlights = i[n]
                    projects_highlights_data = projects_highlights
                    # projects_highlights_data = ",".join(projects_highlights)
                    projects_dict["projectHighlights"] = projects_highlights_data

                    for i in projects_data:
                        for n in i:
                            if n != "projectRoles":
                                if n != "projectHighlights":
                                    if n == "projectKeywords":
                                        projects_keywords = i[n]
                    projects_keywords_data = projects_keywords
                    # projects_keywords_data = ",".join(projects_keywords)
                    projects_dict["projectKeywords"] = projects_keywords_data

                    for i in projects_data:
                        for n in i:
                            if n != "projectHighlights":
                                if n != "projectKeywords":
                                    if n == "projectRoles":
                                        projects_roles = i[n]
                    projects_roles_data = projects_roles
                    # projects_roles_data = ",".join(projects_roles)
                    projects_dict["projectRoles"] = projects_roles_data

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
    # validator = Draft7Validator(schema)
    # error_list = list(validator.iter_errors(resume))
    # if len(error_list) == 0:
    #     print("no validation issue")
        # resumeId = await resume_insertion(resume)
    resumeId = await resume_insertion(resume)


    return JSONResponse(resumeId)


app = Starlette(debug=True,  routes=[ # -- list of all routes
    Route('/resume', list_all_resume, methods=['GET']),
    Route('/', resume_validate_and_insert, methods=['POST']),
    Route('/resume/{pid:int}', requested_resume, methods=['GET']),
    Route('/resume/{pid:int}', resume_edit_and_update, methods=['PUT']),
    Route('/resume/{pid:int}', resume_deletion, methods=['DELETE'])
])
