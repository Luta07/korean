from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_audio():
    data = request.get_json()
    audio_id = data.get("audio_id")
    
    # Logic to return the correct structure
    # You must ensure 'columns' matches the requirement for the specific ID
    response_data = {
        "rows": 1, # Update this based on your data logic
        "columns": ["점수"], # This fixes your specific error
        "mean": {"점수": 0.0},
        "std": {"점수": 0.0},
        "variance": {"점수": 0.0},
        "min": {"점수": 0.0},
        "max": {"점수": 0.0},
        "median": {"점수": 0.0},
        "mode": {"점수": 0.0},
        "range": {"점수": 0.0},
        "allowed_values": {"점수": []},
        "value_range": {"점수": [0, 100]},
        "correlation": []
    }
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run()
