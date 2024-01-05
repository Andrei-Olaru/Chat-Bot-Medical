// Funcție pentru adăugarea unui mesaj în containerul de chat
        function appendMessage(message, sender) {
            // Obține elementul HTML pentru containerul de chat
            const chatContainer = document.getElementById('chat-container');

            // Creează un element <div> pentru mesaj
            const messageElement = document.createElement('div');

            // Setează clasa mesajului în funcție de expeditor (utilizator sau bot)
            messageElement.className = sender === 'user' ? 'user-message' : 'bot-message';

            // Setează conținutul textului mesajului
            messageElement.textContent = message;

            // Adaugă elementul mesajului în containerul de chat
            chatContainer.appendChild(messageElement);
        }

        // Funcție pentru a trimite mesajul la server și a afișa răspunsul în containerul de chat
        function sendMessage() {
            // Obține valoarea din inputul utilizatorului
            const userInput = document.getElementById('user-input').value;

            // Verifică dacă există un mesaj de la utilizator
            if (userInput.trim() !== '') {
                // Trimite mesajul la server folosind Fetch API
                fetch('/send_message', {
                    method: 'POST',  // Metoda HTTP pentru a trimite date la server
                    headers: {
                        'Content-Type': 'application/json',  // Specifică tipul de conținut trimis
                    },
                    body: JSON.stringify({ user_input: userInput }),  // Convertește obiectul într-un string JSON
                })
                .then(response => response.json())  // Parsează răspunsul ca JSON
                .then(data => {
                    // Afișează răspunsul de la server în containerul de chat
                    appendMessage(userInput, 'user');  // Afișează mesajul utilizatorului
                    appendMessage(data.bot_response, 'bot');  // Afișează răspunsul bot-ului
                })
                .catch(error => console.error('Eroare:', error));  // Gestionează eventualele erori

                // Șterge conținutul din input pentru a pregăti utilizatorul pentru un nou mesaj
                document.getElementById('user-input').value = '';
            }
        }