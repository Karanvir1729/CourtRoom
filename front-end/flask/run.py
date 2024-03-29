from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import csv
import os
from Review_Generators.OpenAI_review_generators import get_OpenAI_review_dict
from Review_Generators.cohere_web_connect_review import get_cohere_review_dict
from Review_Generators.replicate_review_generator import generate_replicate_review
from Cohere_Review_Classification.cohere_classifier import get_scores
from AutoKeyWords.chat_gpt_key_word_generation import get_auto_key_words

app = Flask(__name__, 
            template_folder='apps/templates',  # Correct path to your templates
            static_folder='apps/static')       # Correct path to your static files

# Ensure you set a secure secret key
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
upload_folder = app.config['UPLOAD_FOLDER']
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

# Check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'csv'

@app.route('/')
def index():
    return render_template('index.html', current_user=None)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Handle file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    # Check if file is allowed and save it
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File successfully uploaded')
    else:
        flash('Invalid file format')
        return redirect(request.url)
    
    # Redirect to next page after processing
    return redirect(url_for('next_page'))

@app.route('/next')
def next_page():
    # Create a dummy current_user object with minimal properties
    current_user = {'is_authenticated': False}
    return render_template('next.html', current_user=current_user)

@app.route('/word-suggestions')
def word_suggestions():
    # Example list of words. You can replace this with a more sophisticated word source.
    words = ["novelty", "nature", "climate change", "technology", "innovation", "health", "science"]
    return jsonify(words)

# Calculation!!!!
@app.route('/perform_calculation', methods=['POST'])
def perform_calculation():
    data = request.get_json()
    keywords = data['keywords']
    problem = data.get('problem', 'No problem statement provided')
    solution = data.get('solution', 'No solution statement provided')

    #lst = get_auto_key_words(problem, solution)[0:5:2]  # only first 5 auto key words, skipping 1, , rest on the user
    lst = [get_auto_key_words(problem, solution)[0]]  # only first 5 auto key words, skipping 1, , rest on the user

    for i in lst:
        keywords.append(i)
    print(f"LISSSST{lst}")
    openai_selected = data.get('openai', False)
    cohere_selected = data.get('cohere', False)
    replicate_selected = data.get('replicate', False)

    # Print received data on the terminal for debugging
    print(f"Received Data - Keywords: {keywords}, Problem: {problem}, Solution: {solution}, OpenAI: {openai_selected}, Cohere: {cohere_selected}, Replicate: {replicate_selected}")


    # Print received data on the terminal for debugging
    #print(f"Received Data - Keywords: {keywords}, Problem: {problem}, Solution: {solution}")

    # Put function here!
    #calculation_results = [get_personalities(keyword, problem, solution, gpt=0) for keyword in keywords]
    #key_words = ["novelty", "nature", "climate change", "convinence"]  # Get from front end
    calculation_results = []
    if (openai_selected): # check if we are allowed to use chatgpt
        out = get_OpenAI_review_dict(keywords, solution, problem)
        calculation_results += [i for i in out.values()]  # input chatgpt reviews

    if(replicate_selected): # check if we are allowed to use replicate
        out = generate_replicate_review(keywords, problem, solution)
        calculation_results += [i for i in out.values()]  # input replicate reviews

    if (cohere_selected):  # check if we are allowed to use replicate
        out = get_cohere_review_dict(keywords, problem, solution)
        calculation_results += [f"{i[0]} \n Sources {' '.join(i[1])}"  for i in out.values()]  # input replicate reviews

    scores = get_scores(calculation_results)
    string_list = ' '.join(map(str, scores))
    calculation_results[-1] += string_list

    return jsonify({
        "status": "success",
        "message": "Calculation performed",
        "keywords": keywords,
        "problem": problem,
        "solution": solution,
        "calculation_result": calculation_results
        
    })




def get_personalities(keyword, problem, solution, gpt):
    # Implement your logic here
    # This is a placeholder return
    out = get_OpenAI_review_dict(key_words, solution, problem)
    calculation_result = out["convinence"]





@app.route('/search', methods=['POST'])
def search():
    search_id = request.form.get('search_id')
    result = None

    try:
        with open(os.path.join('uploads', 'AI_EarthHack_Dataset.csv'), newline='', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['id'] == search_id:
                    result = row
                    break
    except UnicodeDecodeError as e:
        print(f"Error reading CSV: {e}")
        # Handle the error appropriately

    current_user = {'is_authenticated': False}
    return render_template('next.html', result=result, current_user=current_user)


if __name__ == '__main__':
    app.run(debug=True)
