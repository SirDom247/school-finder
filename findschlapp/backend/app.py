# Main Flask application file
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/institutions_db'
mongo = PyMongo(app)

# Create the Institution class
class Institution(mongo.db.Document):
    name = mongo.db.StringField()
    state = mongo.db.StringField()
    ownership = mongo.db.StringField()

# Endpoint to parse JSON and insert into the database
@app.route('/upload', methods=['POST'])
def upload_json():
    try:
        json_data = request.get_json()

        for institution_data in json_data.get('institutions', []):
            institution = Institution(**institution_data)
            institution.save()

        return jsonify({'message': 'Data uploaded successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to query institutions based on state
@app.route('/search', methods=['GET'])
def search_institutions():
    try:
        state = request.args.get('state')
        institutions = Institution.objects(state=state)

        result = [{'name': inst.name, 'state': inst.state, 'ownership': inst.ownership} for inst in institutions]
        return jsonify({'institutions': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
