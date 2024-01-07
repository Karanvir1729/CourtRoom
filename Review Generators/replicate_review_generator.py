import replicate

def run_replicate(system_prompt, prompt):
  replicate.Client(api_token='r8_LKN7bmUUerXR2u5TC2PD84J2h5xPRZA4g5bYl')
  output = replicate.run(
  "meta/llama-2-70b-chat:2d19859030ff705a87c746f7e96eea03aefb71f166725aee39692f1476566d48", stream=False, input={
    "debug": False,
    "top_k": 50,
    "top_p": 1,
    "prompt": prompt,
    "temperature": 0.75,
    "system_prompt": system_prompt,
    "max_new_tokens": 150,  
    "min_new_tokens": -1,
    "repetition_penalty": 1.2
  }
)
  return output

def generate_personalities(key_words):
  system_prompts = {} 

  for key in key_words:
    system_prompt = ""
    output = ""
    prompt = f"Given a topic write a two sentence second person point of view description of the person who only cares about this topic and nothing else. Just provide the description of the person, starting with you are. Topic: {key}"
    for elem in run_replicate(system_prompt, prompt):
        output += elem

    system_prompts[key] = output

  print(system_prompts)

  return system_prompts



def generate_review(personalities, user_input):
  # put system prompt as input to the model
  reviews = {}
  for k,v in personalities.items():
    output = ""
    for elem in run_replicate(v, user_input):
        output += elem
    print(output)
    reviews[k] = output

  return reviews
   

def generate_replicate_review(key_words, problem, solution):
  prompt = "Provide a short two sentence review of what you think about this problem solution pair. Start your answer with 'The proposed solution'."
  user_input = prompt + problem + solution
  personalities = generate_personalities(key_words)
  reviews = generate_review(personalities, user_input)

  return reviews
   

if __name__ == "__main__":
  key_words = ["novelty", "nature", "profitability"]
  prompt = "Provide a short two sentence review of what you think about this problem solution pair. Start your answer with 'The proposed solution'."
  problem = "Problem: \"The construction industry is indubitably one of the significant contributors to global waste, \
  contributing approximately 1.3 billion tons of waste annually, exerting significant pressure on our landfills and natural resources. \
  Traditional construction methods entail single-use designs that require frequent demolitions, leading to resource depletion and wastage."
  
  solution = "Solution: \ Herein, we propose an innovative approach to mitigate this problem: Modular Construction. This method embraces recycling and reuse, taking a significant stride \
  towards a circular economy.   Modular construction involves utilizing engineered components in a manufacturing facility that are later assembled on-site. These components are designed for easy disassembling,\
  enabling them to be reused in diverse projects, thus significantly reducing waste and conserving resources.  Not only does this method decrease construction waste by up to 90%, \
  but it also decreases construction time by 30-50%, optimizing both environmental and financial efficiency. This reduction in time corresponds to substantial financial savings for businesses.\
  Moreover, the modular approach allows greater flexibility, adapting to changing needs over time.  We believe, by adopting modular construction, the industry can transit from a 'take, make and dispose' model to a \
  more sustainable 'reduce, reuse, and recycle' model, driving the industry towards a more circular and sustainable future. The feasibility of this concept is already being proven in markets around the globe, indicating its potential for \
  scalability and real-world application."

  prompt1 = "Provide a short two sentence review of what you think about this problem solution pair. Start your answer with 'The proposed solution'.Problem: Plastics in the ocean, Solution: Biodegradable plastics "

  generate_replicate_review(key_words, problem, solution)

