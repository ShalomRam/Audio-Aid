import nltk
from flask import Flask, request, render_template
from text_processing.preprocess import preprocess_text
from text_processing.summarize import summarize_text
from text_to_speech.tts import text_to_speech

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_text():
    input_text = request.form['input_text']
    summarized_text = summarize_text(input_text, 3)
    text_to_speech(summarized_text)
    return "Processed Text: " + summarized_text

if __name__ == '__main__':
    app.run(debug=True)
