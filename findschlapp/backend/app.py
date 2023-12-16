from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'institutions_db',
    'host': 'mongodb://localhost:27017/institutions_db',
}

mongo = MongoEngine(app)

class Institution(mongo.Document):
    name = mongo.StringField()
    state = mongo.StringField()
    ownership = mongo.StringField()

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
