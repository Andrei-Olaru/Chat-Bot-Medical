// Funcție pentru adăugarea unui mesaj în containerul de chat
        function appendMessage(message, sender) {
            // Obține elementul HTML pentru containerul de chat
            const chatContainer = document.getElementById('chat-container');

            // Creează un element <div> pentru mesaj
            const messageElement = document.createElement('div');

            // Setează clasa mesajului în funcție de expeditor (utilizator sau bot)
            messageElement.className = sender === 'user' ? 'user-message' : 'bot-message';

            // Setează conținutul HTML al mesajului
            messageElement.innerHTML = message;

            // Adaugă elementul mesajului în containerul de chat
            chatContainer.appendChild(messageElement);
        }

        // Funcție pentru a trimite mesajul la server și a afișa răspunsul în containerul de chat
        function sendMessage() {
            // Afișează iconița de încărcare
            document.getElementById('loading-icon').style.display = 'inline-block';

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
                    // Ascunde iconița de încărcare după ce se primește răspunsul de la server
                    setTimeout(() => {
                    document.getElementById('loading-icon').style.display = 'none';
                    }, 0); // Așteaptă 0 secunde

                    // Afișează răspunsul de la server în containerul de chat
                    appendMessage(userInput, 'user');  // Afișează mesajul utilizatorului
                    appendMessage(data.bot_response, 'bot');  // Afișează răspunsul bot-ului
                })
                .catch(error => {
                    console.error('Eroare:', error);
                    // Asigura-te că ascunzi iconița de încărcare în caz de eroare
                    document.getElementById('loading-icon').style.display = 'none';
                });

                // Șterge conținutul din input pentru a pregăti utilizatorul pentru un nou mesaj
                document.getElementById('user-input').value = '';
            }
        }


        document.getElementById("notificationButton").addEventListener("click", function() {
            var popup = document.getElementById("notificationPopup");
            popup.classList.toggle("hidden");
        });

        document.getElementById("subscribeButton").addEventListener("click", function() {
            var emailInput = document.getElementById("userEmail").value;
            if (emailInput) {
                // Ascunde popup-ul
                var popup = document.getElementById("notificationPopup");
                popup.classList.add("hidden");
        
                // Afișează mesajul de mulțumire
                var thankYouMessage = document.getElementById("thankYouMessage");
                thankYouMessage.classList.remove("hidden");
        
                // Resetarea valorii din câmpul de email
                document.getElementById("userEmail").value = "";
        
                // Ascunde mesajul de mulțumire după 5 secunde
                setTimeout(function() {
                    thankYouMessage.classList.add("hidden");
                }, 5000); // 5000 milisecunde = 5 secunde
            }
        });

        document.getElementById("feedbackButton").addEventListener("click", function() {
            var modal = document.getElementById("feedbackModal");
            modal.classList.toggle("hidden");  // Adaugă sau elimină clasa 'hidden' pentru a afișa sau ascunde modalul
        });

var emojiOptions = document.querySelectorAll(".emoji-option");
emojiOptions.forEach(function(option) {
    option.addEventListener("click", function() {
        var modal = document.getElementById("feedbackModal");
        modal.classList.add("hidden");
    });
});

document.addEventListener("DOMContentLoaded", function() {
    // Selectează toate butoanele de emoticon
    const emojiButtons = document.querySelectorAll('.emoji-option');

    // Adaugă un eveniment de clic pentru fiecare buton de emoticon
    emojiButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Ascunde opțiunile de emoticon
            document.querySelector('.emoji-options').style.display = 'none';
            
            // Crează și adaugă pop-up-ul de feedback
            const popup = document.createElement('div');
            popup.className = 'feedback-popup';
            popup.innerHTML = '<i class="fas fa-thumbs-up"></i> Mulțumim pentru feedback!';
            document.body.appendChild(popup);

            // Șterge pop-up-ul după 2 secunde
            setTimeout(() => {
                popup.remove();
            }, 2000);
        });
    });
});


