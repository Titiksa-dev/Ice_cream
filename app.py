from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('database.db')

@app.route('/flavors', methods=['GET', 'POST'])
def manage_flavors():
    conn = connect_db()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        is_seasonal = data.get('is_seasonal', False)
        cursor.execute("INSERT INTO flavors (name, is_seasonal) VALUES (?, ?)", (name, is_seasonal))
        conn.commit()
        return jsonify({"message": "Flavor added successfully"}), 201
    
    elif request.method == 'GET':
        cursor.execute("SELECT * FROM flavors")
        flavors = cursor.fetchall()
        return jsonify(flavors)

@app.route('/cart', methods=['POST'])
def add_to_cart():
    conn = connect_db()
    cursor = conn.cursor()
    data = request.get_json()
    flavor_id = data.get('flavor_id')
    quantity = data.get('quantity')
    
    cursor.execute("INSERT INTO cart (flavor_id, quantity) VALUES (?, ?)", (flavor_id, quantity))
    conn.commit()
    return jsonify({"message": "Item added to cart"}), 201

@app.route('/allergens', methods=['POST'])
def add_allergen():
    conn = connect_db()
    cursor = conn.cursor()
    data = request.get_json()
    name = data.get('name')
    
    cursor.execute("INSERT INTO allergens (name) VALUES (?)", (name,))
    conn.commit()
    return jsonify({"message": "Allergen added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
