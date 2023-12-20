from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import json

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/institutions_db'
mongo = PyMongo(app)

# Assuming this is within your Flask app
file_path = 'institutions_data.json'

with open(file_path, 'r') as json_file:
    institutions_data = json.load(json_file)

# Insert data into MongoDB on startup
def insert_data_into_mongo():
    try:
        mongo.db.institutions.insert_many(institutions_data)
        print('Data inserted into MongoDB successfully.')
    except Exception as e:
        print(f'Error inserting data into MongoDB: {str(e)}')

# Endpoint to query institutions based on state
@app.route('/search', methods=['GET'])
def search_institutions():
    try:
        state = request.args.get('state')
        # Query MongoDB
        institutions = mongo.db.institutions.find({'state': state})

        # Process the query results
        result = [
            {'name': inst['name'], 'state': inst['state'], 'ownership': inst['ownership']}
            for inst in institutions
        ]

        return jsonify({'institutions': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get all institutions from the MongoDB database
@app.route('/all_institutions', methods=['GET'])
def get_all_institutions():
    try:
        institutions = mongo.db.institutions.find()

        # Process the query results
        result = [
            {'name': inst['name'], 'state': inst['state'], 'ownership': inst['ownership']}
            for inst in institutions
        ]

        return jsonify({'institutions': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ...

# Insert data into MongoDB on startup
insert_data_into_mongo()

if __name__ == '__main__':
    app.run(debug=True)
