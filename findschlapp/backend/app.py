from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/institutions'

mongo = PyMongo(app)

class Institution:
    def __init__(self, name, state, ownership):
        self.name = name
        self.state = state
        self.ownership = ownership

# Endpoint to parse JSON and insert into the database
@app.route('/upload', methods=['POST'])
def upload_json():
    try:
        json_data = request.get_json()

        for institution_data in json_data.get('institutions', []):
            institution = Institution(
                name=institution_data.get('name'),
                state=institution_data.get('state'),
                ownership=institution_data.get('ownership')
            )
            # Insert into MongoDB
            mongo.db.institutions.insert_one({
                'name': institution.name,
                'state': institution.state,
                'ownership': institution.ownership
            })

        return jsonify({'message': 'Data uploaded successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to query institutions based on state
@app.route('/search', methods=['GET'])
def search_institutions():
    try:
        state = request.args.get('state')
        # Query MongoDB
        institutions = mongo.db.institutions.find({'state': state})

        result = [{'name': inst['name'], 'state': inst['state'], 'ownership': inst['ownership']} for inst in institutions]
        return jsonify({'institutions': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
