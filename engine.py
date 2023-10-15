from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configure your MySQL connection
db = {
    "host":"Nona-Pahia",
    "user":"Fiona",
    "password":"9271",
    "database":"STUDY"
}

@app.route('/add_flashcard', methods=['POST'])
def add_flashcard():
    if request.method == 'POST':
        # Get flashcard data from the form
        subject = request.form['subject']
        question = request.form['question']
        answer = request.form['answer']

        # Insert the flashcard data into the database
        cursor = db.cursor()
        cursor.execute("INSERT INTO flashcards (subject, question, answer) VALUES (%s, %s, %s)",
                       (subject, question, answer))
        db.commit()
        cursor.close()

        return redirect(url_for('main_page'))  # Redirect back to the main page

@app.route('/all_flashcards')
def all_flashcards():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM flashcards")
    flashcards = cursor.fetchall()
    cursor.close()
    
    return render_template('all_flashcards.html', flashcards=flashcards)

@app.route('/')
def main_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
