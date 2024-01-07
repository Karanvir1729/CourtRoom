# Takes input from the front end about the creteria
# Goal is to make chat gpt create personalities that are highly biased towards the key words.
# pip install openai
import openai

def get_personality_prompt_dict(key_words):
    personality_prompts = {}
    openai.api_key = "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"

    for key in key_words:

        p = f"Given a topic write a description of the person who only cares about this topic and nothing else. Topic: {key}"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=p,
            temperature=0,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=1,
            presence_penalty=1
        )
        ai_response = response["choices"][0]["text"]
        personality_prompts[key] = ai_response
        #print(key, ai_response)
    return personality_prompts

key_words = ["novelty", "nature", "climate change"]  # Get from front end
print(get_personality_prompt_dict(key_words))