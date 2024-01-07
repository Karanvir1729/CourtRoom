from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import csv
import os

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

@app.route('/process_problem_solution', methods=['POST'])
def process_problem_solution():
    data = request.get_json()
    keywords = data.get('keywords', [])
    problem = data.get('problem', 'No problem statement provided')
    solution = data.get('solution', 'No solution statement provided')

    # Perform a simple calculation
    calculation_result = 1 + 1

    return jsonify({
        "status": "success",
        "message": "Calculation performed",
        "keywords": keywords,
        "problem": problem,
        "solution": solution,
        "calculation_result": calculation_result
    })


@app.route('/perform_calculation', methods=['POST'])
def perform_calculation():
    data = request.get_json()
    keywords = data['keywords']
    problem = data.get('problem', 'No problem statement provided')
    solution = data.get('solution', 'No solution statement provided')
    body: JSON.stringify({ 
    keywords: keywords, 
    problem: yourProblemVariable, 
    solution: yourSolutionVariable 
})



    # Perform a simple calculation
    calculation_result = 1 + 1

    return jsonify({
        "status": "success", 
        "message": "Calculation performed", 
        "keywords": keywords, 
        "problem": problem, 
        "solution": solution,
        "calculation_result": calculation_result
    })




@app.route('/search', methods=['POST'])
def search():
    search_id = request.form.get('search_id')
    result = None

    with open(os.path.join('uploads', 'AI_EarthHack_Dataset.csv'), newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['id'] == search_id:
                result = row
                break
    # Create a dummy current_user object
    current_user = {'is_authenticated': False}

    return render_template('next.html', result=result, current_user=current_user)


if __name__ == '__main__':
    app.run(debug=True)
