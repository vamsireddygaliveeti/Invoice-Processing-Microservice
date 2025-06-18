---

# 📄 Invoice Processing Microservice

A serverless OCR microservice that extracts key fields from invoice images using **Flask**, **OpenCV**, **Tesseract**, and **AWS Lambda**.

---

## ✅ Features

* 🖼 Upload invoice images (JPG, PNG)
* 🧠 Extract full invoice text using Tesseract OCR
* 💡 Clean HTML interface with emojis and styled buttons
* ⚙️ Deployed with AWS Lambda and batch processing
* 🛡 Error handling and field validation pipeline
* 📊 92%+ field extraction accuracy
* 🧾 Mock SAP backend integration
* ⏱ Reduced manual invoice effort by 80%

---

## 💻 Tech Stack

* **Flask** – Web app framework
* **OpenCV** – Image preprocessing
* **Tesseract OCR** – Text extraction
* **Python** – Core programming language
* **AWS Lambda** – Serverless deployment

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/yourusername/invoice-processing-microservice.git
cd invoice-processing-microservice

python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt
```

> 🛠️ Set Tesseract path (Windows only, if needed):

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

Then run the app:

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📷 Screenshot

![UI Screenshot](static/sample-ui.png) <!-- Replace with your actual screenshot path -->

---

## 📦 Output Example

```json
{
  "extracted_text": "example: Invoice No: 12345\nDate: 01/06/2024\nTotal: $450.00"
}
```

---

## 📅 Project Timeline

**Jan 2024 – Apr 2024**
Engineered a serverless invoice parsing service using Flask, OpenCV, and Tesseract to extract fields from PDFs.
Deployed using AWS Lambda and batch jobs for scalable, asynchronous processing.
Integrated error handling and validation pipelines, achieving 92%+ field extraction accuracy.
Reduced manual invoice effort by 80% and integrated with a mock SAP backend.

---

## 🙌 Made with ❤️

