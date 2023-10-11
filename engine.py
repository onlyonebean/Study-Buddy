import mysql.connector

# Create a database connection
db = mysql.connector.connect(
    host="localhost:3306",
    user="Nona-Pahia",
    password="9271",
    database="study"
)


from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="TEST"
)

# Create a cursor for database operations
cursor = db.cursor()

@app.route('/add_flashcard', methods=['POST'])
def add_flashcard():
    data = request.get_json()
    subject = data['subject']
    question = data['question']
    answer = data['answer']

    # Insert the flashcard data into the database
    insert_query = "INSERT INTO flashcards (subject, question, answer) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (subject, question, answer))
    db.commit()

    return jsonify({'message': 'Flashcard added successfully'})

if __name__ == '__main__':
    app.run()

