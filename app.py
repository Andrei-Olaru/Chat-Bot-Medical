from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Setează cheia API de la OpenAI
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.json.get('user_input')

    # Trimite întrebarea la ChatGPT folosind cheia de API
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Specifică modelul ChatGPT pe care vrei să-l utilizezi
            prompt=user_input,
            max_tokens=100  # Numărul maxim de tokeni în răspuns
        )
        bot_response = response.choices[0].text.strip()
    except Exception as e:
        # Gestionează eventualele erori de la ChatGPT
        print("Eroare de la ChatGPT:", e)
        bot_response = "A apărut o eroare în timpul procesării cererii."

    # Returnează răspunsul bot-ului către client
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)