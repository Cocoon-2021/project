from resume_tables import *
from sqlalchemy.sql import select
from starlette.responses import JSONResponse


async def list_all_resume():

    basics_query = select(basics_information)
    basics_information_results = connect_engine.execute(basics_query).all()
    basics_profiles_query = select(basics_profiles)
    basics_profiles_results = engine.execute(basics_profiles_query).all()
    work_query = select(work)
    work_results = engine.execute(work_query).all()
    volunteer_query = select(volunteer)
    volunteer_results = engine.execute(volunteer_query).all()
    education_query = select(education)
    education_results = engine.execute(education_query).all()
    education_courses_query = select(education_courses)
    education_courses_results = engine.execute(education_courses_query).all()
    awards_query = select(awards)
    awards_results = engine.execute(awards_query).all()
    publications_query = select(publications)
    publications_results = engine.execute(publications_query).all()
    certificates_query = select(certificates)
    certificates_results = engine.execute(certificates_query).all()
    skills_query = select(skills)
    skills_results = engine.execute(skills_query).all()
    languages_query = select(languages)
    languages_results = engine.execute(languages_query).all()
    interests_query = select(interests)
    interests_results = engine.execute(interests_query).all()
    references_query = select(references)
    references_results = engine.execute(references_query).all()
    projects_query = select(projects)
    projects_results = engine.execute(projects_query).all()

    resume = [
        {
            "id": i.id,
            "coverLetter": i.coverLetter,
            "basics": {
                "name": i.name,
                "label": i.label,
                "image": i.image,
                "email": i.email,
                "phone": i.phone,
                "url": i.url,
                "summary": i.summary,
                "location": {
                    "address": i.address,
                    "postalCode": i.postalCode,
                    "city": i.city,
                    "countryCode": i.countryCode,
                    "region": i.region
                },
                "profiles": [
                    {
                        "network": p.network,
                        "username": p.username,
                        "url": p.url
                    }
                    for p in basics_profiles_results
                    if p.resumeId == i.id
                ]
            },
            "work": [
                {
                    "name": w.name,
                    "location": w.location,
                    "description": w.description,
                    "position": w.position,
                    "url": w.url,
                    "startDate": w.startDate,
                    "endDate": w.endDate,
                    "summary": w.summary,
                    "highlights": w.highlights,
                    "keywords":  w.keywords
                }
                for w in work_results
                if w.resumeId == i.id
            ],
            "volunteer": [
                {
                    "organization": v.organization,
                    "position": v.position,
                    "url": v.url,
                    "startDate": v.startDate,
                    "endDate": v.endDate,
                    "summary": v.summary,
                    "highlights": v.highlights
                }
                for v in volunteer_results
                if v.resumeId == i.id
            ],
            "education": [
                {
                    "institution": e.institution,
                    "url": e.url,
                    "area": e.area,
                    "studyType": e.studyType,
                    "startDate": e.startDate,
                    "endDate": e.endDate,
                    "score": e.score,
                    "courses": [
                        ec.value
                        for ec in education_courses_results
                        if ec.educationId == e.educationId
                    ]
                }
                for e in education_results
                if e.resumeId == i.id
            ],
            "awards": [
                {
                    "title": a.title,
                    "date": a.date,
                    "awarder": a.awarder,
                    "summary": a.summary
                }
                for a in awards_results
                if a.resumeId == i.id
            ],
            "certificates": [
                {
                    "name": c.name,
                    "date": c.date,
                    "url": c.url,
                    "issuer": c.issuer
                }
                for c in certificates_results
                if c.resumeId == i.id
            ],
            "publications": [
                {
                    "name": p.name,
                    "publisher": p.publisher,
                    "releaseDate": p.releaseDate,
                    "url": p.url,
                    "summary": p.summary
                }
                for p in publications_results
                if p.resumeId == i.id
            ],
            "skills": [
                {
                    "name": s.name,
                    "level": s.level,
                    "keywords": s.keywords
                }
                for s in skills_results
                if s.resumeId == i.id
            ],
            "languages": [
                {
                    "language": l.language,
                    "fluency": l.fluency
                }
                for l in languages_results
                if l.resumeId == i.id
            ],
            "interests": [
                {
                    "name": intere.name,
                    "keywords": intere.keywords
                }
                for intere in interests_results
                if intere.resumeId == i.id
            ],
            "references": [
                {
                    "name": r.name,
                    "reference": r.reference
                }
                for r in references_results
                if r.resumeId == i.id
            ],
            "projects": [
                {
                    "name": pr.name,
                    "description": pr.description,
                    "highlights": pr.highlights,
                    "keywords": pr.keywords,
                    "startDate": pr.startDate,
                    "endDate": pr.endDate,
                    "url": pr.url,
                    "roles": pr.roles,
                    "entity": pr.entity,
                    "type": pr.type

                }
                for pr in projects_results
                if pr.resumeId == i.id
            ]
        }
        for i in basics_information_results
    ]

    return resume
