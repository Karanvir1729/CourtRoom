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


def get_cohere_review_dict( key_words,problem, solution):
    reviews = {}
    co = cohere.Client('cOL5L8qHbfPK78SVMkOiKkU8tkZntE6UJL1d7jnk')  # This is your trial API key
    personalities = get_personality_prompt_dict(key_words)
    for key, value in personalities.items():
        message = f"Suppose that you are a person with this description {value[0]}, now write a review from your perspective about: {solution}, given the problem {problem}"
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
