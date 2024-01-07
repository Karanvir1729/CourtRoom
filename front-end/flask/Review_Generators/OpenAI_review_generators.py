#pip install openai
from openai import OpenAI



def get_personality_prompt_dict(key_words):
    personality_prompts = {}
    client = OpenAI(api_key="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")

    for key in key_words:
        p = f"Given a topic write a description of the person who only cares about this topic and nothing else. Topic: {key}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={"type": "text"},
            messages=[
                {"role": "system",
                 "content": "You are a role-play ai assistant, you pretend that you are a character and write reviews about topics like that character "},
                {"role": "user", "content": p}
            ]
        )
        ai_response = response.choices[0].message.content
        personality_prompts[key] = ai_response
        #print(key, ai_response)
    return personality_prompts

def get_OpenAI_review_dict(key_words, solution, problem):
    reviews = {}
    client = OpenAI(api_key="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")
    personalities = get_personality_prompt_dict(key_words)

    for key, value in personalities.items():

        p = f"Suppose that you are a person with this description {value}, now write a review from your perspective about: {solution}, given the problem {problem}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={"type": "text"},
            messages=[
                {"role": "system",
                 "content": "You are a role-play ai assistant, you pretend that you are a character and write reviews about topics like that character "},
                {"role": "user", "content": p}
            ]
        )
        ai_response = response.choices[0].message.content
        reviews[key] = ai_response
        #print(key, ai_response)
    return reviews

key_words = ["novelty", "nature", "climate change", "convinence"]  # Get from front end

solution= "Ban all plastic products. "
problem = "global warming"
out = get_OpenAI_review_dict( key_words, solution, problem)
print(out["convinence"])
