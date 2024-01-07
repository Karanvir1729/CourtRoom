import cohere
from cohere.responses.classify import Example
co = cohere.Client('cOL5L8qHbfPK78SVMkOiKkU8tkZntE6UJL1d7jnk') # This is your trial API key

txt_file = '/content/modifiedtxt.txt'
examples = []
with open(txt_file, 'r') as file:
  for line in file:
        parts = line.strip().split(',')
        if len(parts) == 2:
            examples.append(Example(parts[0], parts[1]))
inputs=["this item sucks"]
response = co.classify(
  model='embed-english-v2.0',
  inputs=inputs,
  examples=examples)
print('The confidence levels of the labels are: {}'.format(response.classifications))