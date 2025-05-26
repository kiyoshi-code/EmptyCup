from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy data for design agencies
agencies = [
    {
        "id": 1,
        "name": "Epic Designs",
        "rating": "rating1.png",
        "description": "Passionate team of 4 designers working out of Banglore with an experience of 4 years.",
        "projects": 57,
        "years": 8,
        "price_tier": "$$",
        "contacts": ["+91-984532853", "+91-984532854"],
        "is_shortlisted": False
    },
    {
        "id": 2,
        "name": "Studio-D3",
        "rating": "rating2.png",
        "description": "Passionate team of 4 designers working out of Banglore with an experience of 4 years.",
        "projects": 43,
        "years": 6,
        "price_tier": "$$$",
        "contacts": ["+91-984532853", "+91-984532854"],
        "is_shortlisted": False
    },
    {
        "id": 3,
        "name": "House of designs",
        "rating": "rating2.png",
        "description": "This is a random paragraph",
        "projects": 35,
        "years": 5,
        "price_tier": "$$",
        "contacts": ["+91-984532853"],
        "is_shortlisted": False
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/agencies', methods=['GET'])
def get_agencies():
    return jsonify(agencies)

@app.route('/api/agencies/<int:agency_id>/shortlist', methods=['POST'])
def toggle_shortlist(agency_id):
    agency = next((a for a in agencies if a['id'] == agency_id), None)
    if agency:
        agency['is_shortlisted'] = not agency['is_shortlisted']
        return jsonify({"success": True, "is_shortlisted": agency['is_shortlisted']})
    return jsonify({"error": "Agency not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
