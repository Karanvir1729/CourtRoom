Elevator pitch: You dont ask AI to tell you which shirt to buy do you? You look at the reviews because people know the best. What if we make AI roleplay and write those reviews. 
This would not only provide a wider perspective but also add a human touch. 

Set Up instructions
1. Clone the repo
2. Get Cohere, Open AI , and Replicate API keys. Replace the current ones as they do not work for obious reasons. Look at Review_Generators folder and change the api keys in the review generation files.
3. Pip install the dependencies in a venv. flask, openai, cohere, replicate, and requirements.txt
4. Run the run.py located in frontend
5. provide an input csv like given in the hackathon dataset (id, problem, solution)
6. Tell the machine what ID you want to look at
7. Give key words. Think of these as the experts. There will be 1 key word that would be auto generated (so the ai gets to create 1 expert)
8. Select 1 AI model. Cohere would also give you sources which is cool. 
9. Click analyze (would take a few sec (depending on how many keywords you gave))
10. Look at the very last line, this is the sentiment analysis of the review. Closer to 1 means it is a positive review, closer to -1 means that it is a negative review.
11. Launch the server again to re-run


COHERE API

Coher Classifier
This document provides a detailed overview of the  AI model  that involves the use of Cohere Classifier. The specific model used is ‘embed-english-v3.0.’ The model focuses on analysing  Amazon product reviews and classifying our personalised reviews  into positive and negative categories, assigning confidence scores, and calculating an overall average score.

Cohere Classifier is an artificial intelligence tool designed for text classification tasks. It is developed by Cohere, a company specializing in natural language processing (NLP) solutions. The classifier is trained on diverse datasets to accurately predict labels for input text, making it suitable for a wide range of applications, including sentiment analysis.Cohere’s AI-driven sentiment analysis platform allows businesses to gain valuable insights from customer feedback, improve their products, and make informed decisions. Using natural language processing (NLP), Cohere processes large volumes of data in real-time, enabling product, marketing, and capital market businesses to unlock previously untapped data sources and drive growth.

Cohere provides multiple pre-trained models for classification, each designed for specific use cases and varying in accuracy and computational cost. Some popular models include embed-english-v2.0, embed-multilingual-v2.0, embed-english-v3.0 and light versions of each. For this model, we used embed-english-v3.0.

The dataset used for training and testing the Cohere Classifier was obtained from Kaggle. It comprises 1000 Amazon product reviews, with corresponding labels indicating whether the review is positive or negative.The dataset ‘modifiedtxt1.txt’ is the modified version of the dataset which was made more aligned with our requirements and the model.
/CourtRoom/Cohere_Review_Classification/modifiedtxt1.txt

The Cohere Classifier is applied to the reviews which are generated from the solution of the problem. Each review is rated as ‘Positive’ or ‘Negative’ along with a confidence metric for each. The sum of the confidence of positive and negative is 1. 
The difference of the confidences is calculated to get the ‘Score’ of the review. To obtain the final score, the average of all the scores is calculated. 
The results are stored in csv along with the Problem, the Solution, the Score, reviews and the relevant result for the full transparency.




Cohere Websocket - Personalities Generator and Review Generator
This documentation outlines the use of Cohere Coral, a component of the project, designed to generate diverse personalities for reviewing solutions. Specifically, the project employs the ‘Command-light’ model to assess solutions from various perspectives, aiming to eliminate bias in the final reviews.

Cohere Coral is an artificial intelligence tool developed by Cohere for generating diverse and contextually relevant text. It specializes in creating human-like language and is used for tasks such as content creation, conversation generation, and diverse opinion synthesis.Coral is a conversational AI toolkit for enterprises to build RAG-enabled knowledge assistants for their employees and customers

Cohere chat models come pre-trained on vast datasets, enabling them to understand the nuances of language and generate coherent and contextually appropriate responses. This pre-training enhances the efficiency and effectiveness of the personality generation process. 

Cohere Coral offers a range of pre-trained models, each tailored for specific use cases. Some notable models include Command, Command-light and Command-nightly.
The ‘Command-light’ model was selected for this project due to its ability to generate text as good as the command model model, but superfast. Command is Cohere’s text generation LLM which powers conversational agents, summarization, copywriting, and similar use cases. 

Cohere Coral is employed to generate diverse personalities to assess solutions from different viewpoints. The goal is to reduce bias in the final reviews by incorporating a variety of opinions. This process involves creating multiple iterations of solution reviews, each expressing a unique perspective. For this we 3 personalities were crucial, a person who only thinks about ‘climate change’, a person who only thinks about ‘novelty’, a person who only thinks about ‘convenience’ and a person who only thinks of ‘nature’. Point of views from all these personalities are collected.
To ensure the generated reviews are up-to-date and relevant, a web-connect feature is implemented. This allows Cohere Coral to gather real-time information and adapt the generated content based on the latest data and opinions available on the web.After experimentation with various combinations, the temperature for review generation is set to 0.7, striking a balance between diversity and coherence. The citation quality is configured as ‘accurate’ to ensure that the generated content is reliable and factually sound. Moreover, the links to the source of information is also provided along with the review.

