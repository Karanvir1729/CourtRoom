# Takes input from the front end about the creteria
# Goal is to make chat gpt create personalities that are highly biased towards the key words.
# pip install openai
import openai
import re


def get_auto_key_words(problem, solution):
    keywords = []
    openai.api_key = "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"
    p = f" extract the main single topics (not verbs for example) words seperated by space from  this text: {problem}.{solution}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=p,
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=1,
        presence_penalty=1
    )
    ai_response = response["choices"][0]["text"]
    ai_response = re.sub(r'\n', '', ai_response)

    keywords += ai_response.split(" ")

    return keywords

problem = "pollution is rising"
solution = "ban fire crakers"
print(get_auto_key_words(problem, solution))