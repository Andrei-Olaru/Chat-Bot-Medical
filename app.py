from flask import Flask, render_template, request, jsonify
from bardapi import Bard

app = Flask(__name__)

# Token-ul pentru API-ul Bard
BARD_TOKEN = 'fAi7DNpbELeJue9jhdoTbSIElLe3-WLUPfyxp0zpmkinRWewLV7PVk-qOgHPaA-zEquIlg.'

# Inițializarea obiectului Bard
bard = Bard(token=BARD_TOKEN)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.json.get('user_input')

    try:
        # Trimite întrebarea la Bard folosind token-ul API
        answer = bard.get_answer(str(user_input))['content']
        bot_response = answer  # Ajustează în funcție de structura răspunsului obținut

        # Poți face prelucrări suplimentare ale răspunsului aici, dacă este necesar

    except Exception as e:
        # Gestionează eventualele erori de la Bard
        print("Eroare de la Bard:", e)
        bot_response = "A apărut o eroare în timpul procesării cererii."

    # Returnează răspunsul bot-ului către client
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
