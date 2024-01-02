from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Setează cheia API de la OpenAI
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')