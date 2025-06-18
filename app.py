from flask import Flask, request, jsonify, render_template
import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/extract', methods=['POST'])
def extract_text():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    file_path = os.path.join('static', file.filename)
    file.save(file_path)

    img = cv2.imread(file_path)
    text = pytesseract.image_to_string(img)

    return jsonify({'extracted_text': text})

if __name__ == '__main__':
    app.run(debug=True)
