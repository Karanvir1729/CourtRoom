import cohere
import  cohere_web_connect_personality
def get_cohere_review_dict( key_words, solution):
    reviews = {}
    co = cohere.Client('cOL5L8qHbfPK78SVMkOiKkU8tkZntE6UJL1d7jnk')  # This is your trial API key
    personalities = cohere_web_connect_personality.get_personality_prompt_dict(key_words)
    for key, value in personalities.items():
        message = f"Suppose that you are a person with this description {value[0]}, now write a review from your perspective about: {solution}"
        response = co.chat(
            message,
            model="command-light",  # using light version since the normal one is taking 4 times longer
            temperature=0.7,
            citation_quality='accurate',
            connectors=[{"id": "web-search"}]
            )
        ai_response = response.text
        urls = [i['url'] for i in response.documents]
        reviews[key] = (ai_response, urls)
    return reviews
key_words = ["novelty", "nature", "climate change", "convinence"]  # Get from front end
solution= "Ban all plastic products. "
out = get_cohere_review_dict( key_words, solution)
print(out["convinence"])