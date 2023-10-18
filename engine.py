from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
import os, json

app = Flask(__name__)

# Configure your MySQL connection
host="localhost"
user="root"
port="3306"
password="9271"
database="STUDY"

db = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

@app.route('/add_flashcard', methods=['POST'])
def add_flashcard():

    if request.method == 'POST':
        # Get flashcard data from the form
        request_body = json.loads(request.data)
        subject = request_body['subject']
        question = request_body['question']
        answer = request_body['answer']

        # Insert the flashcard data into the database
        cursor = db.cursor()
        cursor.execute("INSERT INTO flashcards (subject, question, answer) VALUES (%s, %s, %s)",
                       (subject, question, answer))
        db.commit()
        cursor.close()

        return redirect(url_for('main_page'))  # Redirect back to the main page

@app.route('/all_flashcards')
def all_flashcards():
    print(db)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM flashcards")
    flashcards = cursor.fetchall()
    cursor.close()
    
    return render_template('all_flashcards.html', flashcards=flashcards)

@app.route('/')
def main_page():
    return render_template('index.html')

# if __name__ == '__main__':
#     app.run()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)