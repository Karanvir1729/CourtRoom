import cohere

def get_personality_prompt_dict(key_words):
	personality_prompts = {} # key -> (text description, [urls])

	co = cohere.Client('cOL5L8qHbfPK78SVMkOiKkU8tkZntE6UJL1d7jnk')  # This is your trial API key
	for key in key_words:
		message = f"Given a topic write a description of the person who only cares about this topic and nothing else. Topic: {key}"
		response = co.chat(
			message,
			model="command-light",  # using light version since the normal one is taking 4 times longer
			temperature=0.7,
			citation_quality='accurate',
			connectors=[{"id": "web-search"}]
		)
		ai_response = response.text
		urls = [i['url'] for i in response.documents]
		personality_prompts[key] = (ai_response, urls)

	return personality_prompts

key_words = ["novelty", "nature", "climate change"]  # Get from front end
print(get_personality_prompt_dict(key_words))
