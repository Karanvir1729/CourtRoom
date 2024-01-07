# Takes input from the front end about the creteria
# Goal is to make chat gpt create personalities that are highly biased towards the key words.
# pip install openai
from openai import OpenAI
import re



#
def get_auto_key_words(problem, solution):
    client = OpenAI(api_key="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")
    keywords = []

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "text"},
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output a list of extract the main single topics (not verbs for example) words seperated by space "},
            {"role": "user", "content": f"Extract the list from  this text: {problem}.{solution}."}
        ]
    )

    ai_response = response.choices[0].message.content
    ai_response = re.sub(r'\n', '', ai_response)

    keywords += ai_response.split(" ")

    return keywords

problem = "pollution is rising"
solution = "ban fire crakers"
print(get_auto_key_words(problem, solution))