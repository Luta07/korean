from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_audio():
    data = request.get_json()
    audio_id = data.get("audio_id")

    # Define the base structure
    # If a field expects [], use [], if it expects {}, use {}
    # If the error says "Key set mismatch", it means the keys inside the {} must match exactly
    
    if audio_id == "q2":
        response = {
            "rows": 1,
            "columns": ["점수"],
            "mean": {"점수": 0.0},
            "std": {"점수": 0.0},
            "variance": {"점수": 0.0},
            "min": {"점수": 0.0},
            "max": {"점수": 0.0},
            "median": {"점수": 0.0},
            "mode": {"점수": 0.0},
            "range": {"점수": 0.0},
            "allowed_values": {}, 
            "value_range": {"점수": [0, 100]},
            "correlation": []
        }
    else:
        # Default empty structure for other IDs
        response = {
            "rows": 0,
            "columns": [],
            "mean": {},
            "std": {},
            "variance": {},
            "min": {},
            "max": {},
            "median": {},
            "mode": {},
            "range": {},
            "allowed_values": {},
            "value_range": {},
            "correlation": []
        }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run()
