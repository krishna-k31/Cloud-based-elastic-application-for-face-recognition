import os
from flask import Flask, request, jsonify

app = Flask(__name__) 

classification_results = None  # Placeholder for classification results

def load_classification_results(prediction_file):
    # Load classification results from the provided CSV file

    global classification_results
    classification_results = {}
    with open(prediction_file, 'r') as file:
        for line in file:

            filename, prediction = line.strip().split(',')
            classification_results[filename] = prediction

def process_image(file):

    global classification_results
    # Extract filename from the file object
    filename = os.path.splitext(file.filename)[0]
    # Look up prediction for the filename in the classification results

    return classification_results.get(filename, 'Unknown')

@app.route('/', methods=['POST'])
def recognize_faces():
    global classification_results
    # Load classification results
    prediction_file = 'classification_face_images_1000.csv'  # Path to classification results file
    # load_classification_results(prediction_file)
    classification_results = {}
    with open(prediction_file, 'r') as file:
        for line in file:

            filename, prediction = line.strip().split(',')
            classification_results[filename] = prediction
    
    file = request.files.get('inputFile')
    if not file:
        return jsonify({'error': 'File not provided'}), 400

    if classification_results is None:
        return jsonify({'error': 'Classification results not loaded yet'}), 500

    prediction = process_image(file)


    fname = file.filename
    fname = fname.split('.')[0]
    return fname+':'+str(prediction), 200
    # return jsonify({'filename': file.filename, 'prediction': prediction}), 200


if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=5000)