import requests

def fetch_real_jobs(query):
    url = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "X-RapidAPI-Key": "",  # Replace with your key
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    params = {
        "query": query,
        "page": 1,
        "num_pages": 1
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        jobs = response.json().get("data", [])
        results = []
        for job in jobs[:5]:  # Limit to top 5
            results.append({
                "title": job.get("job_title"),
                "company": job.get("employer_name"),
                "location": job.get("job_city"),
                "link": job.get("job_apply_link")
            })
        return results
    except Exception as e:
        print("Job fetch error:", e)
        return []
