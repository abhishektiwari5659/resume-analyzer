def match_jobs(user_skills, job_db):
    matches = []
    for job in job_db:
        overlap = set(user_skills).intersection(set(job['skills']))
        if len(overlap) >= 3:
            matches.append(job['title'])
    return matches
