Elevator pitch: You dont ask AI to tell you which shirt to buy do you? You look at the reviews because people know the best. What if we make AI roleplay and write those reviews. 
This would not only provide a wider perspective but also add a human touch. 

Set Up instructions
1. Clone the repo
2. Get Cohere, Open AI , and Replicate API keys. Replace the current ones as they do not work for obious reasons.
3. Pip install the dependencies in a venv. flask, openai, cohere, replicate, and requirements.txt
4. Run the run.py located in frontend
5. provide an input csv like given in the hackathon dataset (id, problem, solution)
6. Tell the machine what ID you want to look at
7. Give key words. Think of these as the experts. There will be 1 key word that would be auto generated (so the ai gets to create 1 expert)
8. Select 1 AI model. Cohere would also give you sources which is cool. 
9. Click analyze (would take a few sec (depending on how many keywords you gave))
10. Look at the very last line, this is the sentiment analysis of the review. Closer to 1 means it is a positive review, closer to -1 means that it is a negative review.
11. Launch the server again to re-run
