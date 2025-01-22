from flask import Flask, request, jsonify, render_template
import random
import json

app = Flask(__name__)

# Simulated genetic data and analysis results
def analyze_genetic_data(data):
    """Simulates the analysis of genetic data and returns health insights."""
    insights = {
        "nutrition": {
            "vitamin_d": "Your genetic markers indicate you may have low Vitamin D levels. Consider supplements.",
            "lactose": "You might be lactose intolerant. Opt for dairy-free alternatives."
        },
        "fitness": {
            "endurance": "Your genes suggest a higher capacity for endurance-based activities. Try running or cycling.",
            "recovery": "Average recovery rate. Ensure proper hydration and rest after workouts."
        },
        "health_risks": {
            "diabetes": "Slightly elevated risk of Type 2 diabetes. Maintain a balanced diet and regular exercise.",
            "heart_disease": "Normal risk levels. Continue regular check-ups."
        }
    }
    return insights

@app.route('/')
def home():
    return "<h1>Welcome to the Genetic Health Optimization Platform!</h1><form action='/upload' method='post' enctype='multipart/form-data'><input type='file' name='genetic_file'><button type='submit'>Upload</button></form>"

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('genetic_file')
    if file:
        try:
            data = file.read().decode('utf-8')
        except (UnicodeDecodeError, AttributeError):
            return jsonify({"status": "error", "message": "Uploaded file is not a valid text file."})
        insights = analyze_genetic_data(data)
        return jsonify({"status": "success", "insights": insights})
    return jsonify({"status": "error", "message": "No file uploaded."})

@app.route('/sample-data', methods=['GET'])
def sample_data():
    sample_result = analyze_genetic_data("sample_genetic_data")
    return jsonify(sample_result)

if __name__ == '__main__':
    app.run(debug=True)
S