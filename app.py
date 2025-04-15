from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="",  
        database="hack"  
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    disease = request.form['disease']
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM doctors_data WHERE disease = %s"
    cursor.execute(query, (disease,))
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template('result.html', disease=disease, data=data)

if __name__ == '__main__':
    app.run(debug=True)
    

    


