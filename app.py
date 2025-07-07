from flask import Flask, render_template, request
import os
from resume_matcher import analyze_resume

app = Flask(__name__)
UPLOAD_FOLDER = 'resumes'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    result = analyze_resume(filepath)
    return render_template('result.html', result=result, filename=file.filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
