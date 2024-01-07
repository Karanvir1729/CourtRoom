import cohere 
co = cohere.Client('cOL5L8qHbfPK78SVMkOiKkU8tkZntE6UJL1d7jnk') # This is your trial API key
message="Can you give me a global market overview of the solar panels?"

response = co.chat(
	message, 
	model="command-light", #using light version since the normal one is taking 4 times longer
	temperature=0.7,
  citation_quality='accurate',
  connectors=[{"id":"web-search"}]
)

answer = response.text
print(answer)