The generated reviews are then fed into the Cohere Classifier, which evaluates the reviews for sentiment (positive/negative) and assigns confidence scores. The goal is to leverage diverse perspectives in the final assessment.

The review generator too utilizes the Cohere Coral's Command-light model with consistent tweaks and settings, including a temperature of 0.7 and ‘accurate’ citation quality. This configuration ensures the generation of diverse and contextually relevant reviews, contributing to a comprehensive assessment of solutions with varied perspectives while maintaining coherence and reliability.




-cohere websocket(personalities, review generation)

-gpt-3.5 turbo(personalities, review generation)
-replicate

SUBMISSION DATA BELOW

Team info-
Saurodeep Majumdar - sdmajumd@uwaterloo.ca
Ayush Khanna - ayushkhanna29@gmail.com
Karanvir Khanna karanvir.khanna@mail.utoronto.ca, 
Rakan- rakan.alalami@mail.mcgill.ca


Project submission-
https://github.com/Karanvir1729/CourtRoom ( Note api keys are dummy in the repo)
The algorithmic tool we've developed, works as the Idea Inspector. It aligns with the concept of an 'Idea Validator' and also incorporates the 'Idea Filter.' This multifaceted tool generates comprehensive reviews for proposed solutions, examining them from diverse perspectives. It then assesses the reviews to validate the viability of the solution. In addition, the Idea Filter component selectively screens out data that isn't relevant to sustainability, vague, or gibberish. By combining these functions, the tool not only evaluates the merit of solutions but also ensures that the generated reviews focus on sustainability-related aspects, providing a refined and thorough analysis for decision-making.
Video/presention

Project Explanation


Revolutionizing solution evaluation through an innovative virtual court case approach, where our AI generates diverse reviews, and the 'Judge' component assigns scores, ensuring a comprehensive and objective assessment with a focus on sustainability.
Our idea inspector  is an advanced algorithmic tool designed for comprehensive solution evaluation. Utilizing a unique virtual court case framework, the AI model functions as a diverse jury, generating detailed reviews from multiple perspectives for a given problem-solution pair. The subsequent evaluation is conducted by the 'Judge,' an integral component that meticulously assesses each review, ultimately determining the optimal decision and assigning a comprehensive score. This innovative approach ensures a thorough and objective analysis, offering a nuanced understanding of the solution's viability. Additionally, the tool incorporates an 'Idea Filter' to weed out irrelevant or vague data, streamlining the evaluation process and emphasizing sustainability-related aspects. 
Our idea inspector significantly augments human evaluation of innovative ideas by enhancing efficiency, reducing bias, and providing a comprehensive evaluation through the incorporation of various perspectives. 
Through its diverse and virtual jury approach, the tool ensures a reduction in evaluative bias, offering a more impartial assessment. Moreover, the capability to process large volumes of data allows for a quicker and more thorough analysis of numerous ideas. The algorithm's training on a real reviews dataset ensures that it understands and reflects genuine human sentiments, while real-time access to the web ensures the information used is up-to-date, providing human evaluators with a reliable and current dataset for decision-making.
The most innovative aspect of our project, lies in its unique virtual court case framework, replicating a deliberative process for solution evaluation. By deploying an AI model as a diverse jury, generating reviews from various perspectives and personalities, and incorporating a meticulous 'Judge' component for final assessment, we introduce a dynamic and sophisticated approach to solution evaluation. This not only enhances efficiency and reduces bias but also provides human evaluators with a comprehensive and nuanced understanding of proposed ideas.


Technical Implementation: 
We used models from OpenAI, Replicate and Cohere to generate evaluations for sustainability and circular economy business ideas. For OpenAI we utilized the GPT3.5-turbo model, Replicate we used the Llama2 model and Cohere we used the command-lite model. The essential idea of our tool is to provide a jury which gives detailed reviews based on multiple personalities then finally decides on a majority vote among . We include an innovative use of GenAI where we first create personalities for the AI agent by supplying a prompt like Given a topic write a two sentence second person point of view description of the person who only cares about this topic and nothing else. Just provide the description of the person, starting with you are. Topic: {key}". The output of this provides a system prompt to be inputted into the AI that will provide a review on the problem solution pair supplied. This enables the model to come up with an output based on its personality. Then the classification was done using the Cohere model. Then an output classification of good/bad is provided and then an average is taken. We used flask for frontend and have a visually appealing UI. We include a functionality to auto search for keywords from the GPT3.5 turbo model to output extra keywords to be personalities based on user input keywords that are provided. This is using a model Also various functionality like radio buttons to select different models or a combination of models from OpenAI GPT3.5, Replicate llama2 and Cohere command-lite are also provided.We also output the reviews and good or bad classifications that are given by the models into a CSV

Since its a flask application just execute run.py using python3 run.py . Also will need to install dependencies of flask, replicate and openai, cohere



Future prospects:
We had an ‘Idea Filter’ implemented in python using the llama2 model. We plan to incorporate this into our final application in the future. This will weed out irrelevant or vague data, streamlining the evaluation process and emphasizing sustainability-related aspects. If it's not even an idea then we should return a response to the user that says. We also plan to deploy application.


Consent and Submission:
All team members consent to the data agreement

