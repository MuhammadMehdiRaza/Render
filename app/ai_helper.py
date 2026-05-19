from groq import Groq
from django.conf import settings

def generate(text):
    try:
        client=Groq(api_key=settings.GROQ_API_KEY)
 
        response=client.chat.completions.create(
            model=settings.GROQ_MODEL,
            messages=[
                {
                    "role":"user",
                    "content":"Summarize this post\n\n"
                    f"Post Content:\n {text}"
                }
            ],
            max_tokens=200,
            temperature=0.4
        )
        summary=response.choices[0].message.content
        return summary
    except Exception as e:
        return f"Can't summarize {str(e)}"

    