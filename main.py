from flask import Flask, jsonify, request

app = Flask(__name__)

# Coada temporară de ouă
egg_queue = []

# Endpoint apelat de BOT-ul tău de pe calculator
@app.route('/add_egg', methods=['POST'])
def add_egg():
    global egg_queue
    data = request.json
    if data and "username" in data and "egg" in data:
        egg_queue.append(data)
        print(f"Primit de la bot local: {data['username']} -> {data['egg']}")
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error", "message": "Invalid data"}), 400

# Endpoint apelat de JOCUL din Roblox
@app.route('/get_eggs', methods=['GET'])
def get_eggs():
    global egg_queue
    current_eggs = egg_queue.copy()
    egg_queue.clear() # Golim coada după ce Roblox le-a preluat
    return jsonify(current_eggs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)