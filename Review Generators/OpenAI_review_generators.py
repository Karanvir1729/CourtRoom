#pip install openai
import openai
import  review_personality_generator

def get_OpenAI_review_dict(key_words, solution):
    reviews = {}
    openai.api_key = "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"
    personalities = review_personality_generator.get_personality_prompt_dict(key_words)

    for key, value in personalities.items():

        p = f"Suppose that you are a person with this description {value}, now write a review from your perspective about: {solution}"
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
        reviews[key] = ai_response
        #print(key, ai_response)
    return reviews

key_words = ["novelty", "nature", "climate change", "convinence"]  # Get from front end

solution= "Ban all plastic products. "
out = get_OpenAI_review_dict( key_words, solution)
print(out["convinence"])