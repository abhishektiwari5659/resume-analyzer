import spacy
import cohere

co = cohere.Client("hJi3f9aG2VNxWS9dZCwmqrsv62dswdSk5Va5hwX1") 
nlp = spacy.load("en_core_web_sm")

# Sample keyword list
keywords = ["python", "java", "mongodb", "html", "css", "flask", "javascript"]

def analyze_resume(text):
    found = [kw for kw in keywords if kw.lower() in text.lower()]
    missing = list(set(keywords) - set(found))
    return found, missing

def get_ai_feedback(text):
    prompt = f"""
You're an expert technical resume reviewer. Analyze the resume content below and provide structured, actionable feedback in these categories:
1. Missing Technical Keywords or Frameworks
2. Suggestions for Better Project Descriptions
3. General Resume Improvements

Resume:
{text}

Respond only in 3 bullet-point sections with specific advice.
    """

    try:
        response = co.generate(
            model='command',
            prompt=prompt,
            max_tokens=200,
            temperature=0.5
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return "Feedback temporarily unavailable."