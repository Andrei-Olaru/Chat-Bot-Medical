# Proiect Flask de Chatbot

Acest proiect reprezintă o aplicație web de chat care utilizează Flask pentru serverul backend și interacționează cu un API de chatbot. Aplicația permite utilizatorilor să trimită întrebări, iar chatbot-ul va furniza răspunsuri pe baza inteligenței artificiale.

## Funcționalități

- **Autentificare și Înregistrare:** Utilizatorii pot crea conturi și se pot autentifica pentru a avea acces la funcționalitățile chat-ului.

- **Interfață de Chat:** Utilizatorii pot trimite întrebări chatbot-ului și vor primi răspunsuri în timp real.

- **Formatare Răspunsuri:** Răspunsurile de la chatbot sunt formatate folosind Markdown pentru o afișare mai plăcută.

## Module și Biblioteci Folosite

- **Flask:** Framework-ul web pentru construirea aplicației.

- **Flask-Login:** Gestionarea autentificării și a sesiunilor utilizatorilor.

- **Flask-Bcrypt:** Criptarea parolelor utilizatorilor înainte de a le stoca în baza de date.

- **Bard API:** API-ul folosit pentru a obține răspunsuri de la chatbot.

- **Flask-CORS:** Permite cererile cross-origin (CORS) pentru a facilita accesul de la diverse surse.

- **Markdown2:** Conversie de text la format Markdown pentru a afișa răspunsurile chatbot-ului într-un mod mai plăcut.

## Instalare

1. **Clonează acest repository:**
   ```bash
   git clone https://github.com/Andrei-Olaru/Chat-Bot-Medical.git

2. **Instalează dependențele folosind pip:**

   ```bash
   pip install -r requirements.txt
## Configurare:
3. **Obține un token pentru API-ul Bard și actualizează variabila BARD_TOKEN în app.py cu acesta.**
- Rulează aplicația:
   ``` bash
   python app.py
- Accesează aplicația într-un browser la adresa http://localhost:5000/.

## Comenzi
- Pentru a rula aplicația, utilizează comanda:

   ```bash
   python app.py
-Pentru a instala dependențele, utilizează comanda:
   ```bash
   pip install -r requirements.txt