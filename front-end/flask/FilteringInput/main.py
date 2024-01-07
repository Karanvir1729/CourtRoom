# Filtering inputs from the user based on various layers
# 1) find any grammatical errors if there are any 
# 2) Start by if it is an idea  - Default output (as this is not a valid idea an evaluation cannot be provided, would you still like to continue?)
# 3) Is it a business idea - Default output (as this is not a business idea we cannot provide an evaluation, would you still like to continue?)
# 4) Is it related to circular economy and sustainability - Default Output (The idea does not relate to circular economy and sustainability would you still like to continue? )
# 5) Does the idea have implementation in it?

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
    "max_new_tokens": 500,  
    "min_new_tokens": -1,
    "repetition_penalty": 1.2
  }
)
  return output


if __name__ == "__main__":

    user_entry = "Problem: The construction industry is indubitably one of the significant contributors to global waste, contributing approximately 1.3 billion tons of waste annually, exerting significant pressure on our landfills and natural resources. Traditional construction methods entail single-use designs that require frequent demolitions, leading to resource depletion and wastage. Solution: Herein, we propose an innovative approach to mitigate this problem: Modular Construction. This method embraces recycling and reuse, taking a significant stride towards a circular economy.   Modular construction involves utilizing engineered components in a manufacturing facility that are later assembled on-site. These components are designed for easy disassembling, enabling them to be reused in diverse projects, thus significantly reducing waste and conserving resources.  Not only does this method decrease construction waste by up to 90%, but it also decreases construction time by 30-50%, optimizing both environmental and financial efficiency. This reduction in time corresponds to substantial financial savings for businesses. Moreover, the modular approach allows greater flexibility, adapting to changing needs over time.  We believe, by adopting modular construction, the industry can transit from a 'take, make and dispose' model to a more sustainable 'reduce, reuse, and recycle' model, driving the industry towards a more circular and sustainable future. The feasibility of this concept is already being proven in markets around the globe, indicating its potential for scalability and real-world application."
  
    system_prompt = ""
    prompt = f"Are there any gramatical errors in: {user_entry}. If there are not any errors provide a one word answer of none"

    output = ""
    for elem in run_replicate(system_prompt, prompt):
            output += elem
    
    print(output)

    if "none" not in output.lower():
        print("please fix the grammatical errors")
        user_input = input("Would you like to continue without fixing? Yes or no")
        if user_input.lower() == "no":
            exit(0)


    system_prompt = "You are an idea evaluator"
    prompt = f"Provide a yes or no answer. Is this an idea: {user_entry} "

    output = ""
    for elem in run_replicate(system_prompt, prompt):
            output += elem

    if 'no' in output.lower():
        print("As this is not a valid idea an evaluation cannot be provided, would you still like to continue?")
        user_input = input("Continue? Yes or No: ")
        if user_input.lower() == "no":
            print("Default Rating Provided")


    # prompt = f"Provide a yes or no answer. Is this a business idea: {user_entry}"
    
    # output = ""
    # for elem in run_replicate(system_prompt, prompt):
    #         output += elem

    # if 'no' in output.lower():
    #     print("As this is not a business idea we cannot provide an evaluation, would you still like to continue?")
    #     user_input = input("Continue? Yes or No: ")

    #     if user_input.lower() == "no":
    #         print("Default Rating Provided")

    # prompt = f"Provide a yes or no answer. Is this idea related to circular economy and sustainability {user_entry}"

    # output = ""
    # for elem in run_replicate(system_prompt, prompt):
    #     output += elem
    
    # print(output)
    
    # if 'no' in output.lower():
    #     print("The idea does not relate to circular economy and sustainability would you still like to continue?")
    #     user_input = input("Continue? Yes or No: ")
    
    # prompt = f"Provide a yes or no answer. Does it talk about an implementation of the proposed solution: {user_entry}"

    # output = ""
    # for elem in run_replicate(system_prompt, prompt):
    #     output += elem
    
    # if 'no' in output.lower():
    #     print("You do not talk about how to implement your idea, a constructive feedback may not be provided, do you still want to continue?")
    #     user_input = input("Continue? Yes or No: ")
    
    # print("Screening and Filtering done now run through models")